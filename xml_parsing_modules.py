##  XML Parsing Modules
# xml.etree.ElementTree  -- Tree structure which is most natural representation of hierarchial data

#xml.dom.minidom -- used by Proficient with DOM (Document Object Module). DOM Applications often starts by 
# Parsing XML into DOM


import xml.etree.ElementTree as et 
mytree = et.parse('C:/Users/Vimala_Revanuru/Desktop/Sample-XML-Files.xml')

myroot = mytree.getroot()  # To get root 
print('****************{}*****************'.format(myroot.tag))
#print(myroot[0].attrib)

for x in myroot[0]:
    #print(x.tag,x.attrib)
    print('{} : {}'.format(x.tag , x.text))


for y in myroot.iter():
    #print('****************{}*****************'.format(y.tag))
    print('{} : {}'.format(y.tag , y.text))
    if y.tag == 'CD':
        pass
    else:
        continue
    #print(y.tag)
    


data = '''<CATALOG>
	<CD>
	<TITLE>dill diya galla</TITLE>
	<ARTIST>Arijit singh</ARTIST>
	<COUNTRY>India</COUNTRY>
	<COMPANY>tseries</COMPANY>
	<PRICE>10.90</PRICE>
	<YEAR>2018</YEAR>
	</CD>
    </CATALOG>
'''
myroot1 = et.fromstring(data)
#print(myroot1.tag)
#print(myroot1.attrib)
