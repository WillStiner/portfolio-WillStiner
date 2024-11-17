from rectangle import Rectangle

class Surface:
    def __init__(self, filename, x, y, h, w):
        self.rect = Rectangle(x, y, h, w)
        self.image = filename
        
    def getRect(self):
        """
        returns rectangle attribute in self.rect
        args: self
        return: rectangle attribute from self.rect
        """
        return self.rect
    
def main():
    surf = Surface("myimage.png", 6, 8, 10, 15)
    print(surf)
    