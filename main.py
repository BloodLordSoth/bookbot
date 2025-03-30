from stats import word_count, get_letter
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = word_count(text)
    letter_count = get_letter(text)
    print("============ BOOKBOT ============")
    print(f"Analying book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in letter_count:
        print(f"{char}: {count}")
    print("============= END ===============")

main()

