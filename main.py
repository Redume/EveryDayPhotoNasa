import eel
import os

eel.init('src', allowed_extensions=['.js', '.html', '.css'])

directory = __file__

directory = directory[:-7] + "src\photo"
name_file = os.listdir(directory)
print(name_file)

for i in name_file:
	eel.photo_name(i) 


eel.photo_name(name_file[1])

eel.start('web/html/index.html')
