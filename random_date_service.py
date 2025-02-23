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


# print(generate_random_date())