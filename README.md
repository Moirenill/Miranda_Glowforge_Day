# Miranda_Glowforge_Day
Linear algebra and vector graphics.  What could be finer?  

Miranda's Glowforge Day 2015-03-16

The first piece of code, import_test.py, started as what it says on the tin.  I used it to do a little basic linear algebra 

on the graph paper image to get a basic set of barrel coefficient parameters.  Those are included in the code, but I'll 

reproduce them here:

a = 6.0 * 10^-6
b = -3.2 * 10^-3
c = -1.57 * 10^-1

I let ImageMagick choose the 'd' coefficient on its own, and it seemed to work fine.  These coefficients are actually a 

slight overcorrection.  There's a small, but detectable pincushion distortion after the translation.  That's a result of my 

relatively crude measurements on the graph paper, and can be corrected with making more measurements.  

undistort.py will take all the files in the forwarded graphics and run both the barrel (un)distortion and convert them to 

BMP.  I started working on some contrast effects as well, but those are not finished.  That problem will either need some 

feedback from a human or a more sophisticated controller than I can write in a day.  

It also includes a basic call to potrace to turn the bitmaps into svg files.  The results are not consistent, mostly due to 

the lighting and contrast.  Again, this is something that a more sophisticated controller could deal with.

I didn't end up using either of the two wrappers I installed.  They're both out of date and neither did what I wanted them 

to do.  I gave up on them and just wrote my own calls using the os.system functionality.  

I had a good time with the problems.  It looks like there's a good deal of interesting math, both in the distortion and the 

svg pathing.  
