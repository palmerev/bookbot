from collections import Counter

def main():
    file_path = 'books/frankenstein.txt'
    with open(file_path) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_counts = count_letters_characters(file_contents)
        char_count_list = [
            {"letter": letter, "count": n} for letter,n in char_counts.items() if letter.isalpha()]
        char_count_list.sort(key=lambda d: d['count'], reverse=True)
        print(f'-- Report on -- {file_path}')
        print(f'The book contains {word_count} words.')
        for entry in char_count_list:
            letter, count = entry['letter'], entry['count']
            print(f'The character "{letter}" was found {count} times.')
        print(f'-- End report --')
        
        


def count_words(contents: str):
    # word count
        words = contents.split()
        word_count = len(words)
        return word_count
        

def count_letters_characters(contents: str):
    # count unique lowercase characters, letters, punctuation, whitespace, etc.
    char_counter = Counter(contents.lower())
    return char_counter
     

if __name__ == '__main__':
    main()