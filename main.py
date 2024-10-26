print('Hello World!')


class Student:
    First_name: "Олег"
    Last_name: "Александрович"
    Count_homeworks: '3'

    def __init__(self, First_name, Last_name, count_homeworks, isAvailable=True):
        self.First_name = First_name
        self.Last_name = Last_name
        self.Count_homeworks = 3
        self.isAvailable = isAvailable

