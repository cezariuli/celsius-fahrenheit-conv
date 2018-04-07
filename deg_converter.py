#Python 3

def FahrenheittoCelsius(deg):
    x =  (deg - 32) * (5.0/9.0)
    return x

def CelsiustoFahrenheit(deg):
    x = deg * 1.8 + 32
    return x


print ("This is a degree convertion tool. Please select which conversion you want to do: \n")

print ("1. Fahrenheit -> Celsius\n")
print ("2. Celsius -> Fahrenheit\n")

print ("Enter a conversion option number: \n")
conversion = int(input())

if conversion > 2:
    print("Incorrect option number.\n")
else:
    degrees = int(input("\nEnter the number of degrees you want to convert: "))
    if conversion == 1:
        print (str(degrees) + " degrees Fahrenheit = " + str(FahrenheittoCelsius(degrees)) + " degrees Celsius\n")
    else:
        if conversion == 2:
            print (str(degrees) + " degrees Celsius = " + str(CelsiustoFahrenheit(degrees)) + " degrees Fahrenheit\n")

input("\n\nPress enter to finish the program.")
