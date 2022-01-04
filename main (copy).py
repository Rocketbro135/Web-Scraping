from bs4 import BeautifulSoup
import requests
import lxml

headers = {
 'User-Agent':
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
}

url = "https://www.reddit.com/r/Stadia/"

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'lxml')

for item in soup.select('.Post'):
    try:
        print('----------------------------------------')
        print(item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text())
    except Exception as e:
        #raise e
        print('')
#----------------------------------
def word_counter(str):
  counts = dict()
  words = str.split()

  for word in words:
    if word in counts:
      counts[word] += 1
    else: 
      counts[word] = 1

    return counts

print(word_counter(#Insert scrape of The word you want))


#Credits for sources:
#https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-12.php