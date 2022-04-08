#Write a program to create a parent class, 3DShapes, with methods printVolume() and printArea(),
#which prints the Volume and Area, respectively. Create classes Cylinder and Sphere by inheriting 3DShapes class. Using these child classes,
#calculate and print the volume and area of a cylinder and sphere.

class threeDShapes:
    def display_area(self):
        print("The area of the 3D shape is : ",self.area)
    def display_volume(self):
        print("The volume of the 3D shape is : ",self.volume)


#child class
class cylinder(threeDShapes):
    def __init__(self,r,h):
        self.radius=r
        self.height=h
    def calculate_area(self):
        self.area=2*3.14*self.radius*(self.radius+self.height)
    def calculate_volume(self):
        self.volume=3.14*self.radius*self.height


class sphere(threeDShapes):
    def __init__(self,r):
        self.radius=r
    def calculate_area(self):
        self.area=4*3.14*self.radius*self.radius
    def calculate_volume(self):
        self.volume=(4/3)*3.14*(self.radius**3)

cylinder_radius = int(input("Enter the radius of the cylinder : "))
cylinder_height = int(input("Enter the height of the cylinder : "))
cylinder_obj = cylinder(cylinder_radius,cylinder_height)
cylinder_obj.calculate_area()
cylinder_obj.display_area()
cylinder_obj.calculate_volume()
cylinder_obj.display_volume()        
sphere_radius = int(input("\nEnter the radius of the sphere : "))
sph_obj = sphere(sphere_radius)
sph_obj.calculate_area()
sph_obj.calculate_volume()
sph_obj.display_area()
sph_obj.display_volume()

    
