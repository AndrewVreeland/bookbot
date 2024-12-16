def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        counting_words(file_contents)
    try:
        number_of_characters(file_contents)
        counting_words(file_contents)
    except Exception as e:
        print(f"An error has occured {e}")


def sort_on(dict_input):
    return dict_input["total"]

def sorted_values(dict_input):
    char_list = []
    for char, count in dict_input.items():
        char_list.append({"char":char, "total": count})

    char_list.sort(reverse = True, key=sort_on)

    for item in char_list:
        # print(item)
        pass
    

def counting_words(file_contents):
    num_of_words = len(file_contents.split())
    if num_of_words> 0:
        return num_of_words
    raise Exception ("must not be a non empty txt file")

def number_of_characters(file_contents):
    lowercase_string = file_contents.lower()
    characters = {}
    unwanted_characters = [",", "!", "#", "$", "%","^","&","*","(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "\'", "\"", "<",".", ">","?", " ", "1", "2", "3", "4", "5" ,"6", "7", "8" ,"9", "0", "@", "/", "\n" ]

    for character in lowercase_string:
        # Skip unwanted characters
        if character in unwanted_characters:
            continue
        # Count the character

        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
            
    sorted_values(characters)
    print(characters)







main()