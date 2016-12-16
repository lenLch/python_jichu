#!/urs/bin/python


class Bird1(object):
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print "Aaaah"
            self.hungry = False
        else:
            print "NO Thankes"
class Bird2(object):
    def __init__(self):
        self.call = "gugugu"

    def tall(self):
        print self.call
class SongBird(Bird1,Bird2):
    def __init__(self):
        super(SongBird,self).__init__()

    def eat(self):
        print "SongBird eat"
    def tall(self):
        print "SongBird talk"

niao = SongBird()
niao.eat()
niao.tall()

super(SongBird,niao).eat()
super(SongBird,niao).tall()
