import xml.etree.ElementTree as ET


root = ET.parse('wealthsimplestocklist.txt').getroot()

print(root.tag)

for hi in root:
    print(hi.tag)
    if hi.tag == 'Retails':
        for i in hi:
            print(i)
			





	# if(hi.tag == "Sports"):
	# 	for i in hi:
	# 		if(i == "GME"):
	# 			print(i)
