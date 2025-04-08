input_from_question = '3,6,9,15'



new_list= input_from_question.split(",")
int_list=[]
max_dif = 0
for _ in new_list:
    int_list.append(int(_))
sorted_list = sorted(int_list)
if len(int_list)>2:      
    for i in range (len(int_list)-1):
        sub = int_list[i] - int_list[i+1]
        if sub <0:
            sub = sub*-1
        
        if sub >max_dif:
            max_dif=sub
print(max_dif)
    

