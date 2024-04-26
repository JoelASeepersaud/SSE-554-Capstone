#API key with getter
polygonAPIkey = 'GV5KLmPDZ8oAG2DVkV5_ye1MoyLcFc6e'

def getPolygonAPIkey():
    return polygonAPIkey

#Configuration dictionary with getter and setter
configurations =    {'date': '',
                    'volume_min': -1,
                    }

def getConfigurations():
    return configurations

def setConfigurations(field, value):
    configurations.update({field : value})