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

bit_analysed_pos = 0
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
