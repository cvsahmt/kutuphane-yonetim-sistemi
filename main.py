# ==============================
# KÜTÜPHANE KİTAP ARAMA SİSTEMİ
# Konsol (CLI) Arayüzlü - OOP
# ==============================

class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __str__(self):
        return f"Kitap Adı: {self.name} | Yazar: {self.author} | Yayın Yılı: {self.year}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, name, author, year):

        for book in self.books:
            if book.name.lower() == name.lower() and book.author.lower() == author.lower():
                print("\n Bu kitap zaten kütüphanede mevcut!")
                return

        book = Book(name, author, year)
        self.books.append(book)
        print("\n Kitap başarıyla eklendi.")

    def remove_book(self, name):
        for book in self.books:
            if book.name.lower() == name.lower():
                self.books.remove(book)
                print("\n Kitap başarıyla silindi.")
                return
        print("\n Kitap bulunamadı.")

    def search_by_name(self, name):
        found = False
        print("\n Arama Sonuçları:")
        for book in self.books:
            if name.lower() in book.name.lower():
                print(book)
                found = True
        if not found:
            print(" Aranan isimde kitap bulunamadı.")

    def search_by_author(self, author):
        found = False
        print("\n Arama Sonuçları:")
        for book in self.books:
            if author.lower() in book.author.lower():
                print(book)
                found = True
        if not found:
            print(" Bu yazara ait kitap bulunamadı.")

    def list_books(self):
        if not self.books:
            print("\n Kütüphanede hiç kitap yok.")
        else:
            print("\n Kütüphanedeki Kitaplar:")
            for book in self.books:
                print(book)


# ==============================
# KONSOL ARAYÜZÜ (MENÜ)
# ==============================

def menu():
    print("\n==============================")
    print("  KÜTÜPHANE YÖNETİM SİSTEMİ  ")
    print("==============================")
    print("1- Kitap Ekle")
    print("2- Kitap Sil")
    print("3- Kitap Ara (İsme Göre)")
    print("4- Kitap Ara (Yazara Göre)")
    print("5- Tüm Kitapları Listele")
    print("6- Çıkış")
    print("==============================")


def main():
    library = Library()

    while True:
        menu()
        choice = input("Seçiminiz: ")

        if choice == "1":
            name = input("Kitap adı: ")
            author = input("Yazar adı: ")
            year = input("Yayın yılı: ")
            library.add_book(name, author, year)

        elif choice == "2":
            name = input("Silinecek kitap adı: ")
            library.remove_book(name)

        elif choice == "3":
            name = input("Aranacak kitap adı: ")
            library.search_by_name(name)

        elif choice == "4":
            author = input("Aranacak yazar adı: ")
            library.search_by_author(author)

        elif choice == "5":
            library.list_books()

        elif choice == "6":
            print("\n Programdan çıkılıyor...")
            break

        else:
            print("\n Geçersiz seçim! Lütfen 1-6 arasında bir değer giriniz.")


if __name__ == "__main__":
    main()
