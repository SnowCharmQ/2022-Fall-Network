import os
import mimetypes

filenames = os.listdir("files")

for filename in filenames:
    print(mimetypes.guess_type(filename)[0])
