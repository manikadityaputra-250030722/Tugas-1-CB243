"""Entry point untuk Studi Kasus 2"""
from models import Author, Book, LibraryMember

def main():
    author = Author('Deva Anjasmara', 1925)
    book = Book(item_id=1, title='Teori Bahlilisme', isbn='978-602-00-1972', author=author)

    book.display_info()
    print('Umur Author pada 2025:', author.get_age(2025))
    print('Denda keterlambatan 3 hari:', book.calculate_late_fee(3))

    member = LibraryMember(member_id=101, name='Siti')
    member.borrow_item(book)
    print('Jumlah item yang dipinjam:', len(member.borrowed_items))
    member.return_item(book)
    print('Jumlah item setelah dikembalikan:', len(member.borrowed_items))

if __name__ == '__main__':
    main()