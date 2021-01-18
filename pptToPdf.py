#!/usr/bin/env python
# coding: utf-8

# In[18]:


import win32com.client
import os
import comtypes.client

kacAdetDonusturulecek = 12 # kaç tane powerPoint dosyası birleştirilecekse buraya sayısını girin

def PPTtoPDF(formatType = 32):
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")

    for i in range(1,(kacAdetDonusturulecek+1)):
        in_file = "PowepointDosyalarınınBulunduğuKlasör\\{0}.pptx".format(str(i))
        out_file = "DönüştürülenDosyanınKaydedileceğiKlasör\\{0}.pdf".format(str(i))
        deck = powerpoint.Presentations.Open(in_file)
        deck.SaveAs(out_file, formatType) # formatType = 32 for ppt to pdf
        deck.Close()
    
    powerpoint.Quit()
PPTtoPDF()

