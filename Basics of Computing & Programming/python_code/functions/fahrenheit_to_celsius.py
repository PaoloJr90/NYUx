def main():
    print("Please enter a temperature in Fahrenheit:")
    fahr = float(input())
    cel = fahrenheit_to_celsius(fahr)
    print(fahr, "Fahrenheit is", cel, "Celsius")

def fahrenheit_to_celsius(F):
    C = (F-32) * 5/9
    #print(F, "Fahrenheit is", C, "Celsius")
    return C

main()
