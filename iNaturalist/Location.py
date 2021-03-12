class Location:
    def __init__(self, coordinates, coordinateType):
        self.coordinates = coordinates
        self.coordinateType = coordinateType

    # TODO Rob.D: more gracefully deal with NoneType coordinates
    #             and furthermore consider other coordinate types
    def __str__(self):
        if len(self.coordinates):
            return "(" + str(self.coordinates[0]) + ", " + str(self.coordinates[1]) + ")"
        else:
            return "()"