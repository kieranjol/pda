import sys
from lxml import etree as ET
import csv
from glob import glob
import os
def grab_csv(csv_file):
    if os.path.isfile(csv_file):
        read_object = open(csv_file)
        reader = csv.reader(read_object)
        csv_list = list(reader)
        read_object.close()
        return csv_list[-1]

def add_value(value, element):
    element.text = value
    
def create_unit(index,parent, unitname):
    dc_namespace = "http://purl.org/dc/elements/1.1/"
    unitname = ET.Element("{%s}%s" % (dc_namespace, unitname))
    parent.insert(index,unitname)
    return unitname


input = sys.argv[1]
os.chdir(input)
csv_files = glob('*.csv')
print csv_files
for files in csv_files:
    namespace = '<metadata xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:dc="http://purl.org/dc/elements/1.1/"></metadata>'
    dc = ET.fromstring(namespace)
    dc_namespace = "http://purl.org/dc/elements/1.1/"
    xsi_namespace = "http://www.w3.org/2001/XMLSchema-instance"
    csv_list = grab_csv(files)
    title = create_unit(1, dc, 'title')
    creator = create_unit(2, dc, 'creator')
    date = create_unit(3, dc, 'date')
    description = create_unit(4, dc, 'description')
    people = create_unit(5, dc, 'people')
    location = create_unit(6, dc, 'location')
    subject = create_unit(7, dc, 'subject')
    add_value(csv_list[1], date)
    add_value(csv_list[2], title)
    add_value(csv_list[3], creator)
    add_value(csv_list[4], people)
    add_value(csv_list[5], location)
    add_value(csv_list[6], description)
    add_value(csv_list[7], subject)
    doc = ET.ElementTree(dc)
    print(ET.tostring(doc, pretty_print=True,encoding='UTF-8',xml_declaration=True))
