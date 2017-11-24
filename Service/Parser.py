from Model.Firma import Firma, Ansprechpartner
import xml.etree.ElementTree as ET
import json
from Config.config import rollen


def get_firmen_objects(name, branche, ort, rolle):
    print(name,branche,ort,rolle)
    with open('..\\Data\\firmendaten.xml', 'r') as xml_file:
        tree = ET.parse(xml_file)
    root = tree.getroot()
    firmen = root.findall('firma')
    firmen_list = []
    if rolle in rollen:
        for firma_element in firmen:
            if firma_element.attrib['name'] == name and branche == "" and ort == "" \
                    and rolle in firma_element.attrib['name']:
                firmen_list = filter_objects(firma_element, firmen_list)
            elif firma_element.attrib['name'] == name and branche == firma_element.find('branche').text and ort == "" \
                    and rolle in firma_element.attrib['name']:
                firmen_list = filter_objects(firma_element, firmen_list)
            elif firma_element.attrib['name'] == name and branche == firma_element.find('branche').text \
                    and ort == firma_element.find('ort').text and rolle in firma_element.attrib['name']:
                firmen_list = filter_objects(firma_element, firmen_list)
            elif "" == name and branche == firma_element.find('branche').text \
                    and ort == firma_element.find('ort').text and rolle in firma_element.attrib['name']:
                firmen_list = filter_objects(firma_element, firmen_list)
            elif "" == name and branche == "" \
                    and ort == firma_element.find('ort').text and rolle in firma_element.attrib['name']:
                firmen_list = filter_objects(firma_element, firmen_list)
            elif "" == name and branche == firma_element.find('branche').text \
                    and ort == "" and rolle in firma_element.attrib['name']:
                firmen_list = filter_objects(firma_element, firmen_list)
            elif firma_element.attrib['name'] == name and branche == "" \
                    and ort == firma_element.find('ort').text and rolle in firma_element.attrib['name']:
                firmen_list = filter_objects(firma_element, firmen_list)
            elif "" == name and branche == "" \
                    and ort == "" and rolle in firma_element.attrib['name']:
                firmen_list = filter_objects(firma_element, firmen_list)
    elif rolle not in rollen:
        for firma_element in firmen:
            if firma_element.attrib['name'] == name and branche == "" and ort == "" \
                    and check_for_role(firma_element.attrib['name']):
                firmen_list = filter_objects(firma_element, firmen_list)
            elif firma_element.attrib['name'] == name and branche == firma_element.find('branche').text and ort == "" \
                    and check_for_role(firma_element.attrib['name']):
                firmen_list = filter_objects(firma_element, firmen_list)
            elif firma_element.attrib['name'] == name and branche == firma_element.find('branche').text \
                    and ort == firma_element.find('ort').text and check_for_role(firma_element.attrib['name']):
                firmen_list = filter_objects(firma_element, firmen_list)
            elif "" == name and branche == firma_element.find('branche').text \
                    and ort == firma_element.find('ort').text and check_for_role(firma_element.attrib['name']):
                firmen_list = filter_objects(firma_element, firmen_list)
            elif "" == name and branche == "" \
                    and ort == firma_element.find('ort').text and check_for_role(firma_element.attrib['name']):
                firmen_list = filter_objects(firma_element, firmen_list)
            elif "" == name and branche == firma_element.find('branche').text \
                    and ort == "" and check_for_role(firma_element.attrib['name']):
                firmen_list = filter_objects(firma_element, firmen_list)
            elif firma_element.attrib['name'] == name and branche == "" \
                    and ort == firma_element.find('ort').text and check_for_role(firma_element.attrib['name']):
                firmen_list = filter_objects(firma_element, firmen_list)
    return json.dumps(firmen_list)


def check_for_role(firma_name):
    for role in rollen:
        if role in firma_name:
            return False
    return True




def filter_objects(firma_element, firmen_list):
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

