#!usr/bin/env python3
import turtle
import pyfiglet
from termcolor import colored
print(colored("*************Website Source Code Downloader**************",'blue'))
print()
print(colored("*************AUTHOR N3X4R PH4NTH0M***************",'red'))
banner =colored(pyfiglet.figlet_format("Source Code Downloader"),"red")
print(banner)





import urllib.request as u
website_name = input("Enter Your Target Website:")
source_open = u.urlopen(website_name)
read_source_code = source_open.read()
print("Source Code:",read_source_code)