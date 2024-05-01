
#API key with getter
polygonAPIkey = 'GV5KLmPDZ8oAG2DVkV5_ye1MoyLcFc6e'

def getPolygonAPIkey():
    return polygonAPIkey

#Configuration dictionary with getter and setter
configurations =    [('date', '2023-01-03', 'Date'),
                     ('volume_min', 10000000, 'Volume Minimum')
                     ]

def getConfigurations():
    return configurations

def setConfigurations(field, value):
    for index in range(len(configurations)):
        if configurations[index][0] == field:
            configurations[index] = (configurations[index][0], value, configurations[index][2])
            return
