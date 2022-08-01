import eel
import os

eel.init('web', allowed_extensions=['.js', '.html','.css'])

directory = __file__
print(directory)
directory = directory[:-7]+"web\images" #получаем путь к папке с фотками
name_file = os.listdir(directory) #путь к папке
#for i in name_file:
	#eel.photo_name(i)  # передаем js'у название файла

print(name_file[1])
eel.photo_name(name_file[1]) #передаем js'у название файла

eel.start('html/index.html')