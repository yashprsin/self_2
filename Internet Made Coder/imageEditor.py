from PIL import Image, ImageEnhance, ImageFilter
import os

path = 'C:\\Users\\Yashp\\PycharmProjects\\pythonProject\\Internet Made Coder\\img'
pathOut = 'C:\\Users\Yashp\\PycharmProjects\\pythonProject\\Internet Made Coder\\editt'

for file in os.listdir(path):
    img1 = Image.open(f"{path}/{file}")
    edit = img1.filter(ImageFilter.SHARPEN)

    clean_name = os.path.splitext(file)[0]

    edit.save(f"{pathOut}/{clean_name}_edited.jpg")
