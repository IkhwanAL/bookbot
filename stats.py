def get_num_words(book: str):
    text = book.split()

    return len(text)

def counting_character(book: str):
    character_counter = dict()

    texts = book.lower()

    for char in texts:
        if char.isalpha() == False:
            continue
        
        if char not in character_counter:
            character_counter.__setitem__(char, 1)
        else:
            count = character_counter.__getitem__(char)

            character_counter.__setitem__(char, count + 1)

    return character_counter

def sort_counted_character(counted_character: dict):
   counted = list(counted_character.items())

   counted.sort(reverse=True, key=lambda item: item[1])

   return dict(counted)

def create_report(book_location, num_words, sorted_counted_character):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for k, v in sorted_counted_character.items():
        print(f"{k}: {v}")
    print("============= END ===============")