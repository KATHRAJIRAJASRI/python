#
string="TeCHNOlogicalUNIversiTY"
vowel_set=[]
consonant_set=[]
vowels="AEIOU"
string=string.upper()
for i in string:
    if i in vowels:
       vowel_set.append(i)
    else:
        consonant_set.append(i)
print("There are",len(vowel_set),"vowels in a given  string")
print("There are",len(consonant_set),"consonant in a given  string")
#
string=" rajasri "
print(string.upper())
print(string.lower())
print(string.strip())
print(string.lstrip())
print(string.rstrip())
print(string.replace("r","R"))
print(string.startswith("R"))
print(string.endswith(" "))
print(string.find("i"))
print(string.count("a"))
print(string.title())
print(string.capitalize())





