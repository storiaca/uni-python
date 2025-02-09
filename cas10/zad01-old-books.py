'''
1. Old Books
Annie goes to her hometown after a very long period out of the country. After coming home, she sees her grandmother's old library and remembers her favorite book. Help Annie by writing a program in which she enters the book (string) she is looking for. Until Annie finds her favorite book or checks out all the books in the library, the program must read the name of each following book (string). The books in the library are finished once you get the text "No More Books".
If she does not find the book, print in two lines: 
    • "The book you search is not here!"
    • "You checked {count} books."
If she finds the book, print on a single line:
        ◦ "You checked {count} books and found it." 
'''
book_name = input()

counter = 0
book_found = False
current_book = input()

while current_book != 'No More Books':
    if current_book == book_name:
        book_found = True
        print(f"You checked {counter} books and found it.")
        break
    counter += 1
    current_book = input()
if not book_found:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")