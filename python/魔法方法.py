


class A(object):
    '''
    This is a test
    '''

    def __getatter__(self,name):
        print "You use getatter"

    def __setattr__(self,name,value):
        print "You use setattr"
        self.__dict__[name] = value
    pass
a = A()

print dir(a)

print a.__doc__
print a.__class__

a.x
a.x = 7

print a.x
print a.__dict__
