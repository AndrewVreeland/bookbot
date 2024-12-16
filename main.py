def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        counting_words(file_contents)
    try:
        number_of_characters(file_contents)
        counting_words(file_contents)
    except Exception as e:
        print(f"An error has occured {e}")


def counting_words(file_contents):
    num_of_words = len(file_contents.split())
    if num_of_words> 0:
        return num_of_words
    raise Exception ("must not be a non empty txt file")

def number_of_characters(file_contents):
    lowercase_string = file_contents.lower()
    char = {}
    total = 1

    try:
        for i in range(len(lowercase_string.split())):
            if lowercase_string[i] not in char:
                char[lowercase_string[i]] = total 

            else:
                total = char[lowercase_string[i]]
                total += 1
                char[lowercase_string[i]] = total
                total = 1
    except Exception as e:
        print(f"An error has occured {e}")
    print(char)





main()