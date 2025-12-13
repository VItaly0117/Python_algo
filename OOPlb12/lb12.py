from abc import ABC, abstractmethod

class PowerSource(ABC):
    def __init__(self, name: str, efficiency: float):
        self.name = name
        self.efficiency = efficiency
    @abstractmethod
    def calculate_power(self, weather_conditions: dict) -> float:#створюэмо абстракний метод
        pass
    def __str__(self):
        return f"Електростанція '{self.name}' (ККД: {self.efficiency*100}%)"

class SolarPlant(PowerSource):
    def __init__(self, name: str, efficiency: float, area_m2: float):
        super().__init__(name, efficiency)
        self.area = area_m2
    def calculate_power(self, weather_conditions: dict) -> float:
        sun_intensity = weather_conditions.get('sun_intensity', 0)
        return self.area * sun_intensity * self.efficiency

class WindTurbine(PowerSource):
    def __init__(self, name: str, efficiency: float, blade_length_m: float):
        super().__init__(name, efficiency)
        self.blade_length = blade_length_m
    def calculate_power(self, weather_conditions: dict) -> float:
        wind_speed = weather_conditions.get('wind_speed', 0)
        if wind_speed < 2: return 0.0
        swept_area = 3.14159 * (self.blade_length ** 2)
        air_density = 1.225
        raw_power = 0.5 * air_density * swept_area * (wind_speed ** 3)
        return raw_power * self.efficiency

class HydroStation(PowerSource):
    def __init__(self, name: str, efficiency: float, water_height_m: float):
        super().__init__(name, efficiency)
        self.height = water_height_m
    def calculate_power(self, weather_conditions: dict) -> float:
        rain_level = weather_conditions.get('rain_level', 1.0)
        flow_rate = 50 * rain_level
        gravity = 9.81
        water_density = 1000
        return water_density * gravity * self.height * flow_rate * self.efficiency

class EnergyGrid:
    def __init__(self):
        self.sources = []
    def add_source(self, source: PowerSource):
        self.sources.append(source)
    def get_total_generation(self, weather: dict):
        print(f"\n--- ЗВІТ ГЕНЕРАЦІЇ (Погода: Сонце {weather['sun_intensity']} Вт/м2, Вітер {weather['wind_speed']} м/с) ---")
        total_watts = 0
        for source in self.sources:
            watts = source.calculate_power(weather)
            total_watts += watts
            print(f"{source.name:<20}: {watts/1000:.2f} кВт")
        print(f"{'-'*40}")
        print(f"ЗАГАЛОМ У МЕРЕЖІ   : {total_watts/1000:.2f} кВт")

if __name__ == "__main__":
    grid = EnergyGrid()
    grid.add_source(SolarPlant("Home Solar Roof", 0.18, 50))
    grid.add_source(WindTurbine("Big Wind Farm 1", 0.40, 20))
    grid.add_source(HydroStation("Dnipro Mini-Hydro", 0.90, 15))
    weather_sunny = {'sun_intensity': 1000, 'wind_speed': 1.0, 'rain_level': 0.8}
    grid.get_total_generation(weather_sunny)
    weather_stormy = {'sun_intensity': 50, 'wind_speed': 15.0, 'rain_level': 2.5}
    grid.get_total_generation(weather_stormy)