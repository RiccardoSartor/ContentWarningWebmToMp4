import os

def folderFiles(folder_path):
    files = []
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            files.append(file)
    return files

def currentPath():
    return os.getcwd()

def webmFiles(path):
    allFiles = folderFiles(path)
    webm = []
    for file in allFiles:
        if '.webm' in file:
            webm.append(file)
    return webm
