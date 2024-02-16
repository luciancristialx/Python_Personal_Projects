class Vehicle:

    def __init__(self, manufacturer, model, mileage, vehicle_type, fuel, power, transmission,registration):
        self.manufacturer = manufacturer.capitalize()
        self.model = model
        self.mileage = mileage
        self.vehicle_type = vehicle_type.capitalize()
        self.fuel = fuel.capitalize()
        self.power = power
        self.transmission = transmission.upper()
        self.registration = registration

    def __str__(self):
        return f"Manufacturer: {self.manufacturer}\n" \
               f"Model: {self.model}\n" \
               f"Type: {self.vehicle_type}\n" \
               f"Mileage: {self.mileage}km\n" \
               f"Registration: {self.registration}\n" \
               f"Fuel: {self.fuel}\n" \
               f"Power: {self.power}\n" \
               f"Transmission: {self.transmission}\n"



