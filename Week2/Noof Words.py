class StringManipulator:
    def __init__(self, text):
        self.text = text

    def no_of_words(self):
        return len(self.text.split())

def main():
    # Create an instance of the StringManipulator class
    sentence = input("Please enter a sentence to count the words : ")
    name = StringManipulator(sentence)

    # Call the find_character method
    result = name.no_of_words()
    print("No of word count is ", result)  # Output: 1

if __name__ == "__main__":
    main()
