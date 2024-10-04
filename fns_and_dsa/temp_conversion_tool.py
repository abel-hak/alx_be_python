FAHRENHEIT_TO_CELSIUS_FACTOR  = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


temperature = float(input("Enter the temperature to convert: "))
temperature_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if type(temperature) is not float:
    print(""Invalid temperature. Please enter a numeric value."")
elif temperature_unit == 'C':
    print(f'{temperature}°C is {convert_to_fahrenheit(temperature)}°F')
elif temperature_unit == 'F':
    print(f'{temperature}°F is {convert_to_celsius(temperature)}°C')
else:
    print('Please enter valid temperature unit')
    
