#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/30-abstract-classes
# Difficulty: Easy

from abc import ABCMeta, abstractmethod

class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

class MyBook(Book) :
    def __init__(self, title, author, price) :
        """
        Initializes a book

        :param title: title of book
        :type title: string
        :param author: author of book
        :type author: string
        :param price: price of book
        :type price: int
        """
        super().__init__(title, author)
        self.price = price
    def display(self) :
        print("Title: " + self.title)
        print("Author: " + self.author)
        print("Price: " + str(self.price))

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
