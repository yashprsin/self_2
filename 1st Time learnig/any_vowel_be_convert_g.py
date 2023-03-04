def translate(String):
    translation = ""

    for latter in String:
        if latter.lower() in "aeiou":
            if latter.upper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + latter

    return translation

print(translate(input("Enter the String  : ")))



