role = "ag"
name = "agentur Deutsche Akademie ag & co."


def is_role_in_name(role, name):
    try:
        index = name.index(role,len(name)-len(role))
        if (name[index - 1] == " ") and ((index + len(role)) % len(name) == 0):
            print("yes")
    except:
        print("fail")


is_role_in_name(role, name)
