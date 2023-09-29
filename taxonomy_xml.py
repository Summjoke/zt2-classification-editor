import xml.etree.ElementTree as ET
import tkinter.messagebox as MessageBox
import os
import webbrowser

import config


    
def get_taxonomy_xml(result_classification):

    if result_classification == {} :
        MessageBox.showwarning(title="No entry", message="Please select a classification entry in the list!")
        return

    tree = ET.parse('.\docs\TaxonomyXML.xml')
    root = tree.getroot()
    
    
    XMLTypeName = result_classification[-1].get('name')
    root.set('binderType', XMLTypeName)
    
    ParentTag1 = root.find('types')
    ParentTag2 = ParentTag1.find('entity')
    ParentTag3 = ParentTag2.find('actor')
    ParentTag4 = ParentTag3.find('animal')
    
    ParentTag = ParentTag4
    
    List = {}
    for i in range(len(result_classification)):
        List[i] = result_classification[i].get('name')
    

    for i in range(len(List)):
        ET.SubElement(ParentTag, List[i])
        ParentTag = ParentTag.find(List[i])
        
    #Write
    ET.indent(tree, '   ')
    try:
        if_write = tree.write(XMLTypeName+'.xml', encoding="utf-8", xml_declaration=False)
    except IOError:
        MessageBox.showwarning(title="Problems", message="Solution: \nTry running this program as an administrator.")
        return
    else:
        # os.startfile(XMLTypeName+'.xml')
        pass
    finally:
        pass
        
    MessageBox.showinfo(title="Complete", message="Generated the "+XMLTypeName+".xml successfully.")

def open_wiki(args):
    Website = args[0]
    result_classification = args[1]
    
    if result_classification == {} :
        MessageBox.showwarning(title="No entry", message="Please select a classification entry in the list!")
        return
    
    if Website == 'Wikipedia' :
        WebDir = 'https://wikipedia.org/wiki/'
        LinkName = result_classification[-1].get('name')
        
    elif Website == 'ZT2Library' :
        WebDir = 'https://zt2downloadlibrary.fandom.com/wiki/'
        LinkName = 'Category:'+result_classification[-1].get('wiki')
        
    else:
        return
        
    Url = WebDir + LinkName
    webbrowser.open(Url)