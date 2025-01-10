import oracledb
from flask import Flask, request, jsonify

# Flask app initialization
app = Flask(__name__)

# OracleDB connection configuration
oracledb.init_oracle_client()  # Use if Oracle Instant Client is required on your system
dsn = oracledb.makedsn("192.168.137.1", 1521, service_name="XE")  # Update host, port, and service name
connection = oracledb.connect(user="system", password="bhavik", dsn=dsn)

# Endpoint: Get all flights
@app.route('/flights', methods=['GET'])
def get_flights():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM flights")
    rows = cursor.fetchall()
    cursor.close()

    flights = [
        {
            "flight_id": row[0],
            "flight_number": row[1],
            "departure_city": row[2],
            "arrival_city": row[3],
            "departure_time": row[4],
            "arrival_time": row[5],
            "available_seats": row[6],
            "status": row[7],
        }
        for row in rows
    ]
    return jsonify(flights)

# Endpoint: Add a new flight
@app.route('/add-flight', methods=['POST'])
def add_flight():
    data = request.json
    cursor = connection.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO flights (flight_id, flight_number, departure_city, arrival_city, departure_time, arrival_time, available_seats, status)
            VALUES (seq_flight_id.NEXTVAL, :1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD HH24:MI:SS'), TO_DATE(:5, 'YYYY-MM-DD HH24:MI:SS'), :6, 'Scheduled')
            """,
            [
                data['flight_number'],
                data['departure_city'],
                data['arrival_city'],
                data['departure_time'],
                data['arrival_time'],
                data['available_seats'],
            ],
        )
        connection.commit()
        return jsonify({"message": "Flight added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()

# Endpoint: Book a flight
@app.route('/book-flight', methods=['POST'])
def book_flight():
    data = request.json
    cursor = connection.cursor()
    try:
        # Check available seats
        cursor.execute("SELECT available_seats FROM flights WHERE flight_id = :1", [data['flight_id']])
        available_seats = cursor.fetchone()
        if not available_seats or available_seats[0] <= 0:
            return jsonify({"message": "No available seats for this flight"}), 400

        # Insert booking
        cursor.execute(
            """
            INSERT INTO bookings (booking_id, flight_id, passenger_id, seat_number, booking_date)
            VALUES (seq_booking_id.NEXTVAL, :1, :2, :3, SYSDATE)
            """,
            [data['flight_id'], data['passenger_id'], data['seat_number']],
        )

        # Update available seats
        cursor.execute(
            "UPDATE flights SET available_seats = available_seats - 1 WHERE flight_id = :1", [data['flight_id']]
        )
        connection.commit()
        return jsonify({"message": "Flight booked successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()

# Endpoint: Update flight status
@app.route('/update-flight-status', methods=['PUT'])
def update_flight_status():
    data = request.json
    cursor = connection.cursor()
    try:
        cursor.execute(
            "UPDATE flights SET status = :1 WHERE flight_id = :2",
            [data['status'], data['flight_id']],
        )
        connection.commit()
        return jsonify({"message": "Flight status updated successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()

if __name__ == '__main__':
    app.run(debug=True)
