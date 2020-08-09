ignore = input("Enter words to be ignored seperated by commas: ")
title = input("Enter a title to generate its acronym: ")

ignore = ignore.upper()
title = title.upper()

ignore_split = ignore.strip(", ")

for word in ignore_split:
  if word in title:
    title = title.strip(word)
    
title = title.strip(" ")

title_split = title.split(' ')

acronym1 = ""
for i in title_split:
  acronym1 = acronym1 + i[0]

#acronym = ""
#for x in acronym1:
  #acronym = acronym + x[0]

print("The acronym is "+ acronym1)  