class Rhombus:
    def __init__(self, side_a, angle_b, angle_a):
        self.side_a = side_a
        self.angle_b = angle_b
        self.angle_a = angle_a
    
    def __setattr__(self, name, value):
        if name == 'side_a':
            if not (value > 0):
                print('side a value must be bigger than 0')
                value = 0
            super().__setattr__(name, value)
        elif name == 'angle_a':
            if hasattr(self, 'angle_b') and not (value == 180 - self.angle_b):
                print('angle b plus angle a must be 180')
                value = 180 - self.angle_b
            super().__setattr__(name, value)
        elif name == 'angle_b':
            if hasattr(self, 'angle_a') and not (value == 180 - self.angle_a):
                print('angle b plus angle a must be 180')
                value = 180 - self.angle_a
            super().__setattr__(name, value)


rhombus_instance = Rhombus(side_a=10, angle_b=90, angle_a=90)
