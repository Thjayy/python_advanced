class Openfile:
    def __init__(self, filename, mode) -> None:
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with Openfile("simple.txt", "w") as file:
    file.write("Hello world")

# file = open("simple.txt", "w")
# file.write("Hello world")
    

