import zmq
import random 
import datetime 

def generate_random_date():
    """Generate a random future date within the next year."""
    start_date = datetime.date.today()
    days_to_add = random.randint(1, 365)  # Ensuring at least 1 day ahead

    rando_date = start_date + datetime.timedelta(days=days_to_add)

    return rando_date.strftime("%Y-%m-%d")  # Convert to string format for consistency

if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:6666")

    print("🔄 Random Date Microservice Running... Listening on port 6666")

    while True:
        new_message = socket.recv()
        request = new_message.decode()
        print(f"📩 Received Request: {request}")

        # Always generate and send a new random date
        random_date = generate_random_date()
        socket.send_string(random_date)
        print(f"📤 Sent Random Date: {random_date}")
