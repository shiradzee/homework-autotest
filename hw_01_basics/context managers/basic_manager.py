class FileWriter:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file is not None:
           self.file.close()
        if exc_val is not None:
            print(f"Произошла ошибка: {exc_val}")
        else:
            print("Запись завершена")

with FileWriter('example.txt') as file:
    file.write("Hello, World!")
