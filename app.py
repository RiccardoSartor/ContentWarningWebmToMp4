import fileManager
import converter

for file in fileManager.webmFiles(fileManager.currentPath()):
    replaced = file.replace('webm', 'mp4')
    converter.convert_webm_to_mp4(file, replaced)