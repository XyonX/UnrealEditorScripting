import unreal as ue
import os
import json

prefix_mapping = {}

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Join the directory with the JSON file name
json_file_path = os.path.join(script_dir, "prefix_mapping.json")

with open(json_file_path,"r") as json_file:
    prefix_mapping=json.loads(json_file.read())

def add_prefix ():
    #instance of unreal class
    system_lib=ue.SystemLibrary
    editor_util=ue.EditorUtilityLibrary
    string_lib=ue.StringLibrary

    selected_asset = editor_util.get_selected_assets()

    for asset in selected_asset :
        asset_name =  system_lib.get_object_name(asset)
        asset_class = asset.get_class()
        class_name = system_lib.get_class_display_name(asset_class)

        class_prefix = prefix_mapping.get(class_name,None)


        if class_prefix is None :
            ue.log(" Undefined class type found ".format(class_name))
            continue
        if not asset_name.startswith(class_prefix):
            #rename the asset as it doesnt have any prefix
            new_name = class_prefix+asset_name
            editor_util.rename_asset(asset,new_name)



add_prefix()