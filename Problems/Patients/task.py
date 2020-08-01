class Patient:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    # create methods here
    def __repr__(self):
        return "Object of the class {}. name: {}, last_name: {}, age: {}".format(self.__class__.__name__, self.name,
                                                                                 self.last_name, str(self.age))

    def __str__(self):
        return f"{self.name} {self.last_name}. {str(self.age)}"


