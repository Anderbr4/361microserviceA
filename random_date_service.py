import zmq
import random 
import datetime 


def generate_random_date():

    # actually the rando month day year thing is tough because you may never get leap years/some months have 30 vs. 31 days. 
    # so having a set day and then adding a random period of time to it seems better. 

    # https://www.geeksforgeeks.org/how-to-add-days-to-a-date-in-python/
    # accessed 02.22.25
    # specifically referencing the use of timedelta function so I can add days to a date
    # 
    start_date = datetime.date.today()
    days_to_add = random.randint(0,365)

    rando_date = start_date + datetime.timedelta(days=days_to_add)

    return rando_date



if __name__ == "__main__":



    context = zmq.Context()

    socket = context.socket(zmq.REP)

    socket.bind("tcp://*:6666")

    while True:
        new_message = socket.recv()
        print(f"{new_message.decode()}")

        if len(new_message) > 0:
            if new_message.decode() == 'Quit': # Client asked server to quit
                break

        confirmation = str(generate_random_date())

        socket.send_string(confirmation)
    # Make a clean exit.
    context.destroy()

