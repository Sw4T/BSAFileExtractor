############################
##### BSAFileExtractor #####
############################
# Small command-line tool to extract specific files from a BSA archive
# Options : 
#   -i : sets the input folder where the BSA archives are, current folder is the default path
#   -o : sets the output folder to given path, current folder is the default path
#
# Example to extract one file : 
#   python BSAFileExtractor.py "Skyrim - Animations.bsa" behavior00.hkx  
# Example to extract multiple files from archive 
#   python BSAFileExtractor.py "Skyrim - Animations.bsa" behavior00.hkx fullcharacter.txt draugr_bow.txt
# Example to extract a file with a given input and output folder
#   python BSAFileExtractor.py "Skyrim - Animations.bsa" -i "D:/Steam/steamapps/common/Skyrim Special Edition/Data" -o "D:/Steam/skyrim_extract" behavior00.hkx 

import sys, os
from pathlib import Path
from bethesda_structs.archive import BSAArchive

# Globals
EXTENSION_FILES = ('.bsa')
OPTIONS = ['-i', '-o', '-h', '-v']
OPTIONS_WITH_ARG = ['-i', '-o']

# Runtime variables
list_filenames = []
input_folder = Path().resolve()
output_folder = Path().resolve().joinpath('extracted')
output_by_user = False
show_header = False
verbose = False
nb_args = len(sys.argv)

# Check argument errors
if nb_args == 1:
    exit('Error : please use a valid syntax to use the command line tool\nValid example : python BSAFileExtractor.py "Skyrim - Animations.bsa" behavior00.hkx')
if not (sys.argv[1]).endswith(EXTENSION_FILES):
    exit('Error : given archive format is not supported. Valid file format : .bsa')

# Handle arguments
it_args = 0
for arg in sys.argv:
    if sys.argv[it_args] in OPTIONS:
        match sys.argv[it_args]:
            case '-i':
                input_folder = Path(sys.argv[it_args]);
            case '-o':
                output_folder = Path(str(sys.argv[it_args]));
                output_by_user = True
            case '-h':
                show_header = True
            case '-v':
                verbose = True
    elif it_args > 1 and (sys.argv[it_args - 1] not in OPTIONS_WITH_ARG):
        list_filenames.append(arg)
    it_args += 1

archive_name = sys.argv[1]
archive_path = input_folder.joinpath(archive_name)

# Checks the output directory and creates it if needed
if not os.path.isdir(output_folder):
    if output_by_user == True:
        exit('Error : please type an existing output folder path to extract the files')
    else:
        os.mkdir(output_folder)

# Iterates over archive file to extract specific files    
try:
    handle_archive = BSAArchive.can_handle(archive_path)
    if not handle_archive:
        exit('The program is not able to handle this archive, please try a valid .bsa file')

    archive = BSAArchive.parse_file(archive_path)
    if show_header:
        print('-----------------------------------')
        print(archive.container.header)               
    
    if nb_args == 2: # If there is no other argument but the archive
        archive.extract(output_folder) 
        print('-----------------------------------\nArchive has been successfully extracted to ' + str(output_folder))
    else:
        print('-----------------------------------\nFilelist to extract :')
        for filename in list_filenames:
            print('\t' + filename)
        print('-----------------------------------\nExtracting...') 

        files_found = []
        nb_total_files = 0
        nb_files_found = 0
        # Search for matching files
        for archive_file in archive.iter_files():
            nb_total_files += 1
            for filename in list_filenames:
                if filename in str(archive_file.filepath):
                    files_found.append(archive_file.filepath)
                    nb_files_found += 1
        
        # Extracts matching files to output folder                 
        for file_to_extract in files_found:
            to_path = output_folder.joinpath(file_to_extract)
            if not to_path.parent.is_dir():
                to_path.parent.mkdir(parents=True)
            with to_path.open("wb") as stream:
                stream.write(archive_file.data)
            if verbose:
                print(file_to_extract)          
            
        print('-----------------------------------\nExtraction complete with ' + str(nb_files_found) + ' files found matching your search within a total of ' + str(nb_total_files) + ' files')
        print('Output folder -> ' + str(output_folder))

except Exception as ex:
    exit('Program error : ' + str(ex))


