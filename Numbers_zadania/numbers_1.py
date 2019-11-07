# calculate distance between 2 cities
# Kraków - 50°03′41″N 19°56′18″E
# Londyn - 51°30′N 0°07′W

from math import cos, atan2, sin, pi, sqrt

londyn_sz = [51, 30]
londyn_dl = [0, 7]
krakow_sz = [50, 3, 41]
krakow_dl = [19, 56, 18]
r_ziemi_km = 6371
mile = 0.621371192


def degrees_to_radians(angle_degrees):
    angle_radians = (angle_degrees*pi)/180
    return angle_radians


def caluclate_distance(jednostka):
    # zamiana na radiany
    lon_sz = degrees_to_radians(londyn_sz[0]+(londyn_sz[1]/60))
    lon_dl = degrees_to_radians(londyn_dl[0]+(londyn_dl[1]/60))
    krk_sz = degrees_to_radians(krakow_sz[0]+(krakow_sz[1]/60)+(krakow_sz[2]/(60**2)))
    krk_dl = degrees_to_radians(krakow_dl[0]+(krakow_dl[1]/60)+(krakow_dl[2]/(60**2)))

    # Haversine formula
    a = sin(abs(lon_sz-krk_sz)/2)**2+cos(lon_sz)*cos(krk_sz)*(sin(abs(lon_dl-krk_dl)/2)**2)
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    d = c * r_ziemi_km

    # wybor jednostki
    if jednostka == "km":
        return d
    elif jednostka == "m":
        return d * mile


print(caluclate_distance("km"))
