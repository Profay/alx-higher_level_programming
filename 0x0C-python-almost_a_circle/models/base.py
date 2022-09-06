#!/usr/bin/python3
"""Modules for class base
It takes a private instance object
"""
import json
import csv


class Base:
    """Declaring the base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Defining the class constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ dictionary to json string
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string to file
        """
        if list_objs is not None:
            list_objs = [objects.to_dictionary() for objects in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ JSON string to dictionary
        """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """  Dictionary to Instance
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            dummy = Rectangle(1, 1)
        elif cls is Square:
            dummy = Square(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ File to instances
        """
        file_name = "{}.json".format(cls.__name__)
        if not file_name:
            return []
        else:
            with open(file_name, "r", encoding="utf-8") as f:
                return [cls.create(**instances) for instances
                        in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Saves json object to csv file
        """
        from models.rectangle import Rectangle
        from models.square import Square

        file_name = "{}.csv".format(cls.__name__)
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open(file_name, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """ Loads from json object
        """
        from models.rectangle import Rectangle
        from models.square import Square

        ret = []
        with open('{}.csv'.format(cls.__name__), "r", newline="",
                  encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                ret.append(cls.create(**d))
        return ret

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Opens a window and draws all the Rectangles and Squares
        """
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            t.pensize(10)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)
