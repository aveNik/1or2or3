# In computer science classes, we haven't taught try & except yet, but my knowledge is much greater than that of my classmates))
# (We have just started learning if/elif/else)


#welcome
print("Maded by tiny_mauss (and without AI)")
print("-------------------")
print(" ")

def main():
  
  #input
  a=input("First number: ")
  b=input("Second number: ")
  c=input("Third number: ")
  
  #IDK what write here xD


  try:
    
    #-i suffix mean "int"
    ai=int(a)
    bi=int(b)
    ci=int(c)

    
    #a=b=c
    if ai==bi and bi==ci:
      print("All numbers are equal")
      
    #a==b!==c or a!=b==c
    elif ai==bi or bi==ci or ai==ci:
      print("only two numbers are equal")
      
    #a!=b!=c
    else:
      print("All numbers are different")
      
  #if input is not a number    
  except ValueError:
    print("Error: one or all numbers you input is NaN")
    #restart
    main()

main()

#bye!
print(" ")
print("thanks for using")
