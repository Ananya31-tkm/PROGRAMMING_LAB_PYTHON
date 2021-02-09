from Graphics.Circle import *
from Graphics.Rectangle import *
from Graphics.Graphics3D.Cuboid import *
from Graphics.Graphics3D.Sphere import *

print("CIRCLE")
r=int(input("Enter radius of circle:"))
print("AREA OF CIRCLE:",area(r))
print("AREA OF CIRCLE:",perimeter(r))

print("\nRECTANGLE")
l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
print("AREA OF RECTANGLE:",Rarea(l,b))
print("AREA OF RECTANGLE:",Rperimeter(l,b))

print("\nCUBOID")
l=int(input("Enter length:"))
w=int(input("Enter width:"))
h=int(input("Enter height:"))
print("AREA OF CUBOID:",CUarea(l,w,h))
print("AREA OF CUBOID:",CUperimeter(l,w,h))

print("\nSPHERE")
r=int(input("Enter radius of sphere:"))
print("AREA OF SPHERE:",Sarea(r))
print("AREA OF SPHERE:",Sperimeter(r))
