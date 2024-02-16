import pandas
from car import Car
from truck import Truck
from suv import Suv

fleet = []
df1 = pandas.read_excel('C:\\Users\\lucia\\PycharmProjects\\PythonCourse\\Practice\\Documents\\fleet.xlsx',sheet_name =
'Sheet1')

for car in df1.index:
    v_manufacturer = df1.iloc[car][0]
    v_model = df1.iloc[car][1]
    v_mileage = df1.iloc[car][2]
    v_type = df1.iloc[car][3]
    v_fuel = df1.iloc[car][4]
    v_power = df1.iloc[car][5]
    v_transmission = df1.iloc[car][6]
    v_registration = df1.iloc[car][7]
    if v_type == "Car":
        car = Car(manufacturer = v_manufacturer, model = v_model, mileage = v_mileage, vehicle_type =  v_type, fuel = v_fuel,
            power = v_power, transmission = v_transmission, registration = v_registration)
        fleet.append(car)
    elif v_type == "Truck":
        truck = Truck(manufacturer = v_manufacturer, model = v_model, mileage = v_mileage, vehicle_type =  v_type, fuel = v_fuel,
            power = v_power, transmission = v_transmission, registration = v_registration)
        fleet.append(truck)
    else:
        suv = Suv(manufacturer = v_manufacturer, model = v_model, mileage = v_mileage, vehicle_type =  v_type,
            fuel = v_fuel, power = v_power, transmission = v_transmission, registration = v_registration)
        fleet.append(suv)

print(fleet)


