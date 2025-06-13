from stats import count_words, count_characters, sort_dictionary
import sys

def main(path_to_file):
    with open(path_to_file) as f:
        text = f.read()
        return (text)

path_to_file = ""

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path_to_file = sys.argv[1]

book = main(path_to_file)
#count_words(book)
#count_characters(book)
#sort_dictionary(count_characters(book))

print("============ BOOKBOT ============")
print(f"Analyzing book found at {path_to_file}")
print("----------- Word Count ----------")
num_words = count_words(book)
print(f"Found {num_words} total words")
print("--------- Character Count -------")

for dictionary in sort_dictionary(count_characters(book)):
    print(f"{dictionary['char']}: {dictionary['num']}")

print("============= END ===============")