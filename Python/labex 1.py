#paragraph
paragraph ="""myself pavan kumar from bangalore and im studying mca at christ and my reg no is 2347243 and my domain name is tourism"""
print(paragraph)
print("\n")

#frequency of specific word
def count_word_frequency(paragraph, word):
    
    words = paragraph.lower().split()
    word_frequency = words.count(word.lower())
    return word_frequency



# Sample paragraph for testing
paragraph = """Your paragraph goes here.My name is pavan of mca for the year 2023 with the reg no: 2347243 and my domain is tourism"""

specific_word = "tourism"

frequency = count_word_frequency(paragraph, specific_word)
print(f"The word '{specific_word}' appears {frequency} times in the paragraph.")
print("\n")



#display data types
paragraph = """Your paragraph goes here.My name is pavan of mca for the year 2023 with the reg no: 2347243 and my domain is tourism"""
for n in paragraph:
    if n.isdigit():
        data_type = "int"
    elif n.replace(',','').isdigit():
        data_type = "float"
    elif n.lower() == "true" or n.lower() == "false":
        if n[1:4].islower() and n[0].isupper():
            data_type = "bool"
        else:
            data_type="str"
    elif n.isalpha():
        data_type="str"
    else:
        data_type="special character"
    print("word- ",n,"\t","|| data type- ",data_type)
print("\n")



    #count alphabets
def count_symbols(paragraph):
    alphabets = 0
    numerics = 0
    special_symbols = 0

    for char in paragraph:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            numerics += 1
        else:
            special_symbols += 1

    return alphabets, numerics, special_symbols

# Sample paragraph for testing
paragraph = """Your paragraph goes here.My name is pavan of mca for the year 2023 with the reg no: 2347243 and my domain is tourism"""

# Calculate the counts of alphabets, numeric characters, and special symbols in the paragraph
alpha_count, numeric_count, special_count = count_symbols(paragraph)

# Display the results
print("Number of Alphabets: ", alpha_count)
print("Number of Numeric Characters: ", numeric_count)
print("Number of Special Symbols: ", special_count)
print("\n")



#set functions
def opration():
    data = {1, 3.14, "hello", True, None}
    popped = data.pop()
    data.clear()
    print(data)
    del data
    return popped

popped = opration()
print("Popped element:", popped)
print("\n")



#set in descending order
domain = {'tourist','destination','package','travel'}
result = sorted(domain, reverse=True)
print(result)
print("\n")


#create tuple and packing and unpacking
tourist = ('pavan','24','developer')
name,age,position = tourist
print(f"Name: {name}")
print(f"Age: {age}")
print(f"position: {position}")
print("\n")



#domain name as character and count
chart = ['t','o','u','r','i','s','m']
target ='i'
count = chart.count(target)
print(f"count of '{target}':{count} ")
print("\n")



#python code to execute all the slicing possibilities and also negative indexing
entities = ["tourist","destination","transport","cafes","events"]
print(entities[:3])
print(entities[2:])
print(entities[2:4])

print(entities[-1])
print(entities[-2:])
print(entities[-4:-1])
print("\n")
