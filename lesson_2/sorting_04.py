def year_sort(book):
    return int(book['published'])

    
    



books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

print(sorted(books, key=year_sort))


# books.sort(key=year_sort(books))
# print(bo


# sorted_books = sorted(books, key=year_sort(books))
# print(sorted_books)