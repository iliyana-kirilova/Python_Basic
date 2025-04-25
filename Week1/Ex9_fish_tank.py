length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

aquarium_volume_liters = (length*width*height)/1000
neaded_water = aquarium_volume_liters - (aquarium_volume_liters*percentage/100)
print(neaded_water)