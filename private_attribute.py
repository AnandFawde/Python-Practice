class passs:
    __name = "SOPPY"      # " __ " makes data unacceceble outside the class

    def __helo(self):
        print("Hello")

    def welcome(self):
        self.__helo()      # indirect method to call private attribute & method
                           # from outside

s1 = passs()

# print(s1.__name)
# print(s1.__helo())
s1.welcome()

