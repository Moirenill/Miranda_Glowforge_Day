import numpy as np
import matplotlib as mpl
import PythonMagick as pm

import os

image_folder = ".\\fwdtracingimages"
image_list = os.listdir(image_folder)

def find_radius(point):
    center = [640.0, 360.0]
    return ( (point[0]-center[0])**2.0 + (point[1]-center[1]) ** 2.0) ** 0.5

def get_matrix_line(p_1, p_2):
    r_1 = find_radius(p_1);
    r_2 = find_radius(p_2);
    return [ (r_2 ** 3.0 - r_1 ** 3.0), (r_2 ** 2.0 - r_1 ** 2.0), (r_2 - r_1), 0]

def get_single_line(point):
    r = find_radius(point)
    return [r**3, r**2, r, 1]

##for image_name in image_list:
##    image_path = image_folder + "\\" + image_name
##    image = pm.Image(image_path)
##    print image_name, image.fileName(), image.magick(), image.size().width(), image.size().height()

filename = image_folder + "\\" + image_list[0]
print filename


p_1 = [625.0, 360.0]
p_2 = [645.0, 360.0]
p_3 = [664.0, 360.0]
p_4 = [683.0, 360.0]
p_12 = [869.0, 360.0]
p_13 = [887.0, 360.0]
p_21 = [1015.0, 360.0]
p_22 = [1030.0, 360.0]

# U = (a * r^3 + b * r^2 + c * r + d ) * R + C
# or
# R_src = R * (a * r^3 + b * r^2 + c * r + d )

# We beging by using relative positions to set up our system of equations.
# That is, E_1 is given by the state equations for p_1 - p_2.  The difference
# in corrected distance between consecutive points should be the same, so we
# can isolate the coefficients without having the graph paper centered.


points = [ p_2, p_3, p_4, p_12, p_13, p_21, p_22]

A = np.matrix(np.zeros([len(points), 4]))

for k in range(len(points)):
    point = points[k]
    A[k, :] = get_single_line(point)

width = 20.0
gridmarks = [ 1, 2, 3, 11, 12, 20, 21]
b = np.zeros([len(gridmarks), 1])
for k in range(len(gridmarks)):
    b[k,0] = -15.0 + width * gridmarks[k]

print A.shape
print b.shape
print b

C = np.linalg.inv( np.transpose(A) * A ) * np.transpose(A)

x = C * b

print x
