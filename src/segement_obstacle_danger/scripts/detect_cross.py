from math import sqrt

# if 2 lines are not been cross, this returns None
# else this returns a cross point
def line_cross_point(p0, p1, q0, q1):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = q0
    x3, y3 = q1
    a0 = x1 - x0
    b0 = y1 - y0
    a2 = x3 - x2
    b2 = y3 - y2

    d = a0 * b2 - a2 * b0
    if d == 0:
        return None

    sn = b2 * (x2 - x0) - a2 * (y2 - y0)
    return (x0 + a0 * sn / d, y0 + b0 * sn / d)


def intersection(p0, p1, r, cx=0, cy=0):
    x0, y0 = p0
    x1, y1 =p1

    xd = x1 - x0
    yd = y1 - y0
    x = x0 - cx
    y = y0 - cy
    a = xd**2 + yd**2
    b = xd * x + yd * y
    c = x**2 + y**2 - r**2

    f0 = c
    f1 = a + 2 * b + c
    if (f0 >= 0 and f1 <= 0) or (f0 <= 0 and f1 >= 0):
        return True
    return -a <= b <= 0 and b**2 - a*c >= 0 and (f0 >= 0 or f1 >= 0)


# if linear and circle are not been cross, this returns None
# else this returns 2 cross points
def circle_cross_points(p0, p1, r, cx=0, cy=0):
    if not intersection(p0, p1, r):
        None
    x0, y0 = p0
    x1, y1 = p1
    xd = x1 - x0
    yd = y1 - y0
    x = x0 - cx
    y = y0 - cy
    a = xd**2 + yd**2
    b = xd * x + yd * y
    c = x**2 + y**2 - r**2
    d = b**2 - a*c
    s1 = (-b + sqrt(d)) / a
    s2 = (-b - sqrt(d)) / a
    return ((x0 + xd * s1, y0 + yd * s1), (x0 + xd * s2, y0 + yd * s2))


def is_cross_linear(p0, p1, q0, q1):
    cross_point = line_cross_point(p0, p1, q0, q1)
    if cross_point is None:
        return False
    cross_x, cross_y = cross_point
    x0, y0 = p0
    x1, y1 = p1
    if x0 > x1:
        return cross_x > x1 and x0 > cross_x
    else:
        return cross_x < x1 and x0 < cross_x



def is_cross_circle(p0, p1, q0, q1):
    r = sqrt(p0[0]**p0[0] + p0[1]**p0[1])
    cross_points = circle_cross_points(q0, q1, r)
    if cross_points is None:
        return False
    ((cross0_x, cross0_y), (cross1_x, cross1_y)) = cross_points
    x0, y0 = q0
    x1, y1 = q1
    if x0 > x1:
        return cross0_x > x1 and x0 > cross0_x or cross1_x > x1 and x0 > cross1_x
    else:
        return cross0_x < x1 and x0 < cross0_x or cross1_x < x1 and x0 < cross1_x