from pathlib import Path

p = Path(__file__).with_name('numbers.txt')
deph_file = open(p)
deph_flat_list = deph_file.readlines()

depth_array = []

for deep_indice in deph_flat_list:
    depth_array.append(int(deep_indice.rstrip('\n')))
    
"""
Premier excercise
"""

last_depth = None
nb_last_depth_dec = 0

for current_depth in depth_array:
    if (last_depth):
        if (last_depth < current_depth):
            nb_last_depth_dec +=1
    last_depth = current_depth
    
print (f"Reponse 1 : {nb_last_depth_dec}")
    
"""
Second excercise
"""
depht_sliding_window = []
depth_last_sum = 0
depth_increase_time = 0

for current_depth in depth_array:
    depht_sliding_window.append(current_depth)
    if (len(depht_sliding_window)==3):
        if(depth_last_sum):
            if(sum(depht_sliding_window) > depth_last_sum):
                depth_increase_time +=1
        depth_last_sum = sum(depht_sliding_window)
        depht_sliding_window.pop(0)
        
print (f"Reponse 2 : {depth_increase_time}")