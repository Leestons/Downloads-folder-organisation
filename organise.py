#! python3
# organise.py - Organises downloads folder.

import shutil
import os
import send2trash
import datetime

now = datetime.datetime.now()
logFile = open('C:\\Users\\Lee\\Downloads\\log.txt', 'a')
logFile.write(now.strftime("%d-%m-%y %H:%M \n"))
logFile.write('\n')


def logging(file):
    print('MOVED', file)
    logFile.write('MOVED ' + file + '\n')


video_ext = [".3g2", ".3gp", ".asf", ".asx", ".avi", ".flv", ".m2ts", ".m4v", 
             ".mkv", ".mov", ".mp4", ".mpg", ".mpeg", ".rm", ".swf", ".vob", 
             ".webm", ".wmv"]
image_ext = [".jpg", ".jpeg", ".JPEG", ".JPG", ".png", ".PNG"]
exe_ext = [".exe", ".msi"]
gif_ext = [".gif"]
music_ext = [".mp3"]
zip_ext = [".zip", ".rar", ".tar", ".gz"]
iso_ext = [".iso"]
jar_ext = [".jar"]
torrent_ext = [".torrent"]
pdf_ext = [".pdf"]
for filename in os.listdir('C:\\Users\\Lee\\Downloads'):
    try:
        if filename.endswith(tuple(zip_ext)):
            shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\zip')
            logging(filename)
        elif filename.endswith(tuple(iso_ext)):
            shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\iso')
            logging(filename)
        elif filename.endswith(tuple(image_ext)):
            shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\images')
            logging(filename)
        elif filename.endswith(tuple(gif_ext)):
            shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\gif')
            logging(filename)
        elif filename.endswith(tuple(exe_ext)):
            shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\exe')
            logging(filename)
        elif filename.endswith(tuple(video_ext)):
            shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\videos')
            logging(filename)
        elif filename.endswith(tuple(jar_ext)):
            shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\jars')
            logging(filename)
        elif filename.endswith(tuple(torrent_ext)):
            shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\torrents')
            logging(filename)
        elif filename.endswith(tuple(pdf_ext)):
            shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\pdf')
            logging(filename)
        elif filename.endswith(tuple(music_ext)):
            shutil.move(filename, 'c:\\Users\\Lee\\Downloads\\music')
            logging(filename)
    except OSError:
        send2trash.send2trash(filename)
        print('DELETED {}. File already exists.'.format(filename))
        logFile.write('DELETED' + filename)
logFile.write('\n')
logFile.close()
print('Log file written successfully')
input('Press enter to quit')
