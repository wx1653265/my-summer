class organism(object):
    def __init__(self):
        self.live=True
        self.nocell=False
class animal(organism):
    def __init__(self):
        super(animal,self).__init__()
        self.moving=True
        self.nomouth=False
class dog(animal):
    #def __init__(self):
        super(dog,self).__init__()
        self.wangwang=True
        self.miaomiao=False
