import xml.etree.ElementTree as ET
from xml.dom import minidom

root = ET.Element("root")
child = ET.SubElement(root, "text")
tree = ET.ElementTree(root)
count = {}
for w in open('a.txt', 'r', encoding='utf-8').read().split():
    if w in count:
        count[w] += 1
    else:
        count[w] = 1
for word, times in count.items():
    word = word.lower()
    word = word.replace(",", "")
    word = word.replace(".", "")
    word = word.replace(";", "")
    grand = ET.SubElement(child, "UniqueWord", word=word).text = str(times) + " times"
   # print ("\"%s\" was found %d times" % (word, times))
tree.write("c.xml", encoding='utf-8')
