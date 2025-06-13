def count_words(text):
    words = text.split()
    num_words = len(words)
    #print(f"Found {num_words} total words")
    return num_words

def count_characters(text):
    all_letters = {}
    words = text.split()
    for word in words:
        for letter in word:
            letter = letter.lower()
            if letter in all_letters:
                all_letters[letter] += 1
            else:
                all_letters[letter] = 1
    #print(all_letters)
    return all_letters

def sort_on(dict):
    return dict["num"]

def sort_dictionary(dict):
    list = []
    for char in dict:
        num = dict[char]
        dict_list = {"char": char, "num": num}
        if char.isalpha():
            list.append(dict_list)
    list.sort(reverse=True, key=sort_on)
    #print(list)
    return list