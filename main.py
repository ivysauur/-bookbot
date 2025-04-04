from stats import get_book_text, get_num_words, letter_count, sort_on

def main():
	text = get_book_text("books/frankenstein.txt")
	
	num_words = get_num_words (text)

	letter_dic = letter_count(text)
	letter_order = sort_on(letter_dic)
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for char_data in letter_order:
		char=char_data["char"]
		if char.isalpha():
			print(f"{char}: {char_data['count']}")
	print("============= END ===============")

if __name__ == "__main__":
	main()



