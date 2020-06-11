import math

def format(time):
    minutes, hours = math.modf(time)
    minutes = (round(minutes, 2)*60)/100
    return '{0:.2f}'.format(hours+minutes)

def extract(time):
    minutes, hours = math.modf(float(time))
    minutes = (round(minutes, 2)*100)/60
    return hours+minutes