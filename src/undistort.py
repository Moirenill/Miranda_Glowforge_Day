import numpy as np
import matplotlib as mpl
import os

image_folder = ".\\fwdtracingimages"
corrected_folder = ".\\corrected_images"
image_list = os.listdir(image_folder)

barrel_string = "convert {filename} -distort Barrel \"{c1} {c2} {c3}\" {outputname}"
channel_string = "-channel B -evaluate set 0 +channel "
contrast_string = "-contrast "
gray_string = "-colorspace Gray "
potrace_string = "potrace -s \"{bitmapname}\""

coeffs = [ 6.0 * 10.0**-6, -3.2 * 10**-3, -1.57 * 10 **-1]

def correct_image(filename, outputname, coeffs):
    command = barrel_string.format(filename=filename, c1=coeffs[0], c2=coeffs[1], c3=coeffs[2], outputname=outputname)
    os.system(command)

def vectorize_image(filename, outputname):
    command = potrace_string.format(bitmapname=filename)
    print command
    os.system(command)



if __name__ == '__main__':
    for k in range(len(image_list)):
        image = image_list[k]
        filename = image_folder + "\\" + image
        bitmapname = corrected_folder + "\\Output_{k}.bmp".format(k=k)
        correct_image(filename, bitmapname, coeffs)
        vectorname = corrected_folder + "\\Output_{k}.svg".format(k=k)

        if k == 10:
            vectorize_image(bitmapname, vectorname)

    
        
