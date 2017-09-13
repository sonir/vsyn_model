from sonilab import timed_interpolation
class Shape:
    """ Shape Class """

    def __init__(self, type, name):

        """
        To instanciate, you should set two argments.
        The one is type. Type means the shape type. It is also used as address for OSC Message.
        The types are /circle, /triangle, /square, /rect, /line, /arc, /wave etc.

        The second is name. It is unique name for each shape object.
        However, the uniquness of the name must be proofed by user.
        """

        self.uid = 0
        self.type = type
        self.name = name
        self.active = 0
        self._x1 = timed_interpolation.TimedInterpolation()
        self._x1.set(0.5, 0.0)
        self._y1 = timed_interpolation.TimedInterpolation()
        self._y1.set(0.5, 0.0)
        self._x2 = timed_interpolation.TimedInterpolation()
        self._x2.set(0.5, 0.0)
        self._y2 = timed_interpolation.TimedInterpolation()
        self._y2.set(0.5, 0.0)

        self._size = timed_interpolation.TimedInterpolation()
        self._size.set(0.137, 0.0)
        self._height = timed_interpolation.TimedInterpolation()
        self._height.set(0.137, 0.0)
        self._angle = timed_interpolation.TimedInterpolation()
        self._angle.set(0.137, 0.0)
        self._freq = timed_interpolation.TimedInterpolation()
        self._freq.set(0.137, 0.0)
        self._amp = timed_interpolation.TimedInterpolation()
        self._amp.set(0.137, 0.0)
        self._phase = timed_interpolation.TimedInterpolation()
        self._phase.set(0.137, 0.0)
        self._thick = timed_interpolation.TimedInterpolation()
        self._thick.set(0.137, 0.0)
        self.fill = 1


    def get_primitive(self):
        if self.type == "/circle" :
            params = [self._x1.update(), self._y1.update(), self._size.update(), self.fill]
        elif self.type == "/triangle" :
            params = [self._x1.update(), self._y1.update(), self._size.update(), self._angle.update(), self.fill]
        elif self.type == "/square" :
            params = [self._x1.update(), self._y1.update(), self._size.update(), self._angle.update(), self.fill]
        elif self.type == "/rect" :
            params = [self._x1.update(), self._y1.update(), self._x2.update(), self._y2.update(), self._angle.update(), self.fill]
        elif self.type == "/line" :
            params = [self._x1.update(), self._y1.update(), self._x2.update(), self._y2.update(), self._thick.update()]
        elif self.type == "/arc" :
            params = [self._x1.update(), self._y1.update(), self._x2.update(), self._y2.update(), self._height.update()]
        elif self.type == "/wave" :
            params = [self._x1.update(), self._y1.update(), self._x2.update(), self._y2.update(), self._freq.update(), self._amp.update(), self._phase.update(), self._thick.update()]
        else:
            print "---- Shape.send() :: Unknown type was set !!"

        return (self.type, params)



    def get(self, variable):
        tmp = None
        #the variable is flg. return the value simply.
        if variable == "uid" or variable == "active" or variable == "fill" or variable == "name" or variable == "type" :
            src = "tmp = self." + variable
            exec(src)
            return tmp
        else:
            src = "tmp = self._" + variable + ".update()"
            exec(src)
            return tmp




    def set(self, variable, *args):

        if args:
            val = args[0]
            size = len(args)

            if variable == "uid" or variable == "active" or variable == "fill" :
                src = "self." + variable + "=" + str(val)
                exec(src)
                return
            elif variable == "name" or variable == "type" :
                # when the variable is array, then use ""
                src = "self." + variable + "=" + "\"" + str(val) + "\""
                exec(src)
                return


            if size == 2:
                # if the second argument was set, set it as duration
                duration = args[1]
            else:
                duration = 0.0

            # set interpolation
            src = "self._" + variable + ".set(" + str(val) + " , " + str(duration) + ")"
            exec(src)











