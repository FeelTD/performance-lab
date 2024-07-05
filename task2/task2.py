import sys

def point(coord_x, coord_y, r, dot_x, dot_y):
    dist = ((coord_x-dot_x)**2+(coord_y-dot_y)**2)**(1/2)
    if (dist < r):
        return 1
    elif (dist == r):
        return 0
    else:
        return 2


file1_path = sys.argv[1]
file2_path = sys.argv[2]
file1 = open(file1_path, 'r')
file2 = open(file2_path, 'r')

coords = file1.readline()
coords_list = [int(x) for x in coords.split()]
r = int(file1.readline())


all_dots = []
for line in file2:
    dot = [int(x) for x in line.split()]
    all_dots.append(dot)

for dots in all_dots:
    print(point(coords_list[0], coords_list[1], r, dots[0], dots[1]))
