from abc import ABC, abstractmethod


class FileSystemElement(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display(self, indent=0):
        pass

    @abstractmethod
    def get_size(self):
        pass


class File(FileSystemElement):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def display(self, indent=0):
        print(' ' * indent + f"📄 {self.name} ({self.size} bytes)")

    def get_size(self):
        return self.size


class Directory(FileSystemElement):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, element):
        self.children.append(element)
        return self

    def display(self, indent=0):
        print(' ' * indent + f"📁 {self.name}/")
        for child in self.children:
            child.display(indent + 4)

    def get_size(self):
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size


def main():
    root = Directory("root")
    home = Directory("home")
    user = Directory("user")

    file1 = File("file1.txt", 100)
    file2 = File("file2.txt", 200)
    file3 = File("file3.txt", 300)

    root.add(home)
    home.add(user)
    user.add(file1)
    user.add(file2)
    root.add(file3)

    root.display()
    print(f"\nTotal size: {root.get_size()} bytes")


if __name__ == "__main__":
    main()
