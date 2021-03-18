from bisect import bisect_left
import string
import sys
import os

class WhiteList:
    """
    Base class for white list chat filtering.  Accepts a list of good words and offers
    filtering functions performed against that list.
    """
    def __init__(self,wordlist):
        self.words = wordlist
        self.words.sort()

        self.numWords = len(self.words)

    def cleanText(self,text):
        if isinstance(text, bytes):
            text = text.decode().strip('.,?!')
        else:
            text = text.strip('.,?!')

        text = text.lower()
        return text

    def isWord(self,text):
        text = self.cleanText(text)
        i = bisect_left(str(self.words),str(text))
        if i not in self.words:
            return False
        if i == self.numWords:
            return False
        return self.words[i] == text

    def isPrefix(self,text):
        text = self.cleanText(text)
        i = bisect_left(self.words,text)

        if i == self.numWords:
            return False

        return self.words[i].startswith(text)

    def prefixCount(self,text):
        text = self.cleanText(text)
        i = bisect_left(self.words,text)

        j = i

        while j < self.numWords and self.words[j].startswith(text):
            j += 1

        return j - i

    def prefixList(self,text):
        text = self.cleanText(text)
        i = bisect_left(self.words,text)

        j = i

        while j < self.numWords and self.words[j].startswith(text):
            j += 1

        return self.words[i:j]
