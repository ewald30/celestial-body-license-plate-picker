import string
from astropy.time import Time
from sunpy.coordinates import get_body_heliographic_stonyhurst
import random

''' Generates romanian license plates based on the location of the celestial bodies on a given observation date.'''

OBSERVATION_TIME = Time('2023-12-23T07:54:00.005')  # The time when coordinates of each celestial body was observed
COUNTY_CODE = 'SV'  # the code of the county you wish to register your car in
planet_list = ['earth', 'venus', 'mars', 'mercury', 'jupiter', 'neptune', 'uranus', 'sun']


planet_coord = [get_body_heliographic_stonyhurst(
    this_planet, time=OBSERVATION_TIME) for this_planet in planet_list]

licenses = []

for idx, coord in enumerate(planet_coord):
    lon, lat, radius = coord.lon.value, coord.lat.value, coord.radius.value

    letters = ''
    license_number = 0

    for value in [lon, lat, radius]:
        letter_index = int(abs(value)) % 26     # 26 letters in english alphabet
        license_number +=int(abs(value))
        letters += string.ascii_uppercase[letter_index]

    license_plate = f"{COUNTY_CODE} {license_number%100} {letters} -- {planet_list[idx]}"
    licenses.append(license_plate)

    print(f"Generated: {COUNTY_CODE} {license_number%100} {letters} -- Planet {planet_list[idx]} -- Coords: lon {lon}, lat {lat}, radius {radius}")

print(f"\n\n Your license plate: {random.choice(licenses)}")