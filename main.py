

def main():
    # grabs the text from frankenstein.txt
    with open('books/Frankenstein.txt') as f:
        file_contents = f.read()
        character_dict = character_count(file_contents)
        dict_list = transform_dict(character_dict)
        dict_list.sort(reverse=True, key=sort_on)
        
        # prints report of the total word count, and how many times each alphabetical character appears
        print('--- Begin report of books/frankenstein.txt ---')
        print(f'{word_count(file_contents)} words found in the document\n')

        for char in dict_list:
            print(f"The '{char['char']}' character was found {char['count']} times")

        print('--- End Report ---')


# counts the number of words in the given file    
def word_count(file_contents):
    counter = 0
    words = file_contents.split()
    
    for word in words:
        counter += 1
    
    return counter

# counts the number of times each character appears in the given file
def character_count(file_contents):
    char_counts = {}
    lowercase = file_contents.lower()

    for char in list(lowercase):
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

# sorting key
def sort_on(dict):
    return dict['count']


# dictionary conversion
def transform_dict(dict):
    dict_list = []
    for char, count in dict.items():
        if char.isalpha():
            dict_list.append({'char': char, 'count': count})
    return dict_list

main()


