def reverse(word):
    my_list = list(word)
    my_list.reverse()
    reverse_string = ''.join(my_list)
    return reverse_string
def elaborate(word_list, word):
    reversed = reverse(word)
    word_list = word_list.insert(0, word)
    word_list.append(reversed)  
def main():
    words = []
    word = input('Enter a word >')
    while word != 'stop':
        elaborate(words, word)
        word = input('Enter a word >')
    print(words)
main()