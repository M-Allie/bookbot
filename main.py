def main():
    book_path = "books/frankenstein.txt"
    book_content = open_book(book_path)
    book_word_count = word_count(book_content)
    book_characters = character_count(convert_to_lowercase(book_content))
    
    #print(f"There are {book_word_count} words in the book.")
    #print(convert_to_lowercase(book_content))
    #print(book_characters)



def open_book(book_to_open):
    with open(book_to_open) as f:
        return f.read()

def word_count(words_to_count):
    words = words_to_count.split()
    return len(words)

def convert_to_lowercase(characters_to_convert):
    return characters_to_convert.lower()

def character_count(characters_to_count):
    counted_characters = {}
    for character in characters_to_count:
        if character in counted_characters:
            counted_characters[character] += 1
        else:
            counted_characters[character] = 1
    return counted_characters




main()
