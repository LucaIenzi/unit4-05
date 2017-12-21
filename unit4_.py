# Created by: luca.ienzi
# Created on: nov 7 2017
# Created for: ICS3U
# calculates volume

PI = 3.14

def volume_of_cylander (hight,radius):
    ans = (2 * PI * radius ** 2 * hight)
    return (ans)
    
user_hight = input("plz input hight",)
user_radius = input("plz input radius",)
volume_ans = volume_of_cylander(user_hight,user_radius)
print(volume_ans)
