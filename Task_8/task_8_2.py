

def polindrom(*args):
    for i in args:
        if i == i[::-1]:
            print(f"{i} слово палиндром ")





polindrom("heleh", "privet", "pollop")