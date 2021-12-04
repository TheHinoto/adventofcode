from os import system
from pathlib import Path

def convert_binnary_array_to_integer(binnary_array: list) -> int:
    binnary_array.reverse()
    decimal_value=0
    for i in range(len(binnary_array)):
        decimal_value += binnary_array[i]*(2**(i))
    return decimal_value
    
with open(Path(__file__).with_name('input.txt'),"r") as f:
    inputs = f.readlines()

diag_array = []
diag_bit_array = []

for el in inputs:
    el = el.rstrip('\n')
    for diag_bit in el:
        diag_bit_array.append(int(diag_bit))
    diag_array.append(diag_bit_array.copy())
    diag_bit_array.clear()

"""
Excercice One
"""   

bit_analysed_pos_maxvalue = len(diag_array[0])
diag_bit_array_size = len(diag_array)

count_bit_one = count_bit_zero = 0
gamma_rate = []
epsilon_rate = []

for i in range (bit_analysed_pos_maxvalue):
    for j in range(diag_bit_array_size):
        if(diag_array[j][i]):
            count_bit_one += 1
        else:
            count_bit_zero += 1
    if count_bit_one > count_bit_zero:
        gamma_rate.append(1)
        epsilon_rate.append(0)     
    else:
        gamma_rate.append(0)
        epsilon_rate.append(1)
        
    count_bit_one = count_bit_zero = 0

gamma_rate_decimal = convert_binnary_array_to_integer(gamma_rate)
epsilon_rate_decimal = convert_binnary_array_to_integer(epsilon_rate)

print(f"Gamma Rate : {gamma_rate_decimal}")
print(f"Epsilon Rate : {epsilon_rate_decimal}")
print(f"Power Consumtion : {gamma_rate_decimal*epsilon_rate_decimal}")



def pop_list_based_bit(liste: list, pos: int, valeur: int) -> list:
    for el in liste:
        if(el[pos]!=valeur):
            liste.remove(el)
            pop_list_based_bit(liste, pos, valeur)
    return liste
        
    
def find_oxgen_rating(diag_array: list) -> list:
    for column in range(len(diag_array[0])):
        most_common_value = count_bit_one = count_bit_zero = 0
        for line in range(len(list(diag_array))):
            
            if(diag_array[line][column]):
                count_bit_one +=1
            else:
                count_bit_zero +=1
                
        most_common_value = int(count_bit_one >= count_bit_zero)
            
        if(len(diag_array)>1):
            diag_array=pop_list_based_bit(diag_array,column,most_common_value)
        
    return diag_array   

def find_co2_scrubber_rating(diag_array: list) -> list:
    for column in range(len(diag_array[0])):
        less_common_value = most_common_value = count_bit_one = count_bit_zero = 0
        for line in range(len(list(diag_array))):
            
            if(diag_array[line][column]):
                count_bit_one +=1
            else:
                count_bit_zero +=1
                
        most_common_value = int(count_bit_one >= count_bit_zero)
        less_common_value = 1 - most_common_value
            
        if(len(diag_array)>1):
            diag_array=pop_list_based_bit(diag_array,column,less_common_value)
        
    return diag_array      
        
oxygen_rating=convert_binnary_array_to_integer(find_oxgen_rating(list(diag_array))[0])
co2_scrubbing=convert_binnary_array_to_integer(find_co2_scrubber_rating(list(diag_array))[0])
life_support_rating = oxygen_rating * co2_scrubbing

print (f"Life support rating : {life_support_rating}")

