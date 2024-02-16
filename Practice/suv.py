from vehicle import Vehicle

class Suv(Vehicle):

    def __init__(self,manufacturer, model, mileage, vehicle_type, fuel, power, transmission,registration):
        super().__init__(manufacturer, model, mileage, vehicle_type, fuel, power, transmission,registration)
