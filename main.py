import os
pasta = "Projects/"
linguangens = {
    "Python",
    "JavaScript",
    "Java",
    "PHP",
    "Ruby",
    "HTML",
    "Lua"
    }
for linguagem in linguangens:
    print(linguagem)
    os.mkdir(pasta + linguagem)
    os.mkdir(pasta + linguagem + "/text.txt")
