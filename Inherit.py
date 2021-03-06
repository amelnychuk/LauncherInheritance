import os

class DerivativeLauncher(object):

    """
    This class allows sub classes to instaniate their super class as a data store.

    """
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


class HoudiniLauncher(DerivativeLauncher):

    """
    Sub Launcher to lauch a specfic program
    """
    def __init__(self):

        DerivativeLauncher.__init__(self)
        self.setRelPath("houdini/hip")


class HoudiniDevLauncher(HoudiniLauncher):
    """
    Derivitive launcher to launch a program with specific properties and work on the data that the parent launcher provides
    """
    def __init__(self):
        HoudiniLauncher.__init__(self)
        self.setRelPath("dev/issue")
        print (self.getRelPath())
        print (self.getParent().getParent().getRelPath())



if __name__ == "__main__":
    L = HoudiniDevLauncher()