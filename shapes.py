import threading
from sonilab import event
import shape

"""
Shapes treats array of shape.
"""

LOCK = threading.Lock()
data = {}
count = 0

def add(name, obj):
    global LOCK , count
    with LOCK:
        data[name]=(count , obj)
        count += 1



def get(name):
    tuple_uid_and_obj = data[name]
    uid = tuple_uid_and_obj[0]
    obj = tuple_uid_and_obj[1]

    tuple_address_and_params = obj.get_primitive()
    adr = tuple_address_and_params[0]
    params = tuple_address_and_params[1]
    params.insert(0, uid)
    return (adr,params)



def get_all():
    container = []
    for elm in data:
        tmp = data[elm]
        container.append( get(tmp[1].name) )
    return container



def get_adr(name):
    tuple_uid_and_obj = data[name]
    return tuple_uid_and_obj[1]



def set(name, variable, *args):
    if args:
        tuple_uid_and_obj = data[name]
        obj = tuple_uid_and_obj[1]
        obj.set(variable, *args)



def print_all():
    print "--- [shapes : print_all() ] ---"
    for elm in data:
        tmp = data[elm]
        obj = tmp[1]
        tmp = obj.get_primitive()
        params = tmp[1]
        print elm , obj
        for param in params:
            print param ,

        print "\n--"

    print "--- [print_all() : end] ---"



