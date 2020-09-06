
from PIL import Image,ImageDraw
txt=input()
img=Image.new("RGB",(200,50),color=(20,100,137))
d=ImageDraw.Draw(img)
d.text((10,10),txt,fill=(255,255,255))
img.save("pic.jpg")
