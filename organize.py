#!/usr/bin/env python3

import os
import shutil

SourcePath='/home/ian/Downloads/'
sourcefiles = os.listdir(SourcePath)
SecondSource = '/home/ian/Downloads/VideoDownloader/'
secondsourcefile = os.listdir(SecondSource)

VideoPath = '/home/ian/Videos/'
PicturePath = '/home/ian/Pictures/'
DocumentPath = '/home/ian/Documents/'

for file in sourcefiles or secondsourcefile:
        
        if file.endswith('.mp4'): #Videos
                shutil.move(os.path.join(SourcePath,file), os.path.join(VideoPath,file))
                print(file)
                print('MP4 File Moved.')
        
        elif file.endswith('.avi'):
                shutil.move(os.path.join(SourcePath,file), os.path.join(VideoPath,file))
                print(file)
                print('AVI File Moved.')

        elif file.endswith('.mkv'):
                shutil.move(os.path.join(SourcePath,file), os.path.join(VideoPath,file))
                print(file)
                print('MKV File Moved.')
        
        elif file.endswith('.webm'):
                shutil.move(os.path.join(SourcePath,file), os.path.join(VideoPath,file))
                print(file)
                print('Webm File Moved.')
        
        elif file.endswith('.MP4'):
                shutil.move(os.path.join(SourcePath,file), os.path.join(VideoPath,file))
                print(file)
                print('MP4 File Moved.')

        elif file.endswith('.mp4'): #YTDownloader
                shutil.move(os.path.join(SecondSource,file), os.path.join(VideoPath,file))
                print(file)
                print('MP4 File Moved.')
        
        elif file.endswith('.avi'):
                shutil.move(os.path.join(SecondSource,file), os.path.join(VideoPath,file))
                print(file)
                print('AVI File Moved.')

        elif file.endswith('.mkv'):
                shutil.move(os.path.join(SecondSource,file), os.path.join(VideoPath,file))
                print(file)
                print('MKV File Moved.')
        
        elif file.endswith('.webm'):
                shutil.move(os.path.join(SecondSource,file), os.path.join(VideoPath,file))
                print(file)
                print('Webm File Moved.')
        
        elif file.endswith('.MP4'):
                shutil.move(os.path.join(SecondSource,file), os.path.join(VideoPath,file))
                print(file)
                print('MP4 File Moved.')

        elif file.endswith('.jpg'): #Pictures
                shutil.move(os.path.join(SourcePath,file), os.path.join(PicturePath,file))
                print(file)
                print('JPG File Moved.')

        elif file.endswith('.png'):
                shutil.move(os.path.join(SourcePath,file), os.path.join(PicturePath,file))
                print(file)
                print('PNG File Moved.')
        
        elif file.endswith('.jpeg'):
                shutil.move(os.path.join(SourcePath,file), os.path.join(PicturePath,file))
                print(file)
                print('JPEG File Moved.')
        
        elif file.endswith('.gif'):
                shutil.move(os.path.join(SourcePath,file), os.path.join(PicturePath,file))
                print(file)
                print('GIF File Moved.')

        elif file.endswith('.pdf'):#Documents
                shutil.move(os.path.join(SourcePath,file), os.path.join(DocumentPath,file))
                print(file)
                print('PDF File Moved.')

        elif file.endswith('.doc'):
                shutil.move(os.path.join(SourcePath,file), os.path.join(DocumentPath,file))
                print(file)
                print('Doc File Moved.')

        elif file.endswith('.txt'):
                shutil.move(os.path.join(SourcePath,file), os.path.join(DocumentPath,file))
                print(file)
                print('TXT File Moved.')

        elif file.endswith('.xlsx'):
                shutil.move(os.path.join(SourcePath,file), os.path.join(DocumentPath,file))
                print(file)
                print('Spreadsheet File Moved.')
