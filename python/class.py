class Person(object):
    age = 10
    name = "Lilei"

    def color(self,color):
        self.language = 'English'
        print "%s is %s,This is %s"%(self.name,color,self.sex)

Lilei = Person()
Hanmei = Person()
Lilei.sex = 'Man'
Hanmei.sex = 'Woman'
Hanmei.name = 'Hanmei'
print Lilei.age
print Lilei.name
print Hanmei.age

Lilei.color('black')
print Lilei.language
Hanmei.color('yellow')
