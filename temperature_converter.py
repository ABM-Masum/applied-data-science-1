# Temperature Converter with functions

# Your functions here!

def kelvin_to_celsius(temperature):
    temperature -= 273.15
    return temperature

def kelvin_to_fahrenheit(temperature):
    temperature  = (temperature - 273.15) * 9/5 + 32
    return temperature

if __name__ == "__main__":
    temperature = input("Temperature in Kelvin:")

    # if temperature.replace("-", "").replace(".", "").isdigit() and temperature.count(".") <= 1:
    #     temperature = float(temperature)
    if temperature.replace("-", "").isdigit():
        temperature = int(temperature)
        print(kelvin_to_celsius(temperature))
        print(kelvin_to_fahrenheit(temperature))
    else:
        print("Please input a digit.")
    pass