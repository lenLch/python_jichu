


class Person(object):
    def __init__(self):
        self.height = 160

    def about(self,name):
        print('{} is about {}'.format(name,self.height))

class Girl(Person):
    def __init__(self):
        super(Girl,self).__init__()
        self.breast = 90
    def about(self,name):
        print('{} is about {},her is {}'.format(name,self.height,self.breast))
        super(Girl,self).about(name)

Chan = Girl()
Chan.about("DiaoChan")
super(Girl,Chan).about("xishi")
