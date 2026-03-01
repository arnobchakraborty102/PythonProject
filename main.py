from PIL import Image
from rembg import remove

imgFile = Image.open("img.jpg")
output = remove(imgFile)
output.save("img_trnss.png")



































