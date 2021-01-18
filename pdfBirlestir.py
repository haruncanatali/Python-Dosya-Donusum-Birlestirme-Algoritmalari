#!/usr/bin/env python
# coding: utf-8

# In[3]:


#pip install PyPDF2
from PyPDF2 import PdfFileMerger, PdfFileReader

kacAdetPdfBirlestirilecek = 12 # kaç adet pdf birleştirilecekse sayısını burada belirtin

mergedObject = PdfFileMerger()
 
for fileNumber in range(1,(kacAdetPdfBirlestirilecek+1)):
    mergedObject.append(PdfFileReader("pdfSunumlarınınOlduğuKlasor\\{0}".format(str(fileNumber))+ ".pdf", "rb"))
mergedObject.write("birlestirilenSunumlarınKaydedilecegiKlasor\\birlestirilmis.pdf")


# In[ ]:




