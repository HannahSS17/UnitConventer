class UnitConverter:

    conversions = {
        "mm": {"mm": 1, "cm": 0.1, "m": 0.001, "km": 10 ** -6},
        "cm": {"mm": 10, "cm": 1, "m": 1 / 100, "km": 1 / 100000},
        "m": {"mm": 1000, "cm": 100, "m": 1, "km": 1 / 1000},
        "km": {"mm": 100000, "cm": 10000, "m": 1000, "km": 1},

        "t": {"t": 1, "kg": 1000, "g": 1000000, "mg": 1000000000},
        "kg": {"t": 0.001, "kg": 1, "g": 1000, "mg": 1000000},
        "g": {"t": 10 ** -6, "kg": 0.001, "g": 1, "mg": 1000},
        "mg": {"t": 10 ** -9, "kg": 10 ** -6, "g": 0.001, "mg": 1},

        "km2": {"km2": 1, "m2": 1000000, "cm2": 10000000000, "mm2": 1000000000000},
        "m2": {"km2": 10 ** -6, "m2": 1, "cm2": 10000, "mm2": 1000000},
        "cm2": {"km2": 10 ** -6, "m2": 0.0001, "cm2": 1, "mm2": 100},
        "mm2": {"km2": 10 ** -12, "m2": 10 ** -6, "cm2": 0.01, "mm2": 1}
    }

    while True:

        try:
            u1 = input("Choose the unit you want to convert from? \n"
                       "The app supports: " + ", ".join(conversions.keys()) + " ")

            u2 = input("Choose the unit you want to convert to. \n"
                       "The app supports: " + ", ".join(conversions[u1].keys()) + " ")

            convert = conversions[u1][u2]

            r1 = input("Enter the value you want to convert: ")
            result = float(r1) * convert

            print("The result is: ", result)

            break

        except KeyError:
            response = "That is not a valid key."
            print(response)

