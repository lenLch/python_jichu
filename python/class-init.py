#!/urs/bin/python
class Person(object):
    age = 10

    def __init__(self,name,sex):
        self.name = (name,sex)

    def color(self,color):
        print"%s is %s,this is %s"%(self.name,color,self.sex)

Lilei = Person('Lilei','Man')
Hanmei = Person('Hanmei','Woman')

Lilei.color('biack')
Hanmei.color('yellow')
