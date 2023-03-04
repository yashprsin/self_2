friend_name = open("Friend.txt", "r")


for friend in friend_name.readlines():
    print(friend)
friend_name.close()

html_file = open("HTML.html", "w")

html_file.write("</p> index of html </p>")