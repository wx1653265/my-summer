class parent(object):
    def implicit(self):
        print"holle world"
class child (parent):
    pass
dad=parent()
son=child()
dad.implicit()
son.implicit()
