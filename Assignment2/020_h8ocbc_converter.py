#CATATAN: JALANKAN FILE DENGAN CARA => execute [ python 020_h8ocbc_converter.py ] di terminal direktori yang bersangkutan

def celciusToKelvinViceVersa(number, choose):
    '''untuk mengubah celcius ke kelvin dan sebaliknya'''
    if choose.upper() == "K":
        value = float(number + 273.15)
        return str(round(value, 2))
    else:
        value = float(number - 273.15)
        return str(round(value, 2))

def fahrenheitToKelvinViceVersa(number, choose):
    '''untuk mengubah fahrenheit ke kelvin dan sebaliknya'''
    if choose.upper() == "K":
        value = float((number - 32) * 5/9 + 273.15)
        return str(round(value, 2))
    else:
        value = float((number - 273.15) * 9/5 + 32)
        return str(round(value, 2))

def fahrenheitToCelciusViceVersa(number, choose):
    '''untuk mengubah fahrenheit ke celcius dan sebaliknya'''
    if choose.upper() == "C":
        value = float((number - 32) * 5/9)
        return str(round(value, 2))
    else:
        value = float((number * 9/5) + 32)
        return str(round(value, 2))

def temperatureConverter(be, af):
    '''Untuk mengonversi temperatur.
    :param be: initial temperatur | string
    :param af: suhu yang dituju C,K,F | string
    :return: print converted temperature'''
    try:
        numbers = int(be[:-1])
        tempKey = be[-1]
    except ValueError:
        err()
    else:
        if tempKey.upper() == "C":
            if af.upper() == "K":
                print("Celcius to Kelvin: " + celciusToKelvinViceVersa(numbers, af)+" K")
            elif af.upper() == "F":
                print("Celcius to Fahrenheit: " + fahrenheitToCelciusViceVersa(numbers, af) + " F")
            else:
                err()
        elif tempKey.upper() == "K":
            if af.upper() == "C":
                value = float(numbers - 273.15)
                print("Kelvin to Celcius: " + celciusToKelvinViceVersa(numbers, af)+" C")
            elif af.upper() == "F":
                print("Kelvin to Fahrenheit: " + fahrenheitToKelvinViceVersa(numbers, af) + " F")
            else:
                err()
        elif tempKey.upper() == "F":
            if af.upper() == "C":
                print("Fahrenheit to Celcius: " + fahrenheitToCelciusViceVersa(numbers, af)+" C")
            elif af.upper() == "K":
                print("Fahrenheit to Kelvin: " + fahrenheitToKelvinViceVersa(numbers, af) + " K")
            else:
                err()


def err():
    '''untuk menampilkan error message'''
    print("Input the correct format [ 100C || 100K || 100F ]\n(Should convert to another temperature)")

def printSpace():
    '''memberi jarak ketika looping menu converter'''
    for loop in range(2):
        print("")

pos = 0
while pos == 0:
    printSpace()
    inputStr = input("\nInput Temperature[ FORMAT: 100C || 100K || 100F or q(for exit)]: ")
    if inputStr != "q":
        toStr = input("\nConvert to [ C || K || F ]: ")
        temperatureConverter(inputStr, toStr)
    else:
        pos = 1
printSpace()
print("Thank you")
