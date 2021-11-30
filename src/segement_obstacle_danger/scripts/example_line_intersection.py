import shapely
from shapely.geometry import LineString, Point
A = (0,0)
B = (0,3)
C = (-2,2)
D = (2,0)
line1 = LineString([A, B])
line2 = LineString([C, D])

int_pt = line1.intersection(line2)
print(int_pt)
#point_of_intersection = int_pt.x, int_pt.y

#print(point_of_intersection)


# def ccw(A,B,C):
#     return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

# # Return true if line segments AB and CD intersect
# def intersect(A,B,C,D):
#     return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)