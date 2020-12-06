class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
    def area(self):
        return self._length*self._width
class MassCount(Road):
    def __init__(self,_length,_width,weight,thickness ):
        super().__init__(_length, _width)
        self.weight = weight
        self.thickness = thickness
r = MassCount(25, 10000, 25, 5)
print(r.area())