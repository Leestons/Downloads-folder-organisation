#! python3
# organise.py - Organises downloads folder.

import shutil, os
for filename in os.listdir():
	if filename.endswith('.zip'):
		shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\zip')
		#print(filename)
	if filename.endswith('.rar'):
		shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\zip')
		#print(filename)
	elif filename.endswith('.iso'):
		shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\iso')
		#print(filename)
	elif filename.endswith('.jpg'):
		shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\images')
		#print(filename)
	elif filename.endswith('.jpeg'):
		shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\images')
		#print(filename)
	elif filename.endswith('.JPEG'):
		shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\images')
		#print(filename)
	elif filename.endswith('.JPG'):
		shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\images')
		#print(filename)
	elif filename.endswith('.PNG'):
		shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\images')
		#print(filename)
	elif filename.endswith('.png'):
		shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\images')
		#print(filename)
	elif filename.endswith('.gif'):
		shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\images')
		#print(filename)
	elif filename.endswith('.exe'):
		shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\exe')
		#print(filename)
	elif filename.endswith('.msi'):
		shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\exe')
		#print(filename)
	elif filename.endswith('.mp4'):
		shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\videos')
		#print(filename)
	elif filename.endswith('.m4v'):
		shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\videos')
		#print(filename)
	elif filename.endswith('.wmv'):
		shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\videos')
		#print(filename)
	elif filename.endswith('.webm'):
		shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\videos')
		#print(filename)
	elif filename.endswith('.jar'):
		shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\jars')
		#print(filename)
	elif filename.endswith('.tar'):
		shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\zip')
		#print(filename)
	elif filename.endswith('.gz'):
		shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\zip')
		#print(filename)
	elif filename.endswith('.torrent'):
		shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\torrents')
		#print(filename)
	elif filename.endswith('.pdf'):
		shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\pdf')
		#print(filename)
print ('Done!')