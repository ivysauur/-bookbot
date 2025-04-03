def get_book_text(path_to_file):
        with open(path_to_file) as f:
                file_contents = f.read()
        return file_contents
#get book text
def get_num_words():
        book=get_book_text("books/frankenstein.txt")
        words = book.split()
        num_words=len(words)
        print(f"{num_words} words found in the document")
#get count of words
