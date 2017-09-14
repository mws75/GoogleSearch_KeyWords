# GoogleSearch_KeyWords
Type in a Google Search url, and output will be csv's containing keywords which are obtained from the recommended searches as well as related searches. 

This script is used to find key words related to a specific google search.  You need to copy and paste the url to the Google search you want to perform.
Ex:   I googled: "What are the best tools for finding Instagram influencers"
Then I copy and paste the URL into my code (in this version it is line 15).

url = 'https://www.google.com/search?q=What+are+the+best+tools+for+finding+Instagram+influencers&rlz=1C1CHFX_enUS601US601&oq=What+are+the+best+tools+for+finding+Instagram+influencers&aqs=chrome..69i57.24849j0j7&sourceid=chrome&ie=UTF-8'

You also need to add the Related Search Value, search_val.  This can be different or the same, depending on what you are looking for. 

Then add the number of times you want to loop through as the last variable in main().
main(url, rel_search_dir, rec_search_dir, rel_parse_dir, search_val, 1)

The default variables are: 
rel_search_dir = "Related_Results.txt"
rec_search_dir = "Recommended_Results.txt"
rel_parse_dir = "Related_Parsed.txt"
rec_parse_dir = "Recommended_Parsed.txt"



Some Notes: 

I have not added a function that excludes generic words like 'the', 'a', 'to'...

This version uses Chromedriver with selenium.  I was not able to get a Firefox version working, from what I read there are some bugs with the new gecodriver. Not sure if there has been an update or work around yet. 
