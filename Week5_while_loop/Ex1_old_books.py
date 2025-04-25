NO_MORE_BOOKS_COMMAND = 'No More Books'
checked_books = 0
target_book = input()

command = input()
while not command == NO_MORE_BOOKS_COMMAND:
    current_book = command
    if current_book == target_book:
        print(f'You checked {checked_books} books and found it.')
        break

    checked_books += 1
    command = input()
else:
    print('The book you search is not here!')
    print(f'You checked {checked_books} books.')
