import xml.etree.ElementTree as ET

#Recursively remove all namespaces from the lxml etree
def remove_all_lxml_namespaces(lxml_root):
    for element in lxml_root.getiterator():
        element.tag = etree.QName(element).localname
        etree.cleanup_namespaces(lxml_root)
