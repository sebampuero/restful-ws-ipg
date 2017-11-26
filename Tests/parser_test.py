role = "mbh"
name = "Derdack gmbh"



def is_role_in_name(role, name):
    try:
        index = name.index(role)
        if name[index-1] == " ":
            print("yes")
    except:
        print("fail")


is_role_in_name(role, name)
