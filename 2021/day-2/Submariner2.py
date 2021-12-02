class Submariner: 
    def __init__(self):
        self.h_pos = 0
        self.depth = 0
        self.aim = 0

    def move_forward(self,value):
        self.h_pos += value
        self.depth += (self.aim * value)
        
    def move_backward(self,value):
        self.h_pos -= value
        
    def move_upward(self,value):
        self.aim -= value
        
    def move_downward(self,value):
        self.aim += value
        
    def get_position(self):
        return [self.h_pos, self.depth]
    
    def get_h_pos(self):
        return self.h_pos
    
    def get_v_pos(self):
        return self.depth