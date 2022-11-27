lyric = ["I'm trying to hold my breath",
          "Let it stay this way",
          "Can't let this moment end",
          "You set off a dream with me",
          "Getting louder now",
          "Can you hear it echoing?",
          "Take my hand",
          "Will you share this with me?",
          "'Cause darling without you",
          "All the shine of a thousand spotlights",
          "All the stars we steal from the nightsky",
          "Will never be enough",
          "Never be enough",
          "Towers of gold are still too little",
          "These hands could hold the world but it'll",
          "Never be enough", "For me",
          "Never, never", "Never, for me",
          "Never enough", "For me"]

for i in [-6, -4, -2, -2, -1, -1, -1]:lyric.insert(i, lyric[i])
print(' --- << Never Enough 2 >> --- ')
for verse in lyric:print(verse, end='\n')
lyric_to_words = [(w.rstrip(',').rstrip('?'))for verse in lyric for w in verse.split(" ")]
word_count_dic = {word:lyric_to_words.count(word)for word in set(lyric_to_words)}
word_sorted = sorted(word_count_dic.keys())
value_sorted = [word_count_dic[word]for word in word_sorted]
print("\n\n --- <<  Word-Counting the lyric of Never Enough >> --- ")
for i  in range(len(value_sorted)):print(str(word_sorted[i]).ljust(10),str(value_sorted[i]).rjust(15))