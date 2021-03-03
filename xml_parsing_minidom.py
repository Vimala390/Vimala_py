from xml.dom.minidom import parse
import xml.dom.minidom as dm
mytree = dm.parse('C:/Users/Vimala_Revanuru/Desktop/movies.xml')
coll1 = mytree.documentElement
myroot = coll1.getAttribute("shelf")
#print(myroot)
movies = coll1.getElementsByTagName('movie')
types = coll1.getElementsByTagName('type')
#print(types)

for movie in movies:
    print("*****Movie*****")
    #print('************{}**********'.format(movie.getAttribute("movie")))
    #print(movie.getAttribute("title").text)
    if movie.hasAttribute("title"):
        print("Title: %s" %movie.getAttribute("title"))
        type = movie.getElementsByTagName('type')[0]
        print("Type: %s" % type.childNodes[0].data)
        format = movie.getElementsByTagName('format')[0]
        print ("Format: %s" % format.childNodes[0].data)
        rating = movie.getElementsByTagName('rating')[0]
        print ("Rating: %s" % rating.childNodes[0].data)
        description = movie.getElementsByTagName('description')[0]
        print ("Description: %s" % description.childNodes[0].data)
    

 
    