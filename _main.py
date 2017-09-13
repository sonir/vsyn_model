# if you want to use this library from outside of sonilab folder, should import as follows,
# from sonilab import sl_metro, sl_osc_send, osc_receive, event
# enjoy !!

import random
from sonilab import sl_metro, sl_osc_send, osc_receive, event
import shapes, shape, send_all

metro = sl_metro.Metro(0.016)
metro2 = sl_metro.Metro(0.5)
sender = sl_osc_send.slOscSend("127.0.0.1" , 57137)
receiver = osc_receive.OscReceive(57138)

ball_posi_a = 0.1
ball_posi_b = 0.9
ball_speed = 0.5


def osc_received (vals):
    print "OSC RECEIVED :: arg[0] = " + str(vals[0]) + " | arg[1] = "  + str(vals[1])



def send(adr, vals):
    sender.send(adr, vals)

event.add("/test" , osc_received)
event.add("/send" , send)
receiver.setup("/foo")



def init():
    global ball_posi_a, ball_posi_b
    #Make Primitives
    node1 = shape.Shape("/circle" , "node1") #set shape_type tag and unique name
    node1.set("x1" , ball_posi_a)
    node1.set("y1" , 0.5)
    node1.set("size" , 0.005)
    node1.set("fill" , 0)
    shapes.add(node1.name , node1)

    node2 = shape.Shape("/circle" , "node2") #set shape_type tag and unique name
    node2.set("x1" , ball_posi_b)
    node2.set("y1" , 0.5)
    node2.set("size" , 0.005)
    node2.set("fill" , 0)
    shapes.add(node2.name , node2)

    ball = shape.Shape("/circle" , "ball") #set shape_type tag and unique name
    ball.set("x1" , ball_posi_a)
    ball.set("y1" , 0.5)
    ball.set("size" , 0.005)
    ball.set("fill" , 1)
    shapes.add(ball.name , ball)

    arc = shape.Shape("/arc" , "arc") #set shape_type tag and unique name
    arc.set("x1" , ball_posi_a)
    arc.set("y1" , 0.5)
    arc.set("x2" , ball_posi_b)
    arc.set("y2" , 0.5)
    arc.set("height", 0.3)
    shapes.add(arc.name , arc)

    wave = shape.Shape("/wave", "wave")
    wave.set("x1" , ball_posi_a)
    wave.set("y1" , 0.5)
    wave.set("x2" , ball_posi_b)
    wave.set("y2" , 0.5)
    wave.set("height", 0.3)
    wave.set("freq" , 4.0)
    shapes.add(wave.name , wave)



def get_primitive(name):
    tmp = shapes.get(name)
    return tmp[1] #<- shapes.get returns a tupple. It includes the shape_tag(same as osc_address) and the list of parameters.


def move_ball():
    print "move_ball"
    global ball_posi_a, ball_posi_b, ball_speed
    ball = shapes.get_adr("ball")
    arc = shapes.get_adr("arc")
    wave = shapes.get_adr("wave")
    ball_x = ball.get('x1')
    print ball_x
    if ball_x == ball_posi_a:
        print "A"
        ball.set("x1" , ball_posi_b, ball_speed)
        arc.set("height", 0.3, ball_speed)
        wave.set("freq", 7.0, ball_speed)
    elif ball_x == ball_posi_b:
        print "B"
        ball.set("x1" , ball_posi_a, ball_speed)
        arc.set("height", -0.3, ball_speed)
        wave.set("freq", 2.0, ball_speed)


def draw():
    dic = shapes.get_all()
    send_all.run(dic)



try :
    #INIT all objects
    init()
    prim = None

    #Start Loop
    while True:
        if metro.update():
            draw()
            if metro2.update(): #write code to execute every 1 sec
                prim = get_primitive("ball")
                print "x1 = " , prim[1] , " : y1 = " , prim[2]
                if random.randint(0,1) == 1:
                    move_ball() #move ball with 50 percent rate in each round


except KeyboardInterrupt :
    receiver.terminate()
