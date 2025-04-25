x_house_height = float(input())
y_house_length = float(input())
h_roof_height = float(input())

wall_square = 2 * x_house_height * x_house_height - 2 * 1.2
wall_side = 2 * x_house_height * y_house_length - 2 * 1.5 * 1.5
total_area = wall_square + wall_side
green_paint = total_area / 3.4

roof_rect = 2 * x_house_height * y_house_length
roof_triangle = (x_house_height * h_roof_height / 2) * 2
total_area_roof = roof_rect + roof_triangle
red_paint = total_area_roof / 4.3

print('%.2f' % green_paint)
print('%.2f' % red_paint)
