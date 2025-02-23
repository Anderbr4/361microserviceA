import random 
import time 


def generate_random_date():

    rando_month = str(random.randint(1, 12))
    rando_day = str(random.randint(1, 31))
    if(rando_month == 2):

        rando_day = str(random.randint(1, 28))

    rando_year = str(random.randint(10, 25))
    return rando_month+"/"+rando_day+"/"+rando_year


print(generate_random_date())