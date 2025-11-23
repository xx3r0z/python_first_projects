def parse(feetinches):
    #.split() with cut up a string at the specified place given to it and
    #put the strings in a list
    parts = feetinches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    #Using return to return 2 values in this way returns a tuple with the values
    return feet, inches

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters