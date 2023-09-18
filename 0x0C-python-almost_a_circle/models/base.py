#!/usr/bin/python3

"""Definition of class named  base model class."""
import json
import csv
import turtle


class Base:
    """Base_model.

    This's represented the "base" for all_other
    classes in_project 0x0C*.

    Private Class_Attributes:
        __nb_object (int): is number of instantiated_Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization a new_Base.

        Argumnets:
            id (int): is the identitification of the new_Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returning the JSON_serialization of list of dictionaray.

        Argumnets:
            list_dictionaries (list): is A list of_dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writting the JSON_serialization of list of objects_to a file.

        Arguments:
            list_objs (list): is A list of inherited_Base instance.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returning the_deserialization of a JSON_string.

        Argumnets:
            json_string (str): is A JSON str_representation of list of_dicts.
        Return:
            If json_string is None or empt - an empty_list.
            else - the Python list is represented by jsonString.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returning class_instantied from a dict of attribute.

        Arguments:
            **dictionary (dict): Key/value pairs_of attributes_to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returning a list_classes instantiated of a file of JSON_strings.

        Reading of `<cls.__name__>.json`.

        Return:
            If the file doesn't exist - an empty_list.
            else - a list of instantiated_classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writting the CSV_serialization of list of_objects to file.

        Argumnets:
            list_objs (list): is  A list of inherited Base_instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returning a list of_classes instantiated of a CSV_file.

        Reading of `<cls.__name__>.csv`.

        Return:
            If the file doesn't exist - an empty_list.
            else - a list of instantiated_classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw_Rectangles and Squares_using the turtle_module.

        Argumnets:
            list_rectangles (list): is A list of Rectangle_objects to draw.
            list_squares (list): is A list of Square_objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
