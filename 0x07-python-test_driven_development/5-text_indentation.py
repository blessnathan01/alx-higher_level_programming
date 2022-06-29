#!/usr/bin/python3
"""
    5-text_indentation: text_indentation()
"""


def text_indentation(text):
    """
        text_indentation prints text with 2 new lines after . ? and :
        Args:
            text (str): text to be formatted.
    """

    tmp = ""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if len(text) == 0:
        return

    for letter in text:
        tmp += letter
        if letter in ["?", ":", "."]:
            while tmp[0] == " ":
                tmp = tmp[1:]
            print(tmp)
            print()
            tmp = ""
    if len(tmp) != 0:
        try:
            while tmp[0] == " ":
                tmp = tmp[1:]
        except:
            pass
        print(tmp, end="")
