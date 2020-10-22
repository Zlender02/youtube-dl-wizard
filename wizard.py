#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import os.path
import platform # from getpass import getuser
import getpass # from getpass import getuser

# Get platform and user information
platform = platform.system()
username = getpass.getuser()
format_content = ""
# download_path will be changeable in the near future.
download_path = "~/Downloads/youtube-dl"
# In the near future this script will no longer need portable dependencies to work. It would first check if its installed natively on the system and then check for portable dependencies.
dependencies = "ffmpeg_ffprobe"

# Selection of the download format
def format_selection():
    global link
    global format_content
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
    # I wanted to use a case statement here, but quickly realized that python does not have one by default. Looking for alternatives.
    # youtube-dl converts the tilde (~) shortcut to the Windows user directory.
    
    def youtube_dl_exec():
        print ("Downloading...")
        os.system('python youtube-dl -q %s --add-metadata --metadata-from-title "%%(artist)s - %%(title)s" --ffmpeg-location %s --audio-quality 0 -o "%s/%%(title)s.%%(ext)s" %s' % (format_content,dependencies,download_path,link))

    if (input_format == "0"):
        youtube_dl_exec()
    elif (input_format == "1" or input_format == "mp4"):
        format_content = "--recode-video mp4"
        youtube_dl_exec()
    elif (input_format == "2" or input_format == "mkv"):
        format_content = "--recode-video mkv"
        youtube_dl_exec()
    elif (input_format == "3" or input_format == "flv"):
        format_content = "--recode-video flv"
        youtube_dl_exec()
    elif (input_format == "4" or input_format == "webm"):
        format_content = "--recode-video webm"
        youtube_dl_exec()
    elif (input_format == "5" or input_format == "avi"):
        format_content = "--recode-video avi"
        youtube_dl_exec()
    elif (input_format == "6" or input_format == "ogg"):
        format_content = "--extract-audio --audio-format vorbis"
        youtube_dl_exec()
    elif (input_format == "7" or input_format == "mp3"):
        format_content = "--extract-audio --audio-format mp3"
        youtube_dl_exec()
    elif (input_format == "8" or input_format == "m4a"):
        format_content = "--extract-audio --audio-format m4a"
        youtube_dl_exec()
    elif (input_format == "9" or input_format == "wav"):
        format_content = "--extract-audio --audio-format wav"
        youtube_dl_exec()
    elif (input_format.lower() == "q"):
        quit()
    else:
        print ("Invalid option, try again.")
        format_selection()

    if platform == "Windows":
        print("Your download is located here:\n C:\\Users\\%s\\Downloads\\youtube-dl"%username)
    elif platform == "Linux":
        print ("Your download is located here:\n /home/%s/Downloads/youtube-dl"%username)
    elif platform == "Darwin":
        print ("Your download is located here:\n /Users/%s/Downloads/youtube-dl"%username)
    else:
        quit()

# Assign the URL of the content they want to download to the variable "link"
def search_has_url():
    global link
    link = input("Insert the link of the content you want to download: ")
    format_selection()

# Assign the search query with the prefix "ytsearch:" to the variable "link"
# ytsearch: to automatically grab the URL of the first youtube search result
def search_ytsearch():
    global link
    link = "ytsearch:" + '"' + input("Type your search query (The first result will be downloaded automatically): ") + '"'
    format_selection()

def search_selection():
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
        quit()
    else:
        print ("Invalid option, try again.")
        search_selection()

# Check if youtube-dl exists. This system will be improved soon to add support for the installed version of the software (not the portable one).
if os.path.isfile("youtube-dl"):
    search_selection()
else:
    print ("youtube-dl python binary does not exist")

# Working on integration with FreeBSD