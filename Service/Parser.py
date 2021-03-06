from Model.Firma import Firma, Ansprechpartner
import xml.etree.ElementTree as ET
import json
from Config.config import rollen
filename = "Data/firmendaten.xml"


# Get the list of companies according to query parameters in JSON format
# @param name the name of the company
# @param branche the department of the company
# @param ort the place of the company
# @param rolle the role the company has
# return the list of companies queried in JSON
def get_firmen_JSON(name, branche, ort, rolle):
    with open(filename, 'r') as xml_file:
        tree = ET.parse(xml_file, ET.XMLParser(encoding='utf-8'))
    root = tree.getroot()
    firmen = root.findall('firma')
    firmen_list = []
    # if the role exists
    if rolle in rollen:
        print("in role")
        for firma_element in firmen:
            name_element = firma_element.attrib['name'].lower()
            branche_element = firma_element.find('branche').text.lower()
            ort_element = firma_element.find('ort').text.lower()
            if name in name_element and branche == "" and ort == "" and is_role_in_name(rolle, name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif name in name_element and branche in branche_element and ort == "" and is_role_in_name(rolle, name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif name in name_element and branche in branche_element and ort == ort_element and is_role_in_name(rolle, name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif "" == name and branche in branche_element and ort == ort_element and is_role_in_name(rolle, name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif "" == name and branche == "" and ort == ort_element and is_role_in_name(rolle, name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif "" == name and branche in branche_element and ort == "" and is_role_in_name(rolle, name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif name in name_element and branche == "" and ort == ort_element and is_role_in_name(rolle, name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif "" == name and branche == "" and ort == "" and is_role_in_name(rolle, name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
    # if no role was desired
    elif rolle == "keine":
        print("no role")
        for firma_element in firmen:
            name_element = firma_element.attrib['name'].lower()
            branche_element = firma_element.find('branche').text.lower()
            ort_element = firma_element.find('ort').text.lower()
            if name in name_element and branche == "" and ort == "" and has_no_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif name in name_element and branche in branche_element and ort == "" and has_no_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif name in name_element and branche in branche_element and ort == ort_element and has_no_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif "" == name and branche in branche_element and ort == ort_element and has_no_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif "" == name and branche == "" and ort == ort_element and has_no_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif "" == name and branche in branche_element and ort == "" and has_no_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif name in name_element and branche == "" and ort == ort_element and has_no_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif "" == name and branche == "" and ort == "" and has_no_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
    else:  # if role was not recognized or no role was given
        return "[]"
    return json.dumps(firmen_list).replace("name", "@name")


# Check if the given company has no role
# @param firma_name the name of the company
# return true if it has no role, false otherwise
def has_no_role(firma_name):
    for role in rollen:
        if is_role_in_name(role, firma_name.strip()):
            return False
    return True


# Check if the given name has a role in it
# @param role the role to check
# @param name the name of the company
# return True if the company name has the specified role, false otherwise
def is_role_in_name(role, name):
    try:
        index = name.index(role, len(name) - len(role))  # get index of searched role from end of string
        if (name[index - 1] == " ") and ((index + len(role)) % len(name) == 0):
            return True
    except:
        try:
            index = name.index(role)  # if searched role was not found at the end of string
            if (name[index-1] == " ") and (name[index+len(role)] == " "):
                return True
        except:
            return False
    else:
        return False


# Parse the XML Elements into objects and populate the given list
# @param firma_element the XML Firma element
# @param firmen_list the list to be populated
# return the populated list
def get_firmen_list(firma_element, firmen_list):
    firma = Firma()
    firma.name = firma_element.attrib['name']
    firma.branche = firma_element.find('branche').text
    firma.strasse_hnr = firma_element.find('strasse_hnr').text
    firma.plz = firma_element.find('plz').text
    firma.ort = firma_element.find('ort').text
    firma.land = firma_element.find('land').text
    firma.website = firma_element.find('website').text
    firma.adresszusatz = "" if firma_element.find('adresszusatz') is None else firma_element.find(
        'adresszusatz').text
    firma.erfassungsdatum = firma_element.find('erfassungsdatum').text
    firma.ansprechpartner = []
    ansprechpartnern_list = firma_element.findall('ansprechpartner')

    for ansprechpartner_element in ansprechpartnern_list:
        ansprechpartner_object = Ansprechpartner()
        ansprechpartner_object.name = ansprechpartner_element.attrib['name']
        ansprechpartner_object.anrede = ansprechpartner_element.find('anrede').text
        ansprechpartner_object.titel = "" if ansprechpartner_element.find('titel') is None else \
            ansprechpartner_element.find('titel').text
        ansprechpartner_object.funktion = "" if ansprechpartner_element.find('funktion') is None else \
            ansprechpartner_element.find('funktion').text
        ansprechpartner_object.telefon = ansprechpartner_element.find('telefon').text
        ansprechpartner_object.fax = "" if ansprechpartner_element.find('fax') is None else \
            ansprechpartner_element.find('fax').text
        ansprechpartner_object.email = ansprechpartner_element.find('email').text
        # declare the object as dictionary in order to be able to be parsed into JSON
        ansprechpartner_object = ansprechpartner_object.__dict__
        firma.ansprechpartner.append(ansprechpartner_object)
    # same as above
    firma = firma.__dict__
    firmen_list.append(firma)
    return firmen_list
