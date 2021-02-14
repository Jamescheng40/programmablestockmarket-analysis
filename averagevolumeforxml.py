import yfinance as yf
import pandas as pd
import math
from lxml import etree


tree = etree.parse("outputfixedv1.txt")
root = tree.getroot()



for hi in root:
    #root.append( etree.Element("child1") )
    for xyz in hi:
        if xyz.find("AveVol1MSin2008").text is None:
            msft = yf.Ticker(xyz.tag)
            data = msft.history(period="max",interval="1mo",start="2008-1-1")
            avg_count = 0
            avg_num = 0
            for i in range(data.shape[0]):
                x = float(data[i:i+1]["Volume"])
                if not(math.isnan(x)):
                    avg_num = avg_num + 1
                    avg_count = avg_count + x
            tmp = etree.SubElement(xyz, "AveVol1MSin2008")
            if(avg_num != 0):
                tmp.text = str(avg_count/avg_num)
    print("Session completed with " + str(hi.tag))


with open("outputfixedv2.txt", 'wb') as doc:
   doc.write(etree.tostring(root, pretty_print = True))