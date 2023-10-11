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
    
    
    xml_typename = result_classification[-1].get('name')
    root.set('binderType', xml_typename)
    
    parent_tag1 = root.find('types')
    parent_tag2 = parent_tag1.find('entity')
    parent_tag3 = parent_tag2.find('actor')
    parent_tag4 = parent_tag3.find('animal')
    
    parent_tag = parent_tag4
    
    list_tags = []
    for item in result_classification:
        list_tags.append(item.get('name'))
    

    for item in list_tags:
        ET.SubElement(parent_tag, item)
        parent_tag = parent_tag.find(item)
        
    #Write
    ET.indent(tree, '   ')
    try:
        if_write = tree.write(xml_typename+'.xml', encoding="utf-8", xml_declaration=False)
    except IOError:
        MessageBox.showwarning(title="Problem", message="Solution: \nTry running this program as an administrator.")
        return
    else:
        # os.startfile(xml_typename+'.xml')
        pass
    finally:
        pass
        
    MessageBox.showinfo(title="Complete", message=" ".join(["Generated the", xml_typename+'.xml.']))

def open_wiki(args):
    website = args[0]
    result_classification = args[1]
    
    if result_classification == {} :
        MessageBox.showwarning(title="No entry", message="Please select a classification entry in the list!")
        return
    
    if website == 'Wikipedia' :
        webdir = 'https://wikipedia.org/wiki/'
        linkname = result_classification[-1].get('name')
        
    elif website == 'ZT2Library' :
        webdir = 'https://zt2downloadlibrary.fandom.com/wiki/'
        linkname = 'Category:'+result_classification[-1].get('wiki')
        
    else:
        return
        
    url = webdir + linkname
    webbrowser.open(url)