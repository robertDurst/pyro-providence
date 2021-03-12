from dateutil import parser

# An object with all the interesting stuff as returned from this endpoint:
# https://api.inaturalist.org/v1/docs/#!/Observations/get_observations
class ObservationResult:
    def __init__(
        self, 
        quality,
        time_observed_at,
        geoprivacy,
        location):

        self.quality = quality
        # datetime object
        try:
            self.time_observed_at = parser.parse(time_observed_at)
        except:
            self.time_observed_at = None
        
        self.geoprivacy = geoprivacy
        self.location = location

        # TODO Rob.D 3/11/2021: include these fields
        # * self.positional_accuracy
        # * self.time_zone_offselt

    def __str__(self):
        return "Observation time: " + self.time_observed_at + "\nLocation: " + self.location.__str__()
        
