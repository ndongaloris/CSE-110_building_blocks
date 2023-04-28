def wind_chill(temperature):
    wind_chill = (
        35.74
        + 0.6215 * temperature
        - 35.75 * wind_speed**0.16
        + 0.4275 * temperature * (wind_speed**0.16)
    )
    return wind_chill


def celsius(temperature):
    temp = (temperature * 9 / 5) + 32
    return temp


def kelvin(temperature):
    temp = (temperature - 273.15) * 9 / 5 + 32
    return temp


while True:
    print()
    try:
        temperature = float(input("What is the temperature?: "))
        type = input("Kelvin, Fahrenheit or Celsius (K/F/C)?: ").lower()
        if type == "f":
            for wind_speed in range(5, 61, 5):
                chill = wind_chill(temperature)
                print(
                    f"At temperature {temperature}F, and wind speed {wind_speed}mph, the windchill is: {chill:.2f}F"
                )
        elif type == "c":
            celsius(temperature)
            temperature = celsius(temperature)
            for wind_speed in range(5, 61, 5):
                chill = wind_chill(temperature)
                print(
                    f"At temperature {temperature}F, and wind speed {wind_speed}mph, the windchill is: {chill:.2f}F"
                )
        elif type == "k":
            kelvin(temperature)
            temperature = kelvin(temperature)
            for wind_speed in range(5, 61, 5):
                chill = wind_chill(temperature)
                print(
                    f"At temperature {temperature}F, and wind speed {wind_speed}mph, the windchill is: {chill:.2f}F"
                )
        else:
            print(
                f"{type} is not among your choice, please choose those that are available to you."
            )
            continue
    except ValueError:
        print("Invalid input, please try again")
        continue
    break
