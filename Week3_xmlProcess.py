import xml.etree.ElementTree as ET
    #parses the xml into element form
tree = ET.parse(r'C:\Users\Jason\Using-Databases-with-Python\tracks\Library.xml')

root = tree.getroot()

# example
#  itlist = root.findall('.//dict')
# # for elem in itlist:
# >>     for item in elem:
#    print(item.text)
