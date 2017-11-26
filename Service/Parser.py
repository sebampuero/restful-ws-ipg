from Model.Firma import Firma, Ansprechpartner
import xml.etree.ElementTree as ET
import json
from Config.config import rollen


# Get the list of companies according to query parameters in JSON format
# @param name the name of the company
# @param branche the department of the company
# @param ort the place of the company
# @param rolle the role the company has
# return the list of companies queried in JSON
def get_firmen_JSON(name, branche, ort, rolle):
    with open('..\\Data\\firmendaten.xml', 'r') as xml_file:
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
            # check role in name as the whole word and not if it is contained inside another word using regex
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
    # if the role does not exist or was not given
    elif rolle not in rollen and rolle == "":
        print("not in role")
        for firma_element in firmen:
            name_element = firma_element.attrib['name'].lower()
            branche_element = firma_element.find('branche').text.lower()
            ort_element = firma_element.find('ort').text.lower()
            if name in name_element and branche == "" and ort == "" and has_not_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif name in name_element and branche in branche_element and ort == "" and has_not_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif name in name_element and branche in branche_element and ort == ort_element and has_not_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif "" == name and branche in branche_element and ort == ort_element and has_not_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif "" == name and branche == "" and ort == ort_element and has_not_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif "" == name and branche in branche_element and ort == "" and has_not_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif name in name_element and branche == "" and ort == ort_element and has_not_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif "" == name and branche == "" and ort == "" and has_not_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
    else:
        return "[]"
    return json.dumps(firmen_list).replace("name", "@name")

# Check if the given company has no role
# @param firma_name the name of the company
# return true if it has no role, false otherwise
def has_not_role(firma_name):
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
        index = name.index(role, len(name) - len(role))
        if (name[index - 1] == " ") and ((index + len(role)) % len(name) == 0):
            return True
    except:
        try:
            index = name.index(role)
            if (name[index-1] == " ") and (name[index+len(role)] == " "):
                return True
        except:
            return False
    else:
        return False

# Parse the XML Elements into objects and populate the given list
# @param firma_element the XML root element
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
    ansprechpartnern = firma_element.findall('ansprechpartner')

    for ansprechpartner_element in ansprechpartnern:
        ansprechpartner = Ansprechpartner()
        ansprechpartner.name = ansprechpartner_element.attrib['name']
        ansprechpartner.anrede = ansprechpartner_element.find('anrede').text
        ansprechpartner.titel = "" if ansprechpartner_element.find('titel') is None else \
            ansprechpartner_element.find('titel').text
        ansprechpartner.funktion = "" if ansprechpartner_element.find('funktion') is None else \
            ansprechpartner_element.find('funktion').text
        ansprechpartner.telefon = ansprechpartner_element.find('telefon').text
        ansprechpartner.fax = "" if ansprechpartner_element.find('fax') is None else \
            ansprechpartner_element.find('fax').text
        ansprechpartner.email = ansprechpartner_element.find('email').text
        # declare the object as dictionary in order to be able to be parsed into JSON
        ansprechpartner = ansprechpartner.__dict__
        firma.ansprechpartner.append(ansprechpartner)
    # same as above
    firma = firma.__dict__
    firmen_list.append(firma)
    return firmen_list
