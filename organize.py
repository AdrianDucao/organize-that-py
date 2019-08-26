#!/bin/python3.7

import os
import shutil

SourcePath='/home/ian/Downloads/'
sourcefiles = os.listdir(SourcePath)

VideoPath = '/home/ian/Videos/'
PicturePath = '/home/ian/Pictures/'

for file in sourcefiles:
        if file.endswith('.mp4'):
                shutil.move(os.path.join(SourcePath,file), os.path.join(VideoPath,file))
                print(file)
                print('MP4 File Moved.')
        
        elif file.endswith('.avi'):
                shutil.move(os.path.join(SourcePath,file), os.path.join(PicturePath,file))
                print(file)
                print('AVI File Moved.')

        elif file.endswith('.mkv'):
                shutil.move(os.path.join(SourcePath,file), os.path.join(PicturePath,file))
                print(file)
                print('MKV File Moved.')

        elif file.endswith('.jpg'):
                shutil.move(os.path.join(SourcePath,file), os.path.join(PicturePath,file))
                print(file)
                print('JPG File Moved.')

        elif file.endswith('.png'):
                shutil.move(os.path.join(SourcePath,file), os.path.join(PicturePath,file))
                print(file)
                print('PNG File Moved.')
        
        elif file.endswith('.jpeg'):
                shutil.move(os.path.join(SourcePath,file), os.path.join(PictureDestinationPath,file))
                print(file)
                print('JPEG File Moved.')
