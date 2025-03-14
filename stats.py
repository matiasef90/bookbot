def get_num_words(book: str):
    words = book.split()
    return len(words)

def get_count_characters(book):
    dic = {}
    for char in book.lower():
        if not char.isalpha():
            continue
        if not dic.get(char):
            dic[char] = 1
            continue
        dic[char] += 1
    return dic

def get_report(url_book):
    print(" BOOKBOT ".center(50, "="))
    print(f"Analyzing book found at {url_book}...")
    with open(url_book) as f:
        book = f.read()
    print(" Word Count ".center(50, "-"))
    print(f"Found {get_num_words(book)} total words")
    print(" Character Count ".center(50, "-"))
    num_chars = get_count_characters(book)
    num_chars = sorted(num_chars.items(), key = lambda item: item[1], reverse= True)
    for key, val in num_chars:
        print(f"{key}: {val}")
    print(" END ".center(50, "="))
    
    