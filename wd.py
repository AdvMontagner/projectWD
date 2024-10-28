#!bin/bash
#>> PROJECT WD
#>> PROJECT TO GET ONLINE WORDLIST'S CONTENT'S AND SAVE IN A LOCAL WORDLIST ARCHIVE

import requests
import subprocess

def clear():
    try:
        subprocess.run("clear") # LINUX
    except:
        subprocess.run("cls") # CMD - WINDOWS
clear()

wordlists = []

while True:
    url = input("URL | (s)ee saved url's / (d)delete url / (st)art / (sa)ve URL's / (r)ead URL file / (e)xit: ")
    url = url.lower()
    url = url.strip()

    if (url == "s"):
        clear()
        for urlAdded in wordlists:
            print(urlAdded)
        
        print("\n")
    
    elif (url == "st"):
        clear()
        wdArchive = input("Archive to save: ")
        
        try:
            archiveContent = open(wdArchive, "r+")
            clear()
        except:
            archiveContent = open(wdArchive, "w+")
            clear()
        print(f"{wdArchive} SELECTED!")
        
        for wd in wordlists:
            print(f"Starting getting the wordlist in {wd}...")

            try:
                request = requests.get(wd)
                print(request.status_code)
                response = request.text
                response.replace(" ", "\n")
                
                pastArchiveContent = archiveContent.read()

                archiveContent.write(pastArchiveContent + "\n" + response)
                print(archiveContent.read())

            except Exception as err:
                print(f"Error...")
                print(err)
                continue

    elif (url == "r"):
        clear()

        try:
            archive = open(input("Archive: "), "r+")
            
            for url in archive.readlines():
                url = url.strip()
                print(url)
                print(f"{url} added...")
                wordlists.append(url)

        except:
            print("Archive not found!")

    elif (url == "sa"):
        clear()
        finalText = ""

        for url in wordlists:
            finalText = f"{finalText}\n{url}".strip()
            archive = open("WD-urls.txt", "w+")
            archive.write(finalText)

            print(f"Saving {url}...")

    elif (url == "e"):
        break

    elif (url == "d"):
        clear()
        for i in range(0, len(wordlists)):
            print(f"{i}: {wordlists[i]}")

        toRemoveUrl = int(input("URL Number: "))

        try:
            wordlists.remove(wordlists[toRemoveUrl])
        except:
            pass

        print("")

    else:
        clear()
        wordlists.append(url)
        print(f"{url} ADDED!\n")