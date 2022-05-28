# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from enum import unique


def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as J:
        readtext = J.read()
    return readtext


# read_file_content("story.txt")


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    textlist = text.replace("\n", "").replace(
        ".", "").replace("?", "").replace(".", "").split(" ")
    text_dict = {}
    for x in textlist:
        if x in text_dict:
            text_dict[x] += 1
        else:
            text_dict[x] = 1
    print(text_dict)


count_words()
