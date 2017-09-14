
'''
The MIT License (MIT)
Copyright (c) 2014 Patrick Olsen
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
Author: Michael Spencer
Email: mwspencer75@gmail.com
Twitter: 
Version 9.2
'''

#Starting Messing with this Version, Version 9 is the robust one

#googe_search
#Uses Beautiful soup and webdriver to google search an imported url
#Then returns the related url from html
#Then searches that url, and so on and so forth.

#Using lxml parser

from bs4 import BeautifulSoup
from selenium import webdriver
import unicodecsv as csv
import time

url = 'https://www.google.com/search?q=What+are+the+best+tools+for+finding+Instagram+influencers&rlz=1C1CHFX_enUS601US601&oq=What+are+the+best+tools+for+finding+Instagram+influencers&aqs=chrome..69i57.24849j0j7&sourceid=chrome&ie=UTF-8'

rel_search_dir = "Related_Results.txt" #enter path to new text file here
rec_search_dir = "Recommended_Results.txt"
rel_parse_dir = "Related_Parsed.txt"
rec_parse_dir = "Recommended_Parsed.txt"
search_val = "How to get more instagram followers"

def get_related_search(url):
    """Creates a list of href from the class _e4d"""
    rel_links = [] 
    driver = webdriver.Chrome() 
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "lxml")
    links = soup.select("p._e4b a[href]") 
    
    for link in links: 
        rel_link = link['href']
        rel_link = str(rel_link)
        rel_links.append(rel_link)
    driver.close()
    return rel_links
    
def get_recommended_search(url, search_val):
    """Creates a list of recommended searches"""
    reco_words = []
    driver = webdriver.Chrome() 
    driver.get("http:\\www.google.com")
    search = driver.find_element_by_name('q')
    search.send_keys(search_val)
    time.sleep(8)
    soup = BeautifulSoup(driver.page_source, "lxml")
    recommendations = soup.select("div.sbqs_c b")
    for reco in recommendations:
        reco_word = reco
        reco_words.append(search_val + reco_word.get_text())
    driver.close()
    print(reco_words)
    return reco_words
    
        
    
    
def write_to_file(dir, results):
    """writes file to directory"""
    for res in results:
        with open(dir, "a") as f:
            f.write(res + "\n") 
        f.close()


def parse_data(fname, dir):
    """Parses the google searches, then creates a list of the words"""
    lists_words = list()
    data = list()
    try:
        fhand = open(fname)
    except:
        print("This is not a file name")
        quit()
    for line in fhand:
        line = line.split("=")
        line = line[2].split("&sa")
        line = line[0].split("+")
        lists_words.append(line)
    for lists in lists_words:
        for word in lists:
            data.append(word)
    return data
    
def get_count(results):
    """Creates a dictionary, word being the key, and word count being the value"""
    counts_dict = dict()
    for word in results:
        counts_dict[word] = counts_dict.get(word, 0) + 1
    return counts_dict
    
def create_csv(counts_dict):
    """Creates a csv of the dictionary"""
    with open('key_words.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Word', 'Count'])
        for key, value in counts_dict.items():
            writer.writerow([key, value])
    csv_file.close()
    
def main(url, rel_search_dir, rec_search_dir, rel_parse_dir, search_val, numTime):
    #url: url to seach
    #rel_search_dir: directory to save related search text file
    #rec_search_dir: directory to save recommeded text file 
    #numTime: number of times to search
    
    i = numTime
    j = numTime
    
    print("Working on related searches")
    for x in range(i):
        rel_links = get_related_search(url)
        write_to_file(rel_search_dir, rel_links)
        url = 'https://www.google.com' + rel_links[0]
    

    print("Working on recommendation")
    for x in range(j):
        
        reco_words = get_recommended_search('http://www.google.come', search_val)
        write_to_file(rec_search_dir, reco_words)
        
        
        
    print("Working on parsing data to text.")
    data_rel = parse_data(rel_search_dir, rel_parse_dir)
    #data_rec = 
    print("Working on dictionary")
    dict_count = get_count(data_rel)
    print("These are the counts: ", dict_count)
    print("Now creating csv of counts")
    create_csv(dict_count)
    print("All done!  Check out the results in whichever folder you ran this script.")        
        
main(url, rel_search_dir, rec_search_dir, rel_parse_dir, search_val, 1)







