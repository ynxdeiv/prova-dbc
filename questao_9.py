#TIP 1: start writing your answer from line 8

import sys #this lines imports sys library
input_from_question='ana,natalia,giovana,manoel,0' 

new_list = input_from_question.split(',')
last = int(new_list[-1])
print(new_list[last])

