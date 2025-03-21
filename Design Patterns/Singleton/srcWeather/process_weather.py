import json
import datetime
from weather_data import weather_json

#загружаем JSON (конвертируем текст в объект Python)
try:
    weather_data = json.loads(weather_json)
except json.JSONDecodeError:
    print("Ой, что-то не так с JSON. Проверь формат данных!")
    exit()

lon = weather_data["coord"]["lon"]  #долгота
lat = weather_data["coord"]["lat"]  #широта
weather_description = weather_data["weather"][0]["description"]  #описание погоды
temperature_kelvin = weather_data["main"]["temp"]  #температура в Кельвинах
wind_speed = weather_data["wind"]["speed"]  #скорость ветра
sunrise_timestamp = weather_data["sys"]["sunrise"]  #время восхода (UNIX)
sunset_timestamp = weather_data["sys"]["sunset"]  #время заката (UNIX)

#температуру в привычных градусах цельсия
temperature_celsius = round(temperature_kelvin - 273.15, 2)

#время восхода и заката более понятней для человека
sunrise_time = datetime.datetime.fromtimestamp(sunrise_timestamp).strftime("%I:%M %p")
sunset_time = datetime.datetime.fromtimestamp(sunset_timestamp).strftime("%I:%M %p")

            #сколько длится световой день
daylight_duration = sunset_timestamp - sunrise_timestamp
hours = daylight_duration // 3600  #часы
minutes = (daylight_duration % 3600) // 60  #минуты

#словарь с обработанными данными
processed_data = {
    "Местоположение": f"{lon}°E, {lat}°N",
    "Погода": weather_description.capitalize(),  # заглавная буква 
    "Температура": f"{temperature_celsius}°C",
    "Скорость ветра": f"{wind_speed} м/с",
    "Восход": sunrise_time,
    "Закат": sunset_time,
    "Длительность светового дня": f"{hours} часов {minutes} минут"
}

#записываем данные в JSON-файл
try:
    with open("src/processed_weather_data.json", "w") as file:
        json.dump(processed_data, file, indent=4)
except IOError:
    print("Ой, не могу сохранить данные в файл. Проверь права доступа!")
    exit()

print("\nОбработанные данные о погоде:")
for key, value in processed_data.items():
    print(f"{key}: {value}")
