class Color:
    def __init__(self, hexcode):
        self._hexcode = hexcode
        self._update_rgb()
    
    def _update_rgb(self):
        self.r = int(self._hexcode[0:2], 16)
        self.g = int(self._hexcode[2:4], 16)
        self.b = int(self._hexcode[4:6], 16)
    
    @property
    def hexcode(self):
        return self._hexcode
    
    @hexcode.setter
    def hexcode(self, value):
        self._hexcode = value
        self._update_rgb()


color = Color('0000FF')
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)