
class Color(object):
    color = (0,0,0)

    @classmethod
    def value(cls):
        if cls.__name__ =='Red': # 类名.__name__==类名
            cls.color = (255,0,0)
        elif cls.__name__ =='Green':
            cls.color = (0,255,0)
        return cls.color

class Red(Color):
    pass
class Green(Color):
    pass
class UnknowColor(Color):
    pass

red = Red()
green = Green()
xcolor = UnknowColor()

print 'red = ',red.value()
print 'green = ',green.value()
print 'xcolor = ',xcolor.value()
