import requests
from bs4 import BeautifulSoup



word = input("Enter a word (enter 'q' to exit): ")

while word != 'q':
    try:

        r = requests.get(url='http://dict.youdao.com/w/'+word+'/#keyfrom=dict2.top')
        soup = BeautifulSoup(r.text, "lxml")

        s = soup.find('div',class_='trans-container').find('ul').find_all('li')




        for item in s:

            print(item.text)
        print('='*40+'\n')
    except Exception:
        print("Sorry, there is no that word in English!\n")
    finally:
        word = input( "Enter a word (enter 'q' to exit): ")