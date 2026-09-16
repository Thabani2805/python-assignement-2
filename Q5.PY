from abc import ABC, abstractmethod

# Abstract class
class FileHandler(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


# Concrete class for text files
class TextFileHandler(FileHandler):

    def read(self):
        print("Reading text file")

    def write(self, data):
        print("Writing text:", data)


# Concrete class for binary files
class BinaryFileHandler(FileHandler):

    def read(self):
        print("Reading binary file")

    def write(self, data):
        print("Writing binary data:", data)


# Create objects
text_file = TextFileHandler()
binary_file = BinaryFileHandler()

# Use the methods
text_file.read()
text_file.write("Hello World")

binary_file.read()
binary_file.write("101010")