

class Student(object):
    def __init__(self):
        pass

    def getScore(self):
        return self.__score

    def setScore(self,value):
        if value < 0 or value > 100:
            raise ValueError("score must between 0----100")
        self.__score = value

s = Student()

s.setScore(99)

print s.getScore()
