import os
import mimetypes

filenames = os.listdir("D:\\1A\\Python lab\\2022-Fall-Network\\lab3\\files")

for filename in filenames:
    print(mimetypes.guess_type(filename)[0])
