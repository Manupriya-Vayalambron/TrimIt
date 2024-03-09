import pyshorteners
import pandas as pd
import pyperclip
link=input("enter the link:")
shortner=pyshorteners.Shortener()
x=shortner.tinyurl.short(link)
print(x)
pyperclip.copy(x)

