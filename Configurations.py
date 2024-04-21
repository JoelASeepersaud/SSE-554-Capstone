polygonAPIkey = 'GV5KLmPDZ8oAG2DVkV5_ye1MoyLcFc6e'
configurations =    {'date': '',
                    'volume_min': -1,
                    }

def getPolygonAPIkey():
    return polygonAPIkey

def getConfigurations():
    return configurations

def setConfigurations(field, value):
    configurations.update({field : value})