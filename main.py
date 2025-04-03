from stats import get_book_text, get_num_words, letter_count

def main():
	text = get_book_text("books/frankenstein.txt")
	
	num_words = get_num_words (text)
	print(f"{num_words} words found in the document")

	char_count = letter_count(text)
	print(char_count)
	

if __name__ == "__main__":
	main()



