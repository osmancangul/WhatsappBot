#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pywhatkit as kit

try :
    kit.sendwhatmsg("+90 000 000 00 00","whatsapp bot uygulaması \U0001F607",16,39)
    print("Gönderme Başarılı")
except:
    print("Beklenmedik Hata :[")

# 16,39 saat göstergesi onu siz belirleyeceksiniz.

