#!sur/bin/python

class animal(object):
    print "a new animal"

    def call(self,yell):
        self.yell = yell

class dog(animal):
    color = 'yellow'
    def setname(self,name):
        self.name = name
    def getname(self):
        return self.name

class cat(animal):
    color = "white"
    def setname(self,name):
        self,name = name

    def getname(self):
        return self.name

dog = dog()
print dog
dog.setname()
dog.getname()

cat = cat()
print cat
cat.setname()
cat.setname()
