from weather import *

myfile = "weather.dat"

mychoice = 0

while(True):
    print("          *** TUFFY TITAN WEATHER LOGGER MAIN MENU")
    print()
    print("1. Set data filename")
    print("2. Add weather data")
    print("3. Print daily report")
    print("4. Print historical report")
    print("9. Exit the program")

    mychoice = int(input("Enter menu choice:"))
    print()

    if mychoice == 1:
        myfile = input("Enter Data Filename:" )
        weather = read_data(myfile)

    elif mychoice == 2:
        dt = input("Enter date:")
        tm = input("Enter time:")
        t = int(input("Enter the Temperature:"))
        h = int(input("Enter the Humidity:"))
        r = float(input("Enter the Rainfall:"))

        weather[dt+tm] = {'t' :t, 'h' :h, 'r' :r}
        write_data(weather, myfile)

    elif mychoice == 3:
        dt = input("Enter date:")
        print(report_daily(weather, dt))

    elif mychoice == 4:
        print(report_historical(read_data(myfile)))

    elif mychoice == 9:
        break
