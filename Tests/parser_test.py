from Service.Parser import get_firmen_JSON
import json

name = "TH"
branche = ""
ort = "wildau"
rolle = ""

pre_string = "{\"json\":{\"firma\":"
post_string = "}}"

list = pre_string + get_firmen_JSON(name, branche, ort, rolle) + post_string

print(list)