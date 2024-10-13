def count_chars(text):
    counts = {}
    for char in text:
        char = char.lower()
        if not char.isalpha():
            continue

        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts

def count_words(text):
    return len(text.split())

def print_report(path_to_book):
    print(f'--- Begin report of {path_to_book} ---')
    with open(path_to_book,'r') as inf:
        text = inf.read()

    num_words = count_words(text)
    print(f'{num_words} words found in the document')
    print('')

    num_chars = count_chars(text)
    char_list = []
    for char,count in num_chars.items():
        char_list.append({"char":char, "count":count})
    char_list.sort(reverse=True, key=sort_on)

    for entry in char_list:
        char = entry["char"]
        count = entry["count"]
        print(f"The '{char}' character was found {count} times")
    
    print('--- End report ---')

def sort_on(dict):
    return dict["count"]

def main():
    book = 'books/frankenstein.txt'
    print_report(book)

if __name__ == '__main__':
    main()
