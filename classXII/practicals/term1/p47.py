#17-07-2022
import sd  #ignore, this is my personal dependency, does not affect code


#goal: take data from first file, make the entire file have capital letters at beginning of sentence, then put into new file

# f1 = open("p47a.txt", 'r')
# f2 = open('p47b.txt', 'w')
# for line in f1.readlines():
#     stringout = "" #Will write to this string
#     seenEOL = True #checks if it has seen a full stop
    
#     for char in line.strip('\n').strip(' '): #removes white spaces as well as newlines
#         if seenEOL == True and char.isalpha(): # If Full stop was seen before
#             stringout+=char.upper() #uppercases the first character it sees and changes the seen condition
#             seenEOL= False
#         else:
#             stringout+=char #just adds the string


#         #checks for full stop
#         if char==".":
#             seenEOL = True #changes the seen condition to true

#     f2.write(stringout+"\n") #we add newline, because we removed it during the stripping
# f1.close()
# f2.close()       



with open("p47a.txt", 'r') as f1:
    with open("p47b.txt", 'w') as f2:
        for line in f1.readlines():
            stringout , seenEOL = "" , False
            for char in line.strip('\n').strip(' '):
                if seenEOL == True and char.isalpha(): stringout+=char.upper() ; seenEOL=False
                else: stringout+=char
                if char==".":seenEOL=True
            f2.write(stringout+"\n")



            
