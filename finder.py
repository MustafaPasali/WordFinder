
def word_finder(word, text):
    word = word.lower()
    text = text.lower()

    dict = {}
    count = 0
    cursor = 0
    while True:

        if text.find(word, cursor) != -1:
            count += 1
            start = text.find(word, cursor)
            finish = start + len(word)
            dict.update({count: {"Start": start, "Finish": finish}})
            cursor = finish
        else:
            print(count)
            break

    return dict

