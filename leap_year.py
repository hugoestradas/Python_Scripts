def is_leap(year):
    leap = False
    
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                leap = True
            else:
                return leap
        else:
            return leap
    else:
        return leap
    return leap
