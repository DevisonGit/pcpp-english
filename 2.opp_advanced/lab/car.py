class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def get_pressure(self):
        return self.pressure

    def pump(self, pressure):
        self.pressure = pressure


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = 'stopped'

    def start(self):
        self.state = 'running'

    def stop(self):
        self.state = 'stopped'

    def get_state(self):
        return self.state


class Vehicle:
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires


# Create two sets of tires
city_tires = Tires(size=15)
off_road_tires = Tires(size=18)

# Create two engines
electric_engine = Engine(fuel_type='electric')
petrol_engine = Engine(fuel_type='petrol')

# Instantiate two vehicles
city_car = Vehicle(VIN='CITY12345', engine=electric_engine, tires=city_tires)
all_terrain_car = Vehicle(VIN='AT45678', engine=petrol_engine, tires=off_road_tires)

# Play with the city car
print("City Car:")
print(f"VIN: {city_car.VIN}")
print(f'Fuel type: { city_car.engine.fuel_type}')
print(f'Tire size: { city_car.tires.size}')
print(f"Engine state: {city_car.engine.get_state()}")
city_car.engine.start()
print(f"Engine state after starting: {city_car.engine.get_state()}")
print(f"Tire pressure: {city_car.tires.get_pressure()}")
city_car.tires.pump(30)
print(f"Tire pressure after pumping: {city_car.tires.get_pressure()}")
city_car.engine.stop()
print(f"Engine state after stopping: {city_car.engine.get_state()}")

# Play with the all-terrain car
print("\nAll-Terrain Car:")
print(f"VIN: {all_terrain_car.VIN}")
print(f'Fuel type: { all_terrain_car.engine.fuel_type}')
print(f'Tire size: { all_terrain_car.tires.size}')
print(f"Engine state: {all_terrain_car.engine.get_state()}")
all_terrain_car.engine.start()
print(f"Engine state after starting: {all_terrain_car.engine.get_state()}")
print(f"Tire pressure: {all_terrain_car.tires.get_pressure()}")
all_terrain_car.tires.pump(35)
print(f"Tire pressure after pumping: {all_terrain_car.tires.get_pressure()}")
all_terrain_car.engine.stop()
print(f"Engine state after stopping: {all_terrain_car.engine.get_state()}")
