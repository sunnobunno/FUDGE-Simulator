import xml.etree.ElementTree

#Method to append items in an XML element to a list
def AppendXMLToList(xmlroot, elementchoice, list):
	for child in xmlroot.iter(elementchoice):
		i = 0
		for elements in child:
			list.append(child[i].text)
			i = i + 1

#Method to append items in an XML element to a dictionary
def AppendXMLToDict(xmlroot, elementchoice, dict):
	for child in xmlroot.iter(elementchoice):
		i = 0
		for elements in child:
			dict[str(child[i].tag)] = child[i].text
			i = i + 1

#Method to append a single item form an XML element to a single variable
#Obselete
def AppendXMLToItem(xmlroot, elementchoice, item):
	for child in xmlroot.iter('elementchoice'):
		item = child.text