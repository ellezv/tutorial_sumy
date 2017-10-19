"""A simple script to generate a summary from a given url."""

from bs4 import BeautifulSoup

import requests

from sumy.nlp.stemmers import Stemmer
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer
from sumy.utils import get_stop_words


def get_text(url):
    """Return string of main content from a given url"""
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    p_tags = soup.find_all('p')
    return ' '.join(map(lambda p: p.text, p_tags))


def summarize(url, language, sentences):
    """Return a generated summary of url content."""
    text = get_text(url)
    parser = PlaintextParser(text, Tokenizer(language))
    summarizer = LsaSummarizer(Stemmer(language))
    summarizer.stop_words = get_stop_words(language)

    for sentence in summarizer(parser.document, sentences):
        print(sentence)

if __name__ == '__main__':
    url = input('what do you not want to read? ')
    language = input('What is the language? ')
    sentences = input('How many sentences can you withstand? ')
    summarize(url, language, sentences)
