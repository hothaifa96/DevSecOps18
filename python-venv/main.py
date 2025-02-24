from PIL import Image
im = Image.open("dog.jpg")

print(dir(im))

# while True:
#     i = input('press o to open the image :')
#     if i == 'o':
#         im.show()
