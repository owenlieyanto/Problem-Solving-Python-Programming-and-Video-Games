def magic(abra, cadabra):
  abra = abra + cadabra
  print(abra)
  confusion(abra, cadabra)
def confusion(cadabra, word1):
  confused = abra + cadabra
  print(confused)
def main():
  word1 = input('Enter a word >')
  word2 = input('Enter a word >')
  magic(word1, word2)
  print(word1, word2)
main()
