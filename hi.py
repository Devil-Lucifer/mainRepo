print('hi')

#fork pracctice
print('just added an print statement \U0001F600')


#function to  add string into list...
def new_list(sentence):
    
    newlist=list(sentence)
    newlist += [sentence]
    
    return newlist

print(new_list("hello"))
