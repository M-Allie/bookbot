def main():
    book_path = "books/frankenstein.txt"
    book_content = open_book(book_path)
    book_word_count = word_count(book_content)
    book_character_count = character_count(convert_to_lowercase(book_content))
    book_list_of_dictonaries = convert_dictonary_to_listOfDictonaries(book_character_count)

    print(f'--- Begin report of {book_path} ---')
    print(f'{book_word_count} words found in the document', end='\n \n \n')
    print_letters(book_list_of_dictonaries)


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

def convert_dictonary_to_listOfDictonaries(dictionary):
    list_of_dictionaries = []
    for item in dictionary:
        dict = {"Character": item, "Number": dictionary[item]}
        list_of_dictionaries.append(dict)
    return list_of_dictionaries

def sort_on(dict):
    return dict["Number"]

def print_letters(characters_to_print):
    characters_to_print.sort(reverse=True, key=sort_on)
    
    for i in characters_to_print:
        char = i["Character"]
        if char.isalpha() == True:
            print(f'The {i["Character"]} character was found {i["Number"]} times.')

main()
