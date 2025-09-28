#script that converts temperatures between Celcius and Fahrenheit, using global variables to store conversion factors.

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5 + 32

temperature = int(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

def convert_to_celsius(fahrenheit):
    converted_temp = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {converted_temp}°C")

def convert_to_fahrenheit(celcius):
    converted_temp = celcius * CELSIUS_TO_FAHRENHEIT_FACTOR
    print(f"{celcius}°C is {converted_temp}°F")

if unit == 'C':
    fahrenheit = temperature
    convert_to_celsius(fahrenheit)
elif unit == 'F':
    celcius = temperature
    convert_to_fahrenheit(celcius)
