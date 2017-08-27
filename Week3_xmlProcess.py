import xml.etree.ElementTree as ET
    #parses the xml into element form
tree = ET.parse(r'C:\Users\Jason\Using-Databases-with-Python\tracks\Library.xml')

root = tree.getroot()
    # . - selects current node (plist) most useful at beginning path
    #/dict/dict//dict - then goes dict branch then next child then //
    # //dict selects all child elements 'dict' within that wrung of tree (ladder)
itlist = root.findall('./dict/dict//dict')
