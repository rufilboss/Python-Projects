#Import Module
from textblob import TextBolb

#Creating variable trans_text
trans_text = TextBolb("I love coding")

#Specify which lang you're translating to.
trans_text.translate(to = 'ar')