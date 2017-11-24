from Model.Firma import Firma, Ansprechpartner
import xml.etree.ElementTree as ET
import json
from Config.config import rollen


def get_firmen_JSON(name, branche, ort, rolle):
    with open('..\\Data\\firmendaten.xml', 'r') as xml_file:
        tree = ET.parse(xml_file,ET.XMLParser(encoding='urf-8'))
    root = tree.getroot()
    firmen = root.findall('firma')
    firmen_list = []
    # if the role exists
    if rolle in rollen:
        print("in role")
        for firma_element in firmen:
            name_element = firma_element.attrib['name']
            branche_element = firma_element.find('branche').text.lower()
            ort_element = firma_element.find('ort').text.lower()
            if name in name_element and branche == "" and ort == "" and rolle in name_element:
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif name in name_element and branche == branche_element and ort == "" and rolle in name_element:
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif name in name_element and branche == branche_element and ort == ort_element.text and rolle in name_element:
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif "" == name and branche == branche_element and ort == ort_element and rolle in name_element:
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif "" == name and branche == "" and ort == ort_element and rolle in name_element:
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif "" == name and branche == branche_element and ort == "" and rolle in name_element:
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif name in name_element and branche == "" and ort == ort_element and rolle in name_element:
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif "" == name and branche == "" and ort == "" and rolle in name_element:
                firmen_list = get_firmen_list(firma_element, firmen_list)
    # if the role does not exist or was not given
    elif rolle not in rollen:
        print("not in role")
        for firma_element in firmen:
            name_element = firma_element.attrib['name']
            branche_element = firma_element.find('branche').text.lower()
            ort_element = firma_element.find('ort').text.lower()
            if name in name_element and branche == "" and ort == "" and check_for_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif name in name_element and branche == branche_element and ort == "" and check_for_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif name in name_element and branche == branche_element and ort == ort_element and check_for_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif "" == name and branche == branche_element and ort == ort_element and check_for_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif "" == name and branche == "" and ort == ort_element and check_for_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif "" == name and branche == branche_element and ort == "" and check_for_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif name in name_element and branche == "" and ort == ort_element and check_for_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
            elif "" == name and branche == "" and ort == "" and check_for_role(name_element):
                firmen_list = get_firmen_list(firma_element, firmen_list)
    return json.dumps(firmen_list)


def check_for_role(firma_name):
    for role in rollen:
        if role in firma_name:
            return False
    return True


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
