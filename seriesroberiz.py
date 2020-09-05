import glob
import os

cwd = os.getcwd()
for series_file in glob.glob("*.mp4") + glob.glob("*.mkv") + glob.glob("*.avi"):
    print(series_file)
    name = ""
    for word in series_file.replace("_", " ").split():
        if word.startswith("S0"):
            break
        else:
            name += word + " "
    path = cwd + '/' + name
    if not os.path.exists(path):
        os.mkdir(path)
    os.rename(cwd + '/' + series_file, path + '/' + series_file)


