import pyqrcode
import os, shutil

title=input("GIVE YOUR QR CODE TITLE")
text=input("WHAT WOULD YOU LIKE THE QR CODE TO SAY")

file_name_svg=title + ".svg"
file_name_png=title + ".png"
url=pyqrcode.create(text)
url.svg(file_name_svg, scale= 8)
url.png(file_name_png, scale=10)

os.mkdir(fr"C:\Users\91735\Desktop\{title}")
shutil.move(f"{file_name_png}",fr"C:\Users\91735\Desktop\{title}")
shutil.move(f"{file_name_svg}",fr"C:\Users\91735\Desktop\{title}")
