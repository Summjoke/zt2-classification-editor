import xml.etree.ElementTree as ET
import os

import config


tree = ET.parse('.\docs\TaxonomyEntries.xml')
root = tree.getroot()

def get_list():

    #Class
    list_class = root.findall('Class')
    # print('\nClass:\n', list_class)

    #Order
    list_order = {}

    for i in range(len(list_class)):
        list_order[i] = list_class[i].findall('Order')
        
    # print('\nOrder:\n', list_order)

    #Family
    list_family = {}

    for i in range(len(list_order)):
        list_family[i] = {}
        for j in range(len(list_order[i])):
            list_family[i][j] = list_order[i][j].findall('Family')
    # print('\nFamily:\n', list_family)
    
    #Genus
    list_genus = {}
    
    for i in range(len(list_family)):
        list_genus[i] = {}
        for j in range(len(list_family[i])):
            list_genus[i][j] = {}
            for k in range(len(list_family[i][j])):
                list_genus[i][j][k] = list_family[i][j][k].findall('Genus')
    # print('\nGenus:\n', list_genus)
    
    #Species
    list_species = {}
    
    for i in range(len(list_genus)):
        list_species[i] = {}
        for j in range(len(list_genus[i])):
            list_species[i][j] = {}
            for k in range(len(list_genus[i][j])):
                list_species[i][j][k] = {}
                for a in range(len(list_genus[i][j][k])):
                    list_species[i][j][k][a] = list_genus[i][j][k][a].findall('Species')
                    
    # print('\nSpecies:\n', list_species)
    
    return list_class, list_order, list_family, list_genus, list_species