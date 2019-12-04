#!/usr/bin/env python3

from urllib.request import urlopen
import sys

def fetch_first_words(url, number_of_words):
    """Fetch first words from an url

        Args:
            url of the website to fetch
            number_of_words total words to print

        Returns:
            prints list of words
    """
    with urlopen(url) as story:
            story_words = []
            words_count = 0
            for line in story:
                if words_count >= number_of_words:
                    break;
                line_words = line.decode('utf-8').split()
                for word in line_words:
                    if words_count >= number_of_words:
                        break;
                    story_words.append(word)
                    words_count += 1;
            printItems(story_words)
    return story_words

def printItems(itemList):
    for item in itemList:
        print(item)


def commandLine(url):
    fetch_first_words(url, 10)


if(__name__ == '__main__'):
    commandLine(sys.argv[1])