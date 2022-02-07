from mimetypes import init
from unicodedata import name


class User:
    def __init__(self, name, location, courseCodes):
        self.name = name
        self.location = location
        self.courseCodes = courseCodes

    def getUserInfo(self):
        course_str = ""
        if type(self.courseCodes) == list:
            for elem in self.courseCodes:
                course_str = str(elem) + ", " + course_str
        else:
            course_str = self.courseCodes
        print(
            f"The user name is: {self.name} and is from {self.location}. The user wants to register for {course_str}")
