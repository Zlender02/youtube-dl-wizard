#!/usr/bin/env python3

import os
import sys
import os.path
import platform
import getpass

# Get platform and user information
platform = platform.system()
username = getpass.getuser()

# Selection of the download format
def format():
    global link
    print('''
In which format you want to download it?

 0 = I don't mind
 1 = Video (mp4)
 2 = Video (mkv)
 3 = Video (flv)
 4 = Video (webm)
 5 = Video (avi)
 6 = Audio (ogg)
 7 = Audio (mp3)
 8 = Audio (m4a)
 9 = Audio (wav)

q = Quit
        ''')
    input_format = input("Response: ")
    
    print ()
    # I wanted to use a case statement here, but quickly realized that python does not have one by default. Working on a workaround.
    # youtube-dl converts the tilde (~) shortcut to the Windows user directory.
    if (input_format == "0"):
        print ("Downloading...")
        os.system('python youtube-dl --ffmpeg-location ffmpeg_ffprobe -q --audio-quality 0 -o "~/Downloads/youtube-dl/%(title)s.%(ext)s" ' + link)
    elif (input_format == "1" or input_format == "mp4"):
        print ("Downloading...")
        os.system('python youtube-dl --ffmpeg-location ffmpeg_ffprobe --recode-video mp4 -q --audio-quality 0 -o "~/Downloads/youtube-dl/%(title)s.%(ext)s" ' + link)
    elif (input_format == "2" or input_format == "mkv"):
        print ("Downloading...")
        os.system('python youtube-dl --ffmpeg-location ffmpeg_ffprobe --recode-video mkv -q --audio-quality 0 -o "~/Downloads/youtube-dl/%(title)s.%(ext)s" ' + link)
    elif (input_format == "3" or input_format == "flv"):
        print ("Downloading...")
        os.system('python youtube-dl --ffmpeg-location ffmpeg_ffprobe --recode-video flv -q --audio-quality 0 -o "~/Downloads/youtube-dl/%(title)s.%(ext)s" ' + link)
    elif (input_format == "4" or input_format == "webm"):
        print ("Downloading...")
        os.system('python youtube-dl --ffmpeg-location ffmpeg_ffprobe --recode-video webm -q --audio-quality 0 -o "~/Downloads/youtube-dl/%(title)s.%(ext)s" ' + link)
    elif (input_format == "5" or input_format == "avi"):
        print ("Downloading...")
        os.system('python youtube-dl --ffmpeg-location ffmpeg_ffprobe --recode-video avi -q --audio-quality 0 -o "~/Downloads/youtube-dl/%(title)s.%(ext)s" ' + link)
    elif (input_format == "6" or input_format == "ogg"):
        print ("Downloading...")
        os.system('python youtube-dl --ffmpeg-location ffmpeg_ffprobe --extract-audio --audio-format vorbis --add-metadata --metadata-from-title "%(artist)s - %(title)s" -q --audio-quality 0 -o "~/Downloads/youtube-dl/%(title)s.%(ext)s" ' + link)
    elif (input_format == "7" or input_format == "mp3"):
        print ("Downloading...")
        os.system('python youtube-dl --ffmpeg-location ffmpeg_ffprobe --extract-audio --audio-format mp3 --add-metadata --metadata-from-title "%(artist)s - %(title)s" -q --audio-quality 0 -o "~/Downloads/youtube-dl/%(title)s.%(ext)s" ' + link)
    elif (input_format == "8" or input_format == "m4a"):
        print ("Downloading...")
        os.system('python youtube-dl --ffmpeg-location ffmpeg_ffprobe --extract-audio --audio-format m4a --add-metadata --metadata-from-title "%(artist)s - %(title)s" -q --audio-quality 0 -o "~/Downloads/youtube-dl/%(title)s.%(ext)s" ' + link)
    elif (input_format == "9" or input_format == "wav"):
        print ("Downloading...")
        os.system('python youtube-dl --ffmpeg-location ffmpeg_ffprobe --extract-audio --audio-format wav --add-metadata --metadata-from-title "%(artist)s - %(title)s" -q --audio-quality 0 -o "~/Downloads/youtube-dl/%(title)s.%(ext)s" ' + link)
    elif (input_format.lower() == "q"):
        print()
    else:
        print ("Invalid option, try again.")
        format()
    
    # Detect OS to show the correct file location. No support for macOS yet.
    if platform == "Windows":
        print("Your download is located here:\n C:\\Users\\" + username + "\\Downloads\\youtube-dl")
    elif platform == "Linux":
        print ("Your download is located here:\n /home/" + username + "/Downloads/youtube-dl")
    elif platform == "Darwin":
        # OS not supported yet.
        quit()
    else:
        quit()

# Assign the URL of the content they want to download to the variable "link"
def search_has_url():
    global link
    link = input("Insert the link of the content you want to download: ")
    format()

# Assign the search query with the prefix "ytsearch:" to the variable "link"
# ytsearch: to automatically grab the URL of the first youtube search result
def search_ytsearch():
    global link
    link = "ytsearch:" + '"' + input("Type your search query (The first result will be downloaded automatically): ") + '"'
    format()

def search():
    print('''
Do you know the URL of the content you want to download?

 1 = Yes
 2 = No, I want to search it on YouTube

q = Quit
        ''')

    input_search = input("Response: ")
    print()
    if (input_search == "1" or input_search == "Yes"):
        search_has_url()
    elif (input_search == "2" or input_search == "No"):
        search_ytsearch()
    elif (input_search.lower() == "q"):
        exit()
    else:
        print ("Invalid option, try again.")
        search()

# Check if youtube-dl exists. This system will be improved soon to add support for the installed version of the software (not the portable one).
if os.path.isfile("youtube-dl"):
    search()
else:
    print ("youtube-dl python binary does not exist")
