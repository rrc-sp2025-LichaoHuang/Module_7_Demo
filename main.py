from developer_1.developer_1 import Person
from developer_2.developer_2 import Book
from developer_3.developer_3 import Car

def main():
    person_instance = Person("Annie", 22)
    book_instance = Book("Cat in the Hat", " Dr. Seuss") 
    print(person_instance) 
    print(book_instance) 	

if __name__ == "__main__":
    main()
