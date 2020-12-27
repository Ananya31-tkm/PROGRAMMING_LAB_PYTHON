def countX(lst, str): 
    count = 0
    for ele in lst: 
        if (ele == str): 
            count = count + 1
    return count 
  
# Driver Code 
lst = ["anu", "ammu", "anna"] 
str = 'a'
print('{} has occurred {} times'.format(str, countX(lst, str))) 
