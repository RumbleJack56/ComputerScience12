d1={'a':90,'b':80}
d2={'c':70,'d':60}
d3={'e':50,'f':40}
print(d1,d2,d3,sep="\n")
for d in (d2,d3): d1.update(d)
print(d1)
