import xml.etree.ElementTree as ET
import shutil
import os


def copy_using_config(
    config_file_name, file_name_tag, file_source_tag, 
    file_destination_tag):

    dir_path = os.path.dirname(os.path.realpath(__file__))
    config_file = os.path.join(dir_path, config_file_name)
    
    tree = ET.parse(config_file)
    config = tree.getroot() 

    for file in config:
        values = file.attrib

        file_name = values[file_name_tag]
        source = values[file_source_tag]
        destination = values[file_destination_tag]

        copy_single_file(file_name, source, destination)


def copy_single_file(file_name, source, destination):
    path_from = os.path.join(source, file_name)
    shutil.copy(path_from, destination)


config_file_name = 'config.xml'
file_name_tag = 'file_name'
file_source_tag = 'source_path'
file_destination_tag = 'destination_path'

copy_using_config(config_file_name, file_name_tag, file_source_tag, file_destination_tag)
    
