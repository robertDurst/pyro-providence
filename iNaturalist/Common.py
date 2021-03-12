from iNaturalist.Location import Location
from iNaturalist.ObservationResult import ObservationResult

##################################################
#                   External                     #
##################################################
def convertToObservationResults(observations):
    observationResults = []

    for observation in observations:
        observationResults.append(parseObservation(observation))
    
    return observationResults

def sortObservationsByMonth(observations):
    dictt = {}
    for observation in observations:
        if (observation.time_observed_at == None):
            continue
        if (not observation.time_observed_at.month in dictt):
            dictt[observation.time_observed_at.month] = []
        dictt[observation.time_observed_at.month].append(observation)
    return dictt

def sortObservationsByHour(observations):
    dictt = {}
    for observation in observations:
        if (observation.time_observed_at == None):
            continue
        if (not observation.time_observed_at.hour in dictt):
            dictt[observation.time_observed_at.hour] = []
        dictt[observation.time_observed_at.hour].append(observation)
    return dictt

##################################################
#                   Internal                     #
##################################################
def parseObservation(observationJson):
    return ObservationResult(
        observationJson["quality_grade"],
        observationJson["time_observed_at"],
        observationJson["taxon_geoprivacy"],
        parseGeoJson(observationJson["geojson"])
    )

def parseGeoJson(geoJson):
    try:
        return Location(
            geoJson["coordinates"],
            geoJson["type"]
        )
    except:
        None