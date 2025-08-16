class Read_File:
    def __init__(self, filename):
        self.filename = filename

    def count_words(self):
        open_file = open(self.filename, 'r', encoding='utf-8')
        file_content = open_file.read()
        return len(file_content.split())

def main():
    reader = Read_File("Read.txt")

    word_count = reader.count_words()
    print(f"\nWord count of TXT file: {word_count}")


if __name__ == '__main__':
    main()