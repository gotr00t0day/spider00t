import requests
import re
import os
import sys
import colorama
from fake_useragent import UserAgent
from colorama import Fore, Back, Style
from urllib.parse import urljoin
 

# Extract links, files and parameters 

banner = """

       ,,,
        \\\          
 .---.  ///
(:::::)(_)():     spider00t v1.0
 `---'  \\\         c0deninja
        ///
       '''


"""

print (Fore.CYAN + banner + "\n")

colorama.init(autoreset=True)

site = input("Enter site: ")
ua = UserAgent()
header = {'User-Agent':str(ua.chrome)}    
try:
     param = []
     response = requests.get(site, headers=header)
     if response.status_code == 200:
          content = response.content
          links = re.findall('(?:href=")(.*?)"', content.decode('utf-8'))
          duplicatelinks = set(links)
          filext = input("Enter file extension: ")
          createfile = open("files.txt", "w")
          print("\n")
          for link in links:
              link = urljoin(site, link)
              if link not in duplicatelinks:
                  print(link + "\n")
                  if filext in link:
                      with open("files.txt", "a") as f:
                          f.writelines(link + "\n")
                  if "=" in link:
                      param.append(link + "\n")


except requests.exceptions.ConnectionError:
    print (Fore.RED + "Connection Error")
except requests.exceptions.MissingSchema:
    print (Fore.RED + "Please use: http://site.com")

print("\n")

with open("files.txt", "r") as f2:
    print (Fore.CYAN + "Found: {} links on {}".format(len(link), site))
    print (Fore.CYAN + "Found: {} {} files".format(len(f2.readlines()), filext))
    createfile.close()

with open("params.txt", "w") as f3:
    f3.writelines(param)

print(Fore.CYAN + "Found: {} parameters".format(len(param)))