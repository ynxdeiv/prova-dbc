##confere se a palavra é um anagrama

input_from_question = input()
def solution(input_from_question):

    new_list=input_from_question.split(',')

    return sorted(new_list[0])== sorted(new_list[1])