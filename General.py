import pandas as pd
import os
import shutil
from pandas import read_csv
from re import findall
import json



def folder_check(directory,create = True):
    """
    Checks to see if a directory exists on hardrive and allows for the creation of it if not.
    Parameters
    ----------
    directory : string
        The directory that is being checked
    create : bool
        If True and the directory does not exist, it is created.
    """
    if not os.path.exists(directory): #Checks if folder exists
        if create == True: 
            os.makedirs(directory) # Creates folder   
            
def copytree(src, dst, symlinks=False, ignore=None):
    """
    Copies folder to another directory
    Parameters
    ----------
    scr : string
        The source directory to be copied
    dst : string
        The destination to where the folder is copied
    """
    for item in os.listdir(src): #Scans items in folder
        s = os.path.join(src, item) # Creates source path for file
        d = os.path.join(dst, item) # Creates destination path for file
        if os.path.isdir(s): # Copies file to new directory
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)            
            
def clear_folder(folder):
    """
    Clears the contents of a directory (WARNING: BE CAREFUL WITH THIS FUNCTION TO AVOID LARGE DATA LOSS)
    Parameters
    ----------
    folder : string
        The directory that wants to emptied
    """
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))   
            
def read_folder(directory, file_suffix, import_limit = 0, name_exclusions = [], index_col = None, index_system = None):
    """
    Imports every file from a folder of a particular file type into a dictionary (NOTE: Only tested for csv files)
    Parameters
    ----------
    directory : string
        The directory containing the files to import
    file_suffix : string
        The file format of the import files
    import_limit : int
        Limits the number of files imported
    name_exclusions : list
        A list of strings that tells read_folder to ignore any file names containing those strings
    index_col : int, str, sequence of int / str, or False, default None
        selects which column in file acts as index column.
    index_system : string, None default None
        Decides how the import files are indexed in dictionary
        'filename_numbers' indexes by numbers in filename
    Returns
    ----------
    data : dictionary
        A dictionary containing the data that is imported
    """
    files = os.listdir(directory) # gathers list of files in directory
    data = {}
    Count = 0
    for file in files: #loops through files
        temp_file_name = directory + "/" + file #gathers file names
        if file_suffix not in temp_file_name: # checks for file suffix
            pass
        elif any(name in temp_file_name for name in name_exclusions): # checks for excluded file name formats
            pass
        else:
            Count += 1
            if index_system == 'filename_numbers':
                data[findall("\d+",file)[0]] = read_csv(temp_file_name,index_col = index_col) # imports file into dictionary
            else:
                data[str(Count)] = read_csv(temp_file_name,index_col = index_col) # imports file into dictionary
        if import_limit > 0: # if no of file has been limited, checks count
            if Count == import_limit: 
                break
    return data


def nested_update(obj, key, value):
    """
    Edits a key within a nested dictionary
    
    Parameters
    ----------
    obj : dict
        Dictionary to be edited
    key : string
        Key within dictionary to be edited
    value : string, int, float
        New value for key

    """
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, (dict, list)):
                nested_update(v, key, value)
            elif k == key:
                obj[k] = value
    elif isinstance(obj, list):
        for item in obj:
            nested_update(item, key, value)     
            

def json_edit(file_location, parameter, parameter_value):
    """
    Edits a parameter within a json file.

    Parameters
    ----------
    file_location : string
        Location of json file that is being edited, json file is imported as a dict
    parameter : list(string)
        List of keys for location of key being edited
    parameter_value : string, int, float
        New value for key
        
    """
    #Open json file
    file_access = open(file_location, "r")
    json_object = json.load(file_access)
    
    #Edit Parameter
    nested_update(json_object, parameter, parameter_value)
            
    #Saves json file
    file_access = open(file_location, "w")
    json.dump(json_object, file_access)
    file_access.close()
            
  