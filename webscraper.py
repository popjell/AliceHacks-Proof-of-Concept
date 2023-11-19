#Proof of concept for our idea. 
#This is a webscraper that gets info from the web about a conflict and summarizes it.
#Would have liked to do more, but money constrains limited us.

import os
#Please install all of these packages before running the code (These are the windows commands idk ab macos or linux or replit)
#pip install transformers
#pip install requests
#pip install bs4
#pip install python-dotenv
#pip install google
from transformers import pipeline
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv, find_dotenv    
from googlesearch import search
 
#Can be changed based off current humanitarian crisis. 
#Make sure to specify news because you dont want to accidentally web scrape a military website and get flagged
#(I definetly did not do that by accident)
prompt = "Isreal Hamas Updates \"news\""

#This is a proof of concept of our idea. It gets info from the web about a conflict and summarizes it.
#The entire idea was not fully realized due to time and money constraints(Open ai costs money)

load_dotenv(find_dotenv())
#Get this from https://huggingface.co/settings/tokens, and place into an env file at the same level as this file
API_TOKEN = os.getenv("API_KEY")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
API_URL = "facebook/bart-large-cnn"
def scrape(query):
    # to search
    urls = search(query, tld="co.in", num=2, stop=2, pause=2)
    urls = list(urls)
    url = urls[1]
    #Note: For times sake, I am just summarizing the first result, as current ai models are very slow.
    #If you want to summarize more, just change the index of urls to 1,2,3,4,5,6,7,8,9,10, or use a for loop to loop the code underneath
    #There are many limitations to the ai model used. It is advised to used openai's gpt-4 model, but I'm too broke for that
    #With gpt-4, you can summarize more, faster, and even ask questions about the data given.
    #Also sometimes the model chooses a random website that has nothing. When a large scale implementation is provided, this does not matter, as that website will be one of 500 or so websites. 
    #However, the time complexity for the ai model used is too high to do that. Better ai models that cost money remove this problem
    #GPT-4 should be used. Im not using it because im a broke highscooler.
    #In order to use gpt-4, after paying for the tokens, you need to replace lines 47, 48, and 51 with whatever code gpt-4 needs to summarize
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.title.string)
    paragraphs = soup.find_all('p')
    summarized = ""
    for para in paragraphs:
        text = summarizer(para.text, max_length=(30), min_length=5, do_sample=False)
        summarized += "\n\n" + text[0]['summary_text']
    #This step takes forever, due to the models limitation. It does work, just be patient(Liek 5 hours patient)
    #Once again, this limitation will be removed with gpt-4
    return summarizer(summarized, max_length=(512), min_length=5, do_sample=False)
    
output = scrape(prompt)
print(output)
    

    
    




