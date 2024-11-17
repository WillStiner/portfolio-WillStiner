class Rectangle:
    def __init__(self, x, y, height, width):
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(height)
        self.width = abs(width)
        
    def __str__(self):
        """
        returns x, y, width and height of the rectangle
        args: self
        return: (str) string containing x, y, width and height of rectangle
        """
        return "(x : {self.x}, y : {self.y}) width: {self.width}, height: {self.height}".format(self=self) #got help from https://realpython.com/lessons/how-and-when-use-str/
    
    
def main():
    rect = Rectangle(6, 8, 10, 15)
    print(rect)
    