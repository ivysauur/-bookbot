def get_book_text(path_to_file):
        with open(path_to_file) as f:
                file_contents = f.read()
        return file_contents
#get book text
def get_num_words(book):
        words = book.split()
        num_words=len(words)
        return num_words
#get count of words
def letter_count(book):
	lower_words=book.lower()
	letter_dic={}
	for letters in lower_words:
		if letters in letter_dic:
			letter_dic[letters]+=1
		else:
			letter_dic[letters]=1
	return letter_dic
