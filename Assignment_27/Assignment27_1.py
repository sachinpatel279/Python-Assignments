class BookStore:
    NoOfBooks = 0

    def __init__(self,bookname,bookauthor):
        self.Name = bookname
        self.Author = bookauthor

        BookStore.NoOfBooks = BookStore.NoOfBooks + 1
    
    def Display(self):
        print(self.Name, " by ", self.Author,".","No of books : ",BookStore.NoOfBooks)

obj1 = BookStore("Linux System Programming","Robert Love")
obj1.Display()

obj2 = BookStore("C Programming","Dennis Ritchie")
obj2.Display()    

