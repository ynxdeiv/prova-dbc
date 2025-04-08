n = int(input())
input_from_question='2,3,5,2,52,5,2'
list = input_from_question.split(',')
k = int(input())
total =0
print(list)
for _ in range(n):
	if int(list[_]) == k:
		total+=1

	

print(total) 