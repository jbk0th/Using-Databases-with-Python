import xmltodict
#
# import xml.etree.ElementTree as ET
#     #parses the xml into element form
# tree = ET.parse(r'C:\Users\Jason\Using-Databases-with-Python\tracks\Library.xml')
#
# root = tree.getroot()
# itlist = root.findall('.plist/dict/dict')
# for elem in itlist:
#     elem[4].text()


# might be easier if could find all text with the fields that are interested in with the xml tree
#track title, rating, len, album, artist, Genre
with open('tracks\\Library.xml') as fd:
    doc = xmltodict.parse(fd.read())
artist = list() # -------
genre = list() # ------
album = list() # ------
track_title = list() # ------
length = list() # -----
rating = list()
count = list() # -----
#maybe a dict of lists would be best?
for song in doc['plist']['dict']['dict']['dict']:
    track_title.append(song['string'][0])
    artist.append(song['string'][1])
    album.append(song['string'][3])
    genre.append(song['string'][4])
    length.append(song['integer'][2])
    count.append(song['integer'][10])
    rating.append(song['integer'][13])
