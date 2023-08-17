# Unreal Editor Scripting

This repository contains a collection of editor scripts for Unreal Engine that can help you automate, optimize, and enhance your game development workflow. These scripts are written in Python and can be run from the Unreal Editor using the command line or the Python console.

## Features

Some of the features that these scripts provide are:

- Auto file prefix: This script will add a prefix to all the files in the current directory, based on their file type. For example, if you have a file named `report.docx`, it will be renamed to `DOC_report.docx`. This script will help you organize your files by their format.
- Project organizer: This script will create subdirectories for each project that you have in the current directory, and move the files that belong to each project into their respective subdirectories. For example, if you have files named `DOC_report.docx`, `PPT_presentation.pptx`, and `XLS_data.xlsx` that are part of the same project, they will be moved to a subdirectory named `Project_1`. This script will help you organize your files by their project.
- Asset cleaner: This script will scan your project for unused or orphaned assets, and delete them from your project folder and your Content Browser. This script will help you reduce the size of your project and improve its performance.
- Level generator: This script will generate a random level based on some parameters that you can specify, such as the number of rooms, the size of each room, the type of lighting, etc. This script will help you create prototype levels quickly and easily.

## Installation

To use these scripts, you need to have Unreal Engine 5 installed on your computer. You also need to enable the Python Editor Script Plugin in your Unreal Editor. To do this, go to Edit > Plugins > Scripting > Python Editor Script Plugin and check the Enabled box. You may need to restart the Unreal Editor for the changes to take effect.

To download these scripts, you can either clone this repository using Git or download it as a ZIP file. To clone this repository using Git, open a terminal or command prompt and enter:

```
git clone https://github.com/XyonX/UnrealEditorScripting.git
```

To download this repository as a ZIP file, go to [this page](https://github.com/XyonX/UnrealEditorScripting.git) and click on the Code button, then select Download ZIP.

## Usage

To run these scripts from the Unreal Editor, you can either use the command line or the Python console. To use the command line, go to Window > Developer Tools > Output Log and enter:

```
py.exec "path/to/script.py"
```

where `path/to/script.py` is the relative or absolute path of the script file that you want to run.

To use the Python console, go to Window > Developer Tools > Python Console and enter:

```
exec(open("path/to/script.py").read())
```

where `path/to/script.py` is the relative or absolute path of the script file that you want to run.

You can also modify the parameters of each script by opening them in a text editor and changing the values of some variables. For example, in the level generator script, you can change the number of rooms by changing the value of `num_rooms`.

## License

This project is licensed under the MIT License - see the [LICENSE](^2^) file for details.