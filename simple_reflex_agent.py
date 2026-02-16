def thermostat(temperature):
    if temperature < 20:
        return "Heater ON"
    else:
        return "Heater OFF"

temp = float(input("Enter temperature: "))
result = thermostat(temp)
print(result)