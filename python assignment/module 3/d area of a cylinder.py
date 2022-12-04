ab=22/7
height = float(input('Height of cylinder: '))
radian = float(input('Radius of cylinder: '))
volume = ab * radian * radian * height
sur_area = ((2*ab*radian) * height) + ((ab*radian**2)*2)
print("Volume is: ", volume)
print("Surface Area is: ", sur_area)