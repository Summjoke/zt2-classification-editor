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
    
    Premise = ['entity', 'actor', 'animal']
    
    num_Complete = 0
    XMLTypeName = result_classification[-1].get('name')
    
    for i in range(len(trees)):
    
        root = trees[i].getroot()
        
        xml_names[i] = root.get('binderType')
        
        tag_types = root.find('types')
        tag_entitys = tag_types.findall('entity')
        for k in range(len(tag_entitys)):
            tag_types.remove(tag_entitys[k])        
        
        ParentTag = root.find('types')
        
        List_RCFnames = {}
        for k in range(len(result_classification)):
            List_RCFnames[k] = result_classification[k].get('name')
            
        print(List_RCFnames)
        List = Premise + list(List_RCFnames.values()) + [xml_names[i]]

        for j in range(len(List)):
            ET.SubElement(ParentTag, List[j])
            ParentTag = ParentTag.find(List[j])
            
        #Write
        ET.indent(trees[i], '   ')
        try:
            if_write = trees[i].write(xml_filenames[i], encoding="utf-8", xml_declaration=False)
        except IOError:
            MessageBox.showwarning(title="Problems", message="Solution: \nTry running this program as an administrator.")
            return
        else:
            num_Complete += 1
             # os.startfile(xml_names[i]+'.xml')
        finally:
            pass
    
    MessageBox.showinfo(title="Complete", message="Modified "+str(num_Complete)+" file(s) to "+XMLTypeName+" successfully.")
