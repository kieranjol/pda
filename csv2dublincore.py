import sys
from lxml import etree as ET


def add_value(value, element):
    element.text = value
    


def create_unit(index,parent, unitname):
    dc_namespace = "http://purl.org/dc/elements/1.1/"
    unitname = ET.Element("{%s}%s" % (dc_namespace, unitname))
    parent.insert(index,unitname)
    return unitname
namespace = '<metadata xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:dc="http://purl.org/dc/elements/1.1/"></metadata>'
dc = ET.fromstring(namespace)
dc_namespace = "http://purl.org/dc/elements/1.1/"
xsi_namespace = "http://www.w3.org/2001/XMLSchema-instance"

create_unit(1, dc, 'title')

creator = create_unit(2, dc, 'creator')
date = create_unit(3, dc, 'date')
description = create_unit(4, dc, 'description')
people = create_unit(5, dc, 'people')
location = create_unit(6, dc, 'location')
subject = create_unit(7, dc, 'subject')
add_value('Joyce,James', creator)
doc = ET.ElementTree(dc)
print(ET.tostring(doc, pretty_print=True,encoding='UTF-8',xml_declaration=True))
