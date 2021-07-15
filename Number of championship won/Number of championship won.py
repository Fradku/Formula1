fhand = open("f1_driverchampions.txt")

drivers = dict()
first_win = dict()
last_win = dict()
for lines in fhand:
    lines = lines.rstrip()
    lines = lines.lower()
    season = lines.split()
    if len(season)<2: continue
    else:
        drivers[season[2]] = drivers.get(season[2], 0) + 1

while True:
    askchecklist = input("Enter a driver's name:")
    askchecklist = askchecklist.replace('_', ' ')
    askchecklist = askchecklist.title()
    ask = askchecklist.replace(' ', '_')
    ask = ask.lower()
    checklist = open('f1_driverlist.txt').read()
    if ask == 'quit':
        quit()

    elif askchecklist not in checklist and drivers:
        askchecklist = askchecklist.title()
        print(askchecklist, 'has never participated any F1 championship as driver\n')


    elif ask in drivers and askchecklist in checklist:
        ask = askchecklist.replace(' ', '_')
        ask = ask.lower()
        print(askchecklist, 'has won a total of', drivers.get(ask), 'championships\n')

    else:
        askchecklist = askchecklist.title()
        print(askchecklist, 'has never won any F1 championship\n')


