import sys, time, requests
from bs4 import BeautifulSoup


def get_review():
    filename = "Titanic"
    website = "https://www.imdb.com/title/tt0120338/reviews"
    reviewlink = website.strip()
    print(reviewlink)
    res = requests.get(reviewlink)
    if res.status_code == 404:
        print('MOVIE NOT FOUND, CHECK SPELLING !')
        time.sleep(2)
        sys.exit()
    result = res.content
    html = BeautifulSoup(result)
    review = html.findAll("div", {"class": "text show-more__control"})
    print(str(filename) + ' reviews')
    print('.......................................')
    texts = [x.text for x in review]
    x = ['\n'.join(texts)]
    for i in x:
        print(i)
    time.sleep(2)
    sys.exit()


def main():
    get_review()


if __name__ == '__main__':
    main()
