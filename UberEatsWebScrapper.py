# LONG - COMP112-01 - FINAL PROJECT

# Importing Required Libraries 
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests

# Retrieving Webpage Contents 
city = input("Please enter the name of a city: ").replace(" ", "-")
state = input("Enter the abbreviation of your state: ")
url = "https://www.ubereats.com/city/" + city.lower() + "-" + state.lower()

# Sending a request to the page 
req = Request(url)
# Getting contents of the webpage 
webpage = urlopen(req).read()
# use BeautifulSoup to parse the webpage
soup = BeautifulSoup(webpage, 'html.parser')

# Lists for compiling all the info scrapped:
restaurant_list = []
rating_list = []
cuisine_list = []
data = {}

# By using Inspect Element, we can see that UberEats uses <h3> tag to identify restaurant names
# Therefore, we can use the <h3> tag to get all the restaurants available
for x in soup.findAll("h3")[:80]: 
     restaurant = x.get_text()
     restaurant_list.append(restaurant)
     rating = soup.find("div", text = restaurant).findNext("div").text 
     rating_list.append(rating)
     cuisine = []
     for child in x.parent.parent.find("span").parent:
          content = child.text.replace('\xa0•\xa0',"")
          if content == "":
               continue
          cuisine.append(content) 
     cuisine_list.append(cuisine)



# Compiling all the 3 lists together into a dictonary 
for i, restaurant in enumerate(restaurant_list):
     data = {}
     data[restaurant] = {
          "Food Genre": cuisine_list[i],
          "Rating": rating_list[i]
     }
     print(data)



