import re
import xml.etree.ElementTree as ET

path = 'C:\\Users\\Rostyk\\Documents\\python-projects\\PP\\a.txt'
file = open(path, 'r', encoding='utf-8')
read_words = []

read_file = file.readlines()
file.close()

for i in range(0, len(read_file)):
    read_file[i] = re.sub('[!?.,—\']', '', read_file[i])
    read_words.append(read_file[i].split())

for i in range(0, len(read_words)):
    for j in range(0, len(read_words[i])):
        read_words[i][j] = str(read_words[i][j]).lower().replace(",", "").replace(".", "").replace(";", "")

word_list = []
#забирає всі слова, які мають менше 3 букв
for i in range(0, len(read_words)):
    variable_list = []
    for j in range(0, len(read_words[i])):
        if len(read_words[i][j]) > 2:
            variable_list.append(read_words[i][j])
    word_list.append(variable_list)

ending_list = []
#додаєм закінчення
for i in range(0, len(word_list)):
    for j in range(0, len(word_list[i])):
        if word_list[i][j][len(word_list[i][j]) - 2] == '’':       #Якщо в нас апостоф, то ми записуєм ост 4 букви
            ending_list.append(word_list[i][j][(len(word_list[i][j]) - 4):])
        else:
            ending_list.append(word_list[i][j][(len(word_list[i][j]) - 3):])
#первіряєм чи закінчення унікальне (тру)
def new_ending (ending, uniq_ending):
    for i in range(0, len(uniq_ending)):
        if (ending == uniq_ending[i]):
            return False
    return True

ending_and_repetitions = []
uniq_ending = []
all_list =[]
# шукає кількість одинакових закінчень
for i in range(0, len(ending_list)):
    ending = ending_list[i]
    counter = 0
    if new_ending(ending, uniq_ending):
        uniq_ending.append(ending)
        for j in range(0, len(ending_list)):
            if ending == ending_list[j]:
                counter += 1
        list = [ending, counter]
        ending_and_repetitions.append(list)
#шукає слово з певним закінченням, його номер рядка і номер слова в рядку
for i in uniq_ending:
    words_with_edentical_endings = []
    for j in range(0, len(word_list)):    #індекс рядка
        for k in range(0, len(word_list[j])):   #індекс слова в рядку
            word_lineNumb_wordNumb = ()
            if word_list[j][k][len(word_list[j][k]) - 2] == '’':
                variable = word_list[j][k][(len(word_list[j][k]) - 4):]
            else:
                variable = word_list[j][k][(len(word_list[j][k]) - 3):]
            if i == variable:
                word_lineNumb_wordNumb = (word_list[j][k], j, k)
                words_with_edentical_endings.append(word_lineNumb_wordNumb)
    all_list.append(words_with_edentical_endings)

root = ET.Element("root")
endingEl = ET.SubElement(root, "ending")

for i in range(0, len(ending_and_repetitions)):
    ET.SubElement(endingEl, "ending", name = ending_and_repetitions[i][0]).text = 'Number of words ' + str(ending_and_repetitions[i][1])
    wordEl = ET.SubElement(endingEl, "Words")
    for j in range(0, len(all_list[i])):
        ET.SubElement(wordEl, "word", name = all_list[i][j][0]).text = 'line ' + str(all_list[i][j][1]+1) + '. position ' + str(all_list[i][j][2]+1)
tree = ET.ElementTree(root)
tree.write("c2.xml", encoding='utf-8')
