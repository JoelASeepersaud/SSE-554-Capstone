#API key with getter
polygonAPIkey = 'GV5KLmPDZ8oAG2DVkV5_ye1MoyLcFc6e'

def getPolygonAPIkey():
    return polygonAPIkey

#Configuration dictionary with getter and setter
configurations =    {'date': '2023-01-03',
                    'volume_min': 10000000,
                    }

def getConfigurations():
    return configurations

def setConfigurations(field, value):
    configurations.update({field : value})