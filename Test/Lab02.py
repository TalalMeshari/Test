"""
#Q2:
done = False
loops = 5
for x in range(1,10):#run 5 times 1 2 3 4 5 ... last number is excluded if the first number is 0 then the loop will not run.
    if done == False:
        for y in range(1,x+1):
          print("*",end=" ")#use ,end=" " to make it print on 1 line
          if (x+1) == 6:
              done = True
    else:
        #print(loops)
        for y in range(1,loops):
            print("*",end=" ")
        loops -=1
    print()#this to create a new line after the above loop ends.
    """


    #Q1:
    #endswith()
    #rfind()

    #rsplit()
allStrs = str(input("Enter all the strings that you want all in one line:"))

print(allStrs)

strList = allStrs.rsplit(" ")

print(strList)
print("second commit")