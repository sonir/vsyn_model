from sonilab import event

def run(array):
    for elm in array:
        adr = elm[0]
        params = elm[1]
        event.bang("/send" , adr, params)



