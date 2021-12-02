class Submariner: 
    def __init__(self):
        self.h_pos = 0
        self.deph = 0

    def move_forward(self,value):
        self.h_pos += value
        
    def move_backward(self,value):
        self.h_pos -= value
        
    def move_upward(self,value):
        self.deph -= value
        
    def move_downward(self,value):
        self.deph += value
        
    def get_position(self):
        return [self.h_pos, self.deph]
    
    def get_h_pos(self):
        return self.h_pos
    
    def get_v_pos(self):
        return self.deph