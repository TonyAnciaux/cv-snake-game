from PIL import Image
image = Image.open("becode_logo.png")
image = image.resize((50, 50), Image.ANTIALIAS)
image.save(fp="becode_logo_50.png")
