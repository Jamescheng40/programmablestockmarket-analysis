# import xml.etree.ElementTree as ET
# import xml.etree as etree

# root = ET.parse('wealthsimplestocklist.txt').getroot()

# print(root.tag)



# for hi in root:
#     #print(hi.tag)
#     if hi.tag == 'Retails':
#         a = ET.Element(root)
#         print(a)
#         for i in hi:
#             b = ET.SubElement(a,i)
#             c = ET.SubElement(b,"Average Volume")
#             print(b)
#             pass
			

# ET.dump(a)

	# if(hi.tag == "Sports"):
	# 	for i in hi:
	# 		if(i == "GME"):
	# 			print(i)


from lxml import etree



tree = etree.parse("test.txt")

root = tree.getroot()


for hi in root:
    #root.append( etree.Element("child1") )
    if hi.tag == "Utilities":
        for xyz in hi:
            if xyz.find("test12345").text is None:
                print("caonima")
            # tmp = etree.SubElement(xyz, "test12345")
            # tmp.text = "caonima"
            #print(xyz)
    

# etree.SubElement(root,'jamescheng')


with open("test.txt", 'wb') as doc:
   doc.write(etree.tostring(root, pretty_print = True))

