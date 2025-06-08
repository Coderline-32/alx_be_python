


FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 


def convert_to_celsius(celsius):
    
    return (celsius -32) * FAHRENHEIT_TO_CELSIUS_FACTOR 

def convert_to_fahrenheit(farenheit):
    
    return farenheit  * CELSIUS_TO_FAHRENHEIT_FACTOR + 32


try: 
    current_temp = int(input("Enter your current temp: "))
    unit = input("Is it (celsius/farenheit): ").strip().lower()

    if unit == "celsius":
        result = convert_to_fahrenheit(current_temp)
        print(f"{current_temp} celsius is equal to {result:.2f} farenheit")

    elif unit == "farenheit":
        result = convert_to_celsius(current_temp)
        print(f"{current_temp} farenheit is equal to {result:.2f} celsius")
              
    else:
    
        print("Enter a valid unit")

except ValueError:
    print("You entered invalid value!")




