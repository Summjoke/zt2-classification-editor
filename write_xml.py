import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilenames
import tkinter.messagebox as MessageBox
import os

import config



xml_trees = []

xml_filenames = []


def get_xmls():
    global xml_trees
    global xml_filenames
    
    filenames = askopenfilenames(title="Select XMLs", filetypes=[("xml files", "*.xml")])
    
    if len(filenames) == 0 :
        return
    
    xml_trees = []
    xml_filenames = []
    
    for item in filenames:
        try:
            xml_trees.append(ET.parse(item))
        except Exception:
            MessageBox.showwarning(title="Problem", message="".join(["This file has encountered a parsing error. Please edit it manually. \n", 'Filename: ', item.split('/')[-1], '\n', 'Solution: \n', 'Make sure that there are no two identical attributes under <BFAIEntityDataShared>.']))
            continue
        else:
            xml_filenames.append(item)
        finally:
            pass
    print('Filenames:', xml_filenames)
    
    
    


def edit_xml(args):
    trees = args[0]
    result_classification = args[1]
    
    premise = ['entity', 'actor', 'animal']
    
    num_complete = 0
    xml_typename = result_classification[-1].get('name')
    
    for i in range(len(trees)):
    
        root = trees[i].getroot()
        
        xml_mainname = root.get('binderType').split('_', 1)[0]
        xml_resnames = []
        
        tag_types = root.find('types')
        
        #Find main name node
        tag_record = tag_types
        while list(tag_record) != []:
            if list(tag_record)[0].tag == xml_mainname:
                tag_mainname = list(tag_record)[0]
                break
            else:
                tag_record = list(tag_record)[0]
        else:
            if tag_record.tag == xml_mainname:
                tag_mainname = tag_record
            else:
                #Problem: No tag for main name
                MessageBox.showwarning(title="Problem", message="".join(["Couldn't find the tag for the species name. \n", 'Filename: ', xml_filenames[i].split('/')[-1]]))
                continue
                
        # print('P1: ', tag_mainname)
        
        tag_reserve = tag_mainname
        xml_resnames.append(tag_reserve.tag)
        
        #Add reserve nodes
        while list(tag_reserve) != []:
            xml_resnames.append(list(tag_reserve)[0].tag)
            tag_reserve = list(tag_reserve)[0]
        
        # print('P2: ', xml_resnames)

        
        list_rcf_names = []
        for item in result_classification:
            list_rcf_names.append(item.get('name'))
            
        list_tags = premise + list_rcf_names + xml_resnames
        print(list_tags)


        tag_types.remove(tag_types.find('entity'))        
        parent_tag = tag_types
        
        for item in list_tags:
            ET.SubElement(parent_tag, item)
            parent_tag = parent_tag.find(item)
            
        #Write
        ET.indent(trees[i], '   ')
        try:
            if_write = trees[i].write(xml_filenames[i], encoding="utf-8", xml_declaration=False)
        except IOError:
            MessageBox.showwarning(title="Problem", message="Couldn't write the XML. \nSolutions: \n1. Try running this program as an administrator. \n2. The XMLs cannot be read-only.")
            return
        else:
            num_complete += 1
             # os.startfile(xml_filenames[i]+'.xml')
        finally:
            pass
    
    if num_complete == 1 :
        unit = 'file'
    else:
        unit = 'files'
    
    MessageBox.showinfo(title="Complete", message= " ".join (["Modified", str(num_complete), unit, "to", xml_typename+'.']))
    
