from PIL import Image

path = "/home/kame/Desktop/"
filename = "00000767"
fileending = ".JPG"
foo = Image.open(path + filename + fileending)
foo = foo.resize((round(foo.size[0] / 5), round(foo.size[1] / 5)), Image.ANTIALIAS)
foo.save(path + filename + "_resized" + fileending, optimize=True, quality=95)
