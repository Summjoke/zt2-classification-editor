import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilenames
import tkinter.messagebox as MessageBox
import os

import config



xml_trees = {}

xml_filenames = {}
xml_names = {}


def get_xmls():
    global xml_trees
    global xml_filenames
    
    filenames = askopenfilenames(title="Select XMLs", filetypes=[("xml files", "*.xml")])
    print('Filenames:', filenames)
    
    if len(filenames) == 0 :
        return
    
    xml_filenames = filenames
    xml_trees = {}
    for i in range(len(xml_filenames)):
        xml_trees[i] = ET.parse(xml_filenames[i])


def edit_xml(args):
    trees = args[0]
    result_classification = args[1]
    
    premise = ['entity', 'actor', 'animal']
    
    num_complete = 0
    xml_typename = result_classification[-1].get('name')
    
    for i in range(len(trees)):
    
        root = trees[i].getroot()
        
        xml_names[i] = root.get('binderType')
        
        tag_types = root.find('types')
        tag_entitys = tag_types.findall('entity')
        for k in range(len(tag_entitys)):
            tag_types.remove(tag_entitys[k])        
        
        parent_tag = root.find('types')
        
        list_rcf_names = {}
        for k in range(len(result_classification)):
            list_rcf_names[k] = result_classification[k].get('name')
            
        print(list_rcf_names)
        list_tags = premise + list(list_rcf_names.values()) + [xml_names[i]]

        for j in range(len(list_tags)):
            ET.SubElement(parent_tag, list_tags[j])
            parent_tag = parent_tag.find(list_tags[j])
            
        #Write
        ET.indent(trees[i], '   ')
        try:
            if_write = trees[i].write(xml_filenames[i], encoding="utf-8", xml_declaration=False)
        except IOError:
            MessageBox.showwarning(title="Problem", message="Solutions: \n1. Try running this program as an administrator. \n2. The XMLs cannot be read-only.")
            return
        else:
            num_complete += 1
             # os.startfile(xml_names[i]+'.xml')
        finally:
            pass
    
    if num_complete == 1 :
        unit = 'file'
    else:
        unit = 'files'
    
    MessageBox.showinfo(title="Complete", message= " ".join (["Modified", str(num_complete), unit, "to", xml_typename+'.']))
    
