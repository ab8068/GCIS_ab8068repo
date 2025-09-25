#string seperation with split white space
a_string = "S 11 2 3 R"
tokens = a_string.split(" ")
print(tokens[1])
for i in tokens:
    print(i)