def dictionary_count(mydict):
    return 

def word_count(text):
    words = text.split()
    return len(words)

def get_letter(text):
    text = text.lower()
    mydict = {}
    for char in text:
        if char.isalpha():
            if char not in mydict:
                mydict[char] = 1
            else:
                mydict[char] += 1    

    sorted_list = sorted(mydict.items(), key=lambda pair: pair[1], reverse=True)
    for char, count in sorted_list:
        return sorted_list