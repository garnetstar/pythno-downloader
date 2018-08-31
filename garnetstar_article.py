import urllib.request, json 
from datetime import date
import os

today = date.today()
directory = str(today)

if not os.path.exists(directory):
    os.makedirs(directory)
    
with urllib.request.urlopen("http://garnetstar.hukot.net:8081/article") as url:
    data = json.loads(url.read().decode())
    
for element in data:
    with urllib.request.urlopen("http://garnetstar.hukot.net:8081/article/" + str(element['article_id']) ) as articleUrl:
        articleData = json.loads(articleUrl.read().decode())
        
        fileName = directory + '/' + articleData['title'] + '.md'
        file = open(fileName, 'w')
        file.write(articleData['content'])
        file.close
        print(fileName + ' succesfully saved')
        
