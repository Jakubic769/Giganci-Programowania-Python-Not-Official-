class HelloWorld:
    def __init__(self, a):
        self.a = a

    def print_message(self):
        print(self.a)



obj = HelloWorld("Print")
obj.print_message()