def count_words(filename):
    '''Count the approximate number of words in the file.'''
    try: 
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f'The file {filename} has apporximately {num_words} words in the file.')

 filename = 'text_files/alice.txt'
 count_words(filename)