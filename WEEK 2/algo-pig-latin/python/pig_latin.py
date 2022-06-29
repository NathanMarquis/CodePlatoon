def translate(word_or_phrase):
  word_list = word_or_phrase.split()
  piggified_list = []

  def piggy_word_converter(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

    if word[0] in vowels:
      pig_arr = list(word)
      pig_arr.append('ay')
      pig_word = ''.join(pig_arr)
      return pig_word

    elif word[0] in consonants:
      pig_arr = list(word)
      pig_arr.append(pig_arr.pop(0))
      pig_arr.append('ay')
      pig_word = ''.join(pig_arr)
      return pig_word

  for word in word_list:
    piggified_list.append(piggy_word_converter(word))
  
    print (' '.join(piggified_list))
    return ' '.join(piggified_list)

# translate('you are cool guy')