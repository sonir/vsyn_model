from sonilab import event
import send_all


def send (adr, params):
    print adr , " : " ,
    for elm in params :
        print elm ,
    print " /// "

event.add("/send" , send)


array = []
array.append( ("/test1",[1,'a']) )
array.append( ("/test2",[2,'b']) )
array.append( ("/test3",[3,'c']) )
send_all.run(array)





