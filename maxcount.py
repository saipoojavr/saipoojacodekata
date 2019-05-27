word=input()
list1=list(word)
dict = {iter:list1.count(iter) for iter in list1}
large = max(dict, key=dict.get)  
print(large)