def minutes_to_hour_and_minutes(minutes):
    hours = 0
    while minutes > 59:
        minutes -= 60;
        hours += 1;
    return str(hours) + ':' + str(minutes)