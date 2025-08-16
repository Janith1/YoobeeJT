class Read_File:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        open_file = open(self.filename, 'r', encoding='utf-8')
        file_content = open_file.read()
        open_file.close()
        return file_content

    def write_file(self, file_content):
        open_file = open(self.filename, 'w', encoding='utf-8')
        open_file.write(file_content)
        open_file.close()

def main():
    reader = Read_File("Read2.txt")

    file_content = reader.read_file()
    print(f"\nFile Content is as below \n{file_content}")

    reader.write_file("Newly added text to the file")

    file_content = reader.read_file()
    print(f"\nNew File Content is as below \n{file_content}")


if __name__ == '__main__':
    main()