import math


def main():
    speed = float(input('Gib Geschwindigkeit des Raumschiffs in km/s ein:'))
    mass = float(input('Gib Masse des Planeten in Pentatonnen:'))
    radius =float(input('Gib Radius des Planeten in km:'))
    if speed <= 0 or mass <= 0 or radius <= 0:
        print('Falsche Eingaben')
        return
    ekg = math.sqrt(6.674 * (mass / radius))
    zkg = ekg * 1.414
    if speed < ekg:
        print('Raumschiff mit Planet kollidiert')
    if speed >= ekg and speed <= zkg:
        print('Raumschiff kreist um Planet')
    if speed > zkg:
        print('Nichts passiert')

while True:
    main()
    again = input('Neue Berechnung? j/n:')
    if again.lower() == 'n':
        print('Bye...')
        break