import requests, json
from pprint import pprint

quoteURL = "http://www.iheartquotes.com/api/v1/random?format=json&max_lines=3&source=literature"

def main():
    quote = get_quote()
    pprint(format_quote(quote))

def get_quote():
    quotedata = requests.get(quoteURL).json()
    return quotedata["quote"]

def format_quote(quote):
    quote = quote.encode('ascii', 'ignore')
    dash = quote.find("--")
    if dash != -1:
        author = quote[dash+3:].lstrip()
        quote = quote[0:dash].rstrip()
    else:
        author = ""
    
    q = {}
    q["quote"] = quote
    q["author"] = author
    return q


if __name__ == "__main__":
    main()
