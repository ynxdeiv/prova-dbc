## entra 6 valores onde os 3 primeiros representa o salario e os 3 ultimos os gastos respectivamente, o objetivo é subtrair e ver quem economizou mais.

input_from_question = '300,250,150,50,40,30'

new_list= input_from_question.split(",")

max_economia = 0 

salario = new_list[:3]
gastos = new_list[3:]

for _ in range(3):

    economia = int(salario[_])- int(gastos[_])

    if economia >max_economia:
        max_economia = economia
