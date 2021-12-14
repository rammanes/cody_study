import tkinter as tk

from oop import BinarySearch


class BinarySearchEvent(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('400x400')
        self.title("Binary Search")
        label = tk.Label(self, text = "Enter an item")
        label.grid(row = 0, column = 0)
        label2 = tk.Label(self, text="Enter a search item")
        label2.grid(row=1, column=0)
        BinarySearchEvent.first_entry = tk.Entry(self, width = 20)
        BinarySearchEvent.first_entry.grid(row = 1, column = 1)
        BinarySearchEvent.search_entry = tk.Entry(self, width=20)
        BinarySearchEvent.search_entry.grid(row=0, column=1)
        add_button = tk.Button(self, text = "add", command = add_item)
        add_button.grid(row = 2, column = 0)
        add_button = tk.Button(self, text="search", command=search_item)
        add_button.grid(row=2, column=1)


items = []


def add_item():
    list_item = BinarySearchEvent.first_entry.get()
    items.append(int(list_item))
    print(items)


def search_item():
    element = BinarySearchEvent.search_entry.get()
    print(items)
    bsearch = BinarySearch(items)
    result = bsearch.binary_search(int(element))
    if result != -1:
        print("Element is present at index " + str(result))
    else:
        print("Not found")


bs = BinarySearchEvent()
bs.mainloop()