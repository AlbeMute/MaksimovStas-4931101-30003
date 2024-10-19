# TODO Найдите количество книг, которое можно разместить на дискете
diskette_size_mb = 1.44
pages = 100
number_of_lines = 50
number_of_chars = 25
bytes_per_char = 4

converting_mb_to_bytes = 1024 * 1024
diskette_size_bytes = diskette_size_mb * converting_mb_to_bytes
book_size = pages * number_of_lines * number_of_chars * bytes_per_char
number_of_books = diskette_size_bytes // book_size
print("Количество книг, помещающихся на дискету:", int(number_of_books))
