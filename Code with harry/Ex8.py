# oh Soldier Prettify my folder
# path, dictionary file, format
# def soldier("C://", "harry.txt", "jpg")

import os


def soldier(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        file_list = f.read().split("\n")

    for file in files:
        if file not in file_list:
            os.rename(file, file.capitalize())

        if os.path .splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i += 1


soldier(r"C:\Users\jo\Downloads\video\Course\Python Course with CwH\LOL",
        r"C:\Users\jo\PycharmProjects\test1\Code with harry\ext.txt", ".png")
