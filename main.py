def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read() 
        words_in_file = count_words(file_contents)
        characters_in_file = count_characters(file_contents)
        sorted_letters_in_file = sorted_alphabet_count(characters_in_file)    
        nice_report(f.name, words_in_file, sorted_letters_in_file)

def count_characters(file_contents):
    count = {}
    temp_character = ''
    for i in range(0, len(file_contents)-1):
        temp_character = file_contents[i].lower()
        if temp_character in count:
            count[temp_character] += 1
        else:
            count [temp_character] = 1
    return count

def sort_on(dictionary1):
    return dictionary1['count']

def sorted_alphabet_count(count):
    list_count = []
    for i in count:
        if i.isalpha() == True:
            list_count.append({'letter' : i, 'count' : count[i]})

    list_count.sort(reverse=True, key=sort_on)
    return list_count

def nice_report(book_file, word_count, letter_count):
    print(f"--- Begin report of {book_file} ---")
    print(f"{word_count} words found in the document")
    print("")
    for i in letter_count:
        print(f"The '{i['letter']}' character was found {i['count']} times")
    print("--- End report ---")

def count_words(file_contents):
    list_words = file_contents.split()
    return len(list_words)

main()

