
import re

with open("text.txt", encoding='utf-8') as file:
    in_string = file.read() # почему когда применяешь функцию len() здесь - содержимое файла не читается ???

massive = re.split("\n", in_string)

number_of_strings = len(massive)

list_count_len = []
list_count_words = []
for line in massive:
    list_count_len.append(len(line))
    words = line.split()
    list_count_words.append(len(words))

pointer = 0
print('Количество строк в файле:',number_of_strings)
for num in list_count_words:
    print('Строка',str(pointer+1)+':','число слов:',list_count_words[pointer],'число символов:',list_count_len[pointer])
    pointer += 1