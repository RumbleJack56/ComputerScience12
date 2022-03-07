XI = {}
for k in range(int(input("Number of sections in Class XI: "))):
    sec = input("Enter Section: ")
    str = input("Enter Stream: ")
    XI[sec] = str
for a in XI:
    print("%-2s- %-10s"%(a,XI[a]))
