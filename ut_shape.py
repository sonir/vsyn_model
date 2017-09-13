import shape
from sonilab import sl_metro

metro = sl_metro.Metro(1.0)


shape.Shape.__doc__
obj = shape.Shape("/circle" , "foo")

# obj.type = "SQUARE"
obj.active = True
obj.set("x1" , 0.1)
obj.set("y1" , 0.2)
obj.set("y1" , 0.2)
obj.set("x2" , 0.3)
obj.set("y2" , 4.0)

obj.set("size" , 0.131)
obj.set("height" , 0.132)
obj.set("angle" , 0.133)
obj.set("freq" , 0.134)
obj.set("amp" , 0.135)
obj.set("phase" , 0.136)
obj.set("thick" , 0.139)
obj.fill = False


#check all parameters with get method
assert obj.get("type") == "/circle"
assert obj.get("name") == "foo"
assert obj.get("active") == 1
assert obj.get("x1") == 0.1
assert obj.get("y1") == 0.2
assert obj.get("x2") == 0.3
assert obj.get("y2") == 4.0

assert obj.get("size") == 0.131
assert obj.get("height") == 0.132
assert obj.get("angle") == 0.133
assert obj.get("freq") == 0.134
assert obj.get("amp") == 0.135
assert obj.get("phase") == 0.136
assert obj.get("thick") == 0.139
assert obj.get("fill") == 0


#Test parameter managements
obj.set("type" , "/circle") #Test set parameter with set method
rt = obj.get_primitive()
assert rt[0] == "/circle"
params = rt[1]
assert params[0] == 0.1
assert params[1] == 0.2
assert params[2] == 0.131
assert params[3] == 0

#Triangle Test
obj.set("type" , "/triangle")
rt = obj.get_primitive()
assert rt[0] == "/triangle"
params = rt[1]
assert params[0] == 0.1
assert params[1] == 0.2
assert params[2] == 0.131
assert params[3] == 0.133
assert params[4] == 0

#Square Test
obj.set("type" , "/square")
rt = obj.get_primitive()
assert rt[0] == "/square"
params = rt[1]
assert params[0] == 0.1
assert params[1] == 0.2
assert params[2] == 0.131
assert params[3] == 0.133
assert params[4] == 0

#Rect Test
obj.set("type" , "/rect")
rt = obj.get_primitive()
assert rt[0] == "/rect"
params = rt[1]
assert params[0] == 0.1
assert params[1] == 0.2
assert params[2] == 0.3
assert params[3] == 4.0
assert params[4] == 0.133
assert params[5] == 0

#Line Test
obj.set("type" , "/line")
rt = obj.get_primitive()
assert rt[0] == "/line"
params = rt[1]
assert params[0] == 0.1
assert params[1] == 0.2
assert params[2] == 0.3
assert params[3] == 4.0
assert params[4] == 0.139

#ARC Test
obj.set("type" , "/arc")
rt = obj.get_primitive()
assert rt[0] == "/arc"
params = rt[1]
assert params[0] == 0.1
assert params[1] == 0.2
assert params[2] == 0.3
assert params[3] == 4.0
assert params[4] == 0.132

#WAVE Test
obj.set("type" , "/wave")
rt = obj.get_primitive()
assert rt[0] == "/wave"
params = rt[1]
assert params[0] == 0.1
assert params[1] == 0.2
assert params[2] == 0.3
assert params[3] == 4.0
assert params[4] == 0.134
assert params[5] == 0.135
assert params[6] == 0.136
assert params[7] == 0.139


#TEST .set method with int
obj.set("uid" , 137)
assert obj.uid == 137
obj.set("active" , 138)
assert obj.active == 138
obj.set("fill" , 139)
assert obj.fill == 139

# TEST .set method with string
obj.set("type" , "str_test_for_type")
assert obj.type == "str_test_for_type"
obj.set("name" , "str_test_for_name")
assert obj.name == "str_test_for_name"

#restore the shape type
obj.set("type" , "/wave")
obj.set("x1" , 0.0)
print "Basically, you should use setter and getter methods."
print "ex obj.set(\"X1\", 2.0)\n"

#interpolation demo
print "If you set variables with second as second argment then the parameter thanged with interpolation."
print "ex. obj.set(\"x1\" , 10.0, 10.0) # <- means make x1 value change to 10.0 with 10.0 seconds"
obj.set("x1" , 10.0, 10.0)
while True:
    if metro.update():
        tmp = obj.get_primitive()
        params = tmp[1]
        print params[0]
        if params[0]==10.0:
            break

print "OK"
