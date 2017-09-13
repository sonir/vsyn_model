import time
import shapes, shape

circle1 = shape.Shape("/circle" , "circle1")
rect1 = shape.Shape("/rect" , "rect1")

shapes.add(circle1.name, circle1)
shapes.add(rect1.name, rect1)
shapes.print_all()

#Check set UID
tupple_adr_and_params1 = shapes.get_primitive(circle1.name)
tupple_adr_and_params2 = shapes.get_primitive(rect1.name)
assert tupple_adr_and_params1[1][0] == 0
assert tupple_adr_and_params2[1][0] == 1


#check get_all
all_obj = shapes.get_all()
for elm in all_obj:
    obj = elm[1]
    print elm[0], ":" , obj[0], "," , obj[1], "," , obj[2], "," , obj[3]



#How to write and reat each shape
shapes.set("circle1" , "x1", 777.0) #You can set plural parameters with set method
circle1 = shapes.get("circle1") #You can each shape objects with get method
assert circle1.get("x1") == 777.0


#You can set param with time transition
shapes.set("circle1" , "x1", 700.0 , 2.0) #You can set plural parameters with set method
circle1._x1.print_params()

while circle1.get("x1") != 700.0:
    print circle1.get("x1") #print the transition
    time.sleep(0.1)


#You can see all objects and the parameters with print_all()
shapes.print_all()

print "OK"
