import os

class Launcher(object):
    def __init__(self):

        self.setRelPath("Projects/amelnychuk")
        self.instaniateSuperClass()

    def setRelPath(self, path):
        if not hasattr(self, "super"):
            self._relPath = path
        else:
            self._relPath = os.path.join(self.super.getRelPath(), path)
    def getRelPath(self):
        return self._relPath

    def instaniateSuperClass(self):
        self.super = self.__class__.__bases__[0]()

    def getParent(self):
        return self.super




class HoudiniLauncher(Launcher):
    def __init__(self):

        Launcher.__init__(self)
        self.setRelPath("houdini/hip")
        print ("Working")





class HoudiniDevLauncher(HoudiniLauncher):
    def __init__(self):
        HoudiniLauncher.__init__(self)
        self.setRelPath("dev/issue")
        print (self.getRelPath())
        print (self.getParent().getParent().getRelPath())



if __name__ == "__main__":
    L = HoudiniDevLauncher()