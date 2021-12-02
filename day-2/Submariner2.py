class Submariner: 
    def __init__(self):
        self.h_pos = 0
        self.v_pos = 0

    def move_forward(self,value):
        self.h_pos += value
        
    def move_backward(self,value):
        self.h_pos -= value
        
    def move_upward(self,value):
        self.v_pos -= value
        
    def move_downward(self,value):
        self.v_pos += value
        
    def get_position(self):
        return [self.h_pos, self.v_pos]
    
    def get_h_pos(self):
        return self.h_pos
    
    def get_v_pos(self):
        return self.v_pos