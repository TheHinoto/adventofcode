from pathlib import Path

import Submariner1, Submariner2
    
if __name__ == "__main__":

    submariner1 = Submariner1.Submariner()
    submariner2 = Submariner2.Submariner()

    moove_file = open(Path(__file__).with_name('mooves.txt'))
    moove_list = moove_file.readlines()

    for instruction in moove_list:
        move = instruction.rstrip('\n')
        [direction, distance] = move.split(" ")
        distance = int(distance)
        
        if (direction == "up"):
            submariner1.move_upward(distance)
            submariner2.move_upward(distance)
        
        elif (direction == "down"):
            submariner1.move_downward(distance)
            submariner2.move_downward(distance)
            
        elif (direction == "forward"):
            submariner1.move_forward(distance)
            submariner2.move_forward(distance)
            
        
    print(f"Awnser 1 : {submariner1.get_h_pos()*submariner1.get_v_pos()}")
    print(f"Awnser 2 : {submariner2.get_h_pos()*submariner2.get_v_pos()}")
