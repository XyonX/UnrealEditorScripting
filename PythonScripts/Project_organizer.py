import unreal as ue
import os

editor_util =ue.EditorUtilityLibrary()
system_lib = ue.SystemLibrary()
editor_asset_library = ue.EditorAssetLibrary()

#get the selected assets
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)

# project parent directory
parent_dir = "\\Game"

organize_count = 0
for asset in selected_assets:

    # get the asset class information
    asset_name = system_lib.get_object_name(asset)
    asset_class=asset.get_class()
    class_name=system_lib.get_class_display_name(asset_class)

    #setup the new path
    new_path = os.path.join(parent_dir,class_name,asset_name)
    editor_asset_library.rename_loaded_asset(asset,new_path)
    ue.log("  asset class type is : {} ".format(class_name))
    ue.log("  new path for the assets {} is {} ".format(asset_name,new_path))
    organize_count +=1


ue.log(" Number of assets organized : {}".format(organize_count))