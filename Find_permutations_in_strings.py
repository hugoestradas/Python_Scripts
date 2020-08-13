char_lenght = 26
  
def factorial(n) : 
      
    fact = 1; 
    for i in range(2, n + 1) : 
        fact = fact * i; 
    return fact 
        
def countPerms(st) : 
      
    length = len(st) 
    freq = [0] * char_lenght 
      
    for i in range(0, length) : 
        if (st[i] >= 'a') : 
            freq[(ord)(st[i]) - 97] = freq[(ord)(st[i]) - 97] + 1; 
    
    fact = 1
    for i in range(0, char_lenght) : 
        fact = fact * factorial(freq[i]) 
    
    return factorial(length) / fact 
  
word = "HugoEstrada"
print (countPerms(word))
