# import libraries
import requests
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire import webdriver

import sys
import re
import os
from selenium.webdriver.support.relative_locator import locate_with

# folder with all lyrics
all_path = #r"YOUR OWN FILEPATH"

# proxy setup
# NOTE: can be run on your own computer by deleting all lines related to the proxy and sw_options
proxy_host = "38.153.152.244"
proxy_port = "9594"

proxy_user = "fdiywpvf"
proxy_pass = "gpslbbon6x5f"


# set up proxy
sw_options = {
    'proxy': {
        'http': f'http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
        'https': f'https://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}'
    }
}

# chrome service + web driver
w_driver = webdriver.Chrome(
    service = ChromeService(ChromeDriverManager().install()),
    seleniumwire_options = sw_options
)

# what artist does the user wish to search for
def req_artist():
    return input("What artist do you want to search for?")

# return potential artists
# NOTE: this function was not used in the final version but would have combed through a page full of artists based on the user's input but was ultimately not used; ignore it
def sch_artist(reqd_artist):
    schd_artist = ""
    chars = "[0123456789][.][ ]"
    # iterate through pages if necessary
    page = 1

    # retrieve website and data
    w_driver.get("https://search.azlyrics.com/search.php?q=" + reqd_artist + "&w=artists&p=" + str(page) + "&x=57d767e406310e8d33e6ad407d7d6ea73ba8891fed4069c8c883211c1802fa49")
    a_list = w_driver.find_element(By.TAG_NAME, "tbody")

    # how many pages
    num_pages = len(w_driver.find_elements(By.CLASS_NAME, "btn btn-primary btn-nav"))

    # print text
    a_split = re.split(chars, a_list.text)
    print("Is the artist any of the following? There are " + str(num_pages) + " total pages.")
    for artist in a_split:
        print(artist)
    # ask user if any of the following are artists they want

    # return artist they request
    return schd_artist

# main
if __name__ == "__main__":

    # go to base website domain
    w_driver.get("https://www.azlyrics.com/")
    # requested artist
    req_art = req_artist().replace(" ", "").lower()
    # artist path
    full_path = os.path.join(all_path, req_art)

    # create folder of artist name and create files there
    try:
        os.mkdir(full_path)
    except FileExistsError as e:
        print("You have already started scanning this artist!")

    # change to new folder
    os.chdir(full_path)

    # requested artist page, contains all songs on the site
    # download the titles + lyrics as files to a folder
    w_driver.get("https://www.azlyrics.com/" + req_art[0] + "/" + req_art + ".html")

    # for every link to a song, scrape the lyrics to a file into a folder
    # iterate through every song under the div listAlbum
    # every single item here is named listalbum-item

    # get songs from the page
    # retrieve songs to go to their page
    la_items = w_driver.find_elements(By.XPATH, "//div[contains(concat(' ', @class, ' '), ' listalbum-item ')]/a")

    # create a list of all the titles
    titles = list()

    # convert text into usable titles (no special characters, no spaces)
    for la in la_items:
        title = re.sub("[^A-z0-9]", "", la.text)
        title_path = os.path.join(full_path, title) + ".txt"

        # print(title_path)

        # if title does not exist in the current folder, append it
        if not os.path.exists(title_path):
            titles.append(title)

    # if there are no titles left to scrape, end program
    if len(titles) == 0:
        sys.exit("You already scanned this artist! There are no songs left.")

    print(titles)

    # wait function (wait until lyrics have loaded)
    wait = WebDriverWait(w_driver, 5)

    # comb through each site, and save each title and text as a JSON file
    for title in titles:
        # retrieve lyrics from site (XPATH: /html/body/div[2]/div[2]/div[2]/div[5])

        # try to parse lyrics, if the song's title does not exist on the site, skip it and continue
        try:
            w_driver.get("https://www.azlyrics.com/lyrics/" + req_art + "/" + title.replace(" ", "").lower() + ".html")
            wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[5]")))
            lyrics = re.sub(r"\[(.*?)]", "", w_driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[5]").text)

        except (TimeoutException, NoSuchElementException):
            print("Song " + title + " not found or took too long to load. Continuing.")
            continue

        # try to create a file from this song; if it already exists, skip it and continue (some artists will release the same song twice)
        try:
            # create new file
            f_name = title + ".txt"
            new_f = open(f_name, "w+")

            # write lyrics to file
            new_f.write(lyrics)
            new_f.close()

        except FileExistsError as e:
            print("Song " + title + " already found. Continuing.")
            continue
        #print(lyrics)

    # after driver finishes, quit
    w_driver.quit()
