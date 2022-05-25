import os
os.chdir("classXII\snippets")
while os.getcwd()[-6::] != "GIT_IT": 
    print(os.getcwd()[0:len(os.getcwd()) - os.getcwd()[::-1].index("\\") - 1])
    os.chdir(os.getcwd()[0:len(os.getcwd()) - os.getcwd()[::-1].index("\\") - 1])
print(os.getcwd())






#function to go back n directories, and then return the working directory
def goBackDirectory(times):
    for _ in times:
        os.chdir(os.getcwd()[0:len(os.getcwd()) - os.getcwd()[::-1].index("\\") - 1])
    return os.getcwd
