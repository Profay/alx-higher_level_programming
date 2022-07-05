#!/usr/bin/python3

def writing(text=""):
    with open("txt.txt", mode='w', encoding='utf-8') as file:
        return file.write(text)


print(writing("I am going to school"))