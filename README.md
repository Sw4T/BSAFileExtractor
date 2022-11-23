# BSAFileExtractor

A simple CLI tool to extract one or a list of specific files from a Bethesda archive. 
Requires [Python 3.10](https://www.python.org/downloads/) or higher.

A copy of [Bethesda-structs project by Stephen Bunn](https://github.com/stephen-bunn/bethesda-structs) is already provided within the repository and is needed for this project.

_Actual supported formats_ : .bsa

## Options available
- **-i** : Sets the input folder with an absolute path
- **-o** : Sets the output folder with an absolute path
- **-h** : Shows the header of the archive
- **-v** : Verbose mode - prints every filepath to be extracted

## How to use
- Put the Bethesda archive(s) you want to work with in this repository (_or use -i option_)
- Open a command-line interface (if you're using Windows, type 'cmd' in your search bar)
- Navigate to the path where you've cloned/downloaded this repository by typing ``cd PATH_TO_YOUR_FOLDER``
- Execute the program by using the following syntax : 

``python BSAFileExtractor.py ARCHIVE_NAME [-i "INPUT_FOLDER" | -o "OUTPUT_FOLDER" | -h | -v] file.txt file2.hkk ...``

## Examples
#### To extract all files matching a keyword
``python BSAFileExtractor.py "Skyrim - Animations.bsa" behavior00.hkx`` 
#### To extract all files using multiple keywords
``python BSAFileExtractor.py "Skyrim - Animations.bsa" behavior00.hkx fullcharacter.txt draugr_bow.txt``
#### To extract all files with a given input and output folder
``python BSAFileExtractor.py "Skyrim - Animations.bsa" -i "D:/Steam/steamapps/common/Skyrim Special Edition/Data" -o "D:/Steam/skyrim_extract" behavior00.hkx``
#### To extract multiple files while printing archive header and matching paths found
``python BSAFileExtractor.py "Skyrim - Animations.bsa" -v -h behavior00.hkx fullcharacter.txt``
#### To extract a specific file
``python BSAFileExtractor.py "Skyrim - Animations.bsa" meshes\clutter\blacksmith\blacksmithforge01\behaviors\behavior00.hkx``
#### To extract all files from the archive
``python BSAFileExtractor.py "Skyrim - Animations.bsa"``
