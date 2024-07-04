def main():
    book_path = "books/frankenstein.txt"
    book_content = open_book(book_path)
    book_word_count = word_count(book_content)
    
    print(f"There are {book_word_count} words in the book.")

def open_book(book_to_open):
    with open(book_to_open) as f:
        return f.read()

def word_count(words_to_count):
    words = words_to_count.split()
    return len(words)

main()
