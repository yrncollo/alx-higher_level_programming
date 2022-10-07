#!/usr/bin/python3
"""This module supplies one class, Base"""

import json
import csv
import turtle


class Base:
    """Structure of the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialiases an instance of Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        listob = []
        if list_objs is not None:
            for i in list_objs:
                listob.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(listob))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        list_inst = []
        try:
            with open(filename, 'r') as f:
                list_inst = cls.from_json_string(f.read())
            for i, v in enumerate(list_inst):
                list_inst[i] = cls.create(**list_inst[i])
        except Exception:
            pass
        return list_inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes a list of Rectangles or Squares to csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            csv_writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for i in list_objs:
                    csv_writer.writerow([i.id, i.width, i.height, i.x, i.y])
            elif cls.__name__ == "Square":
                for i in list_objs:
                    csv_writer.writerow([i.id, i.size, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a list of Rectangles or Squares from csv"""
        filename = cls.__name__ + ".csv"
        list_inst = []
        try:
            with open(filename, 'r') as f:
                csv_reader = csv.reader(f)
                for args in csv_reader:
                    if cls.__name__ == "Rectangle":
                        dic = {"id": int(args[0]),
                               "width": int(args[1]),
                               "height": int(args[2]),
                               "x": int(args[3]),
                               "y": int(args[4])}
                    elif cls.__name__ == "Square":
                        dic = {"id": int(args[0]),
                               "size": int(args[1]),
                               "x": int(args[2]),
                               "y": int(args[3])}
                    obj = cls.create(**dic)
                    list_inst.append(obj)
        except Exception:
            pass
        return list_inst

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        screen_width = 620
        padding = 10
        row_width = padding
        row_height = 0
        screen_height = padding
        color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo',
                      'violet']
        color_size = len(color_list)
        color_index = 0
        for rect in list_rectangles:
            potential_width = row_width + rect.width + rect.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += rect.width + rect.x + padding
                if (row_height < rect.height + rect.y):
                    row_height = rect.height + rect.y
            else:
                screen_height += row_height + padding
                row_width = rect.width + rect.x + padding * 2
                row_height = rect.height + rect.y

        for square in list_squares:
            potential_width = row_width + square.size + square.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += square.size + square.x + padding
                if (row_height < square.size + square.y):
                    row_height = square.size + square.y
            else:
                screen_height += row_height + padding
                row_width = square.size + square.x + padding * 2
                row_height = square.size + square.y

        turtle.screensize(canvwidth=screen_width, canvheight=screen_height)
        turtle.pu()
        turtle.left(180)
        turtle.forward(screen_width/2 - padding)
        turtle.right(90)
        turtle.forward(screen_height/2 - padding)
        turtle.right(90)
        row_width = padding
        row_height = 0
        for rect in list_rectangles:
            potential_width = row_width + rect.width + rect.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += rect.width + rect.x + padding
                if (row_height < rect.height + rect.y):
                    row_height = rect.height + rect.y
            else:
                turtle.pu()
                turtle.left(180)
                turtle.forward(row_width - padding)
                turtle.left(90)
                turtle.forward(row_height + padding)
                turtle.left(90)
                row_width = rect.width + rect.x + padding * 2
                row_height = rect.height + rect.y
            turtle.pd()
            turtle.pencolor(color_list[color_index % color_size])
            for _ in range(4):
                turtle.forward(5)
                turtle.back(5)
                turtle.right(90)
            turtle.pu()
            turtle.forward(rect.x)
            turtle.right(90)
            turtle.forward(rect.y)
            turtle.left(90)
            turtle.pd()
            turtle.pencolor('black')
            turtle.fillcolor(color_list[color_index % color_size])
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.right(90)
                turtle.forward(rect.height)
                turtle.right(90)
            turtle.end_fill()
            color_index += 1
            turtle.pu()
            turtle.forward(rect.width + padding)
            turtle.left(90)
            turtle.forward(rect.y)
            turtle.right(90)

        for square in list_squares:
            potential_width = row_width + square.size + square.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += square.size + square.x + padding
                if (row_height < square.size):
                    row_height = square.size + square.y
            else:
                turtle.pu()
                turtle.left(180)
                turtle.forward(row_width - padding)
                turtle.left(90)
                turtle.forward(row_height + padding)
                turtle.left(90)
                row_width = square.size + square.x + padding * 2
                row_height = square.size + square.y
            turtle.pd()
            turtle.pencolor(color_list[color_index % color_size])
            for _ in range(4):
                turtle.forward(5)
                turtle.back(5)
                turtle.right(90)
            turtle.pu()
            turtle.forward(square.x)
            turtle.right(90)
            turtle.forward(square.y)
            turtle.left(90)
            turtle.pd()
            turtle.pencolor('black')
            turtle.fillcolor(color_list[color_index % color_size])
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)
            turtle.end_fill()
            color_index += 1
            turtle.pu()
            turtle.forward(square.size + padding)
            turtle.left(90)
            turtle.forward(square.y)
            turtle.right(90)

        turtle.getscreen()._root.mainloop()
