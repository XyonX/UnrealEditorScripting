import unreal as ue


def rename_assets(target_string,new_string,use_case):
    #instance of unreal class
    system_lib=ue.SystemLibrary
    editor_util=ue.EditorUtilityLibrary
    string_lib=ue.StringLibrary

    #get the selected assets
    selected_assets = editor_util.get_selected_assets()
    num_assets = len(selected_assets)
    replaced = 0

    ue.log("selected {} Assets ".format(num_assets))

    #loop through each asset and rename them

    for asset in selected_assets :
        asset_name = system_lib.get_object_name(asset)
        ue.log(asset_name)

        if string_lib.contains(asset_name,target_string,use_case=use_case) :
            search_case = ue.SearchCase.CASE_SENSITIVE if use_case else ue.SearchCase.IGNORE_CASE
            new_name = string_lib.replace(asset_name,target_string,new_string,search_case=search_case)
            editor_util.rename_asset(asset,new_name)

            replaced+=1
            ue.log(" renamed asset {}".format(asset_name))

        else:
            ue.log(" {} doesnt contain the targated string ".format(asset_name))

    ue.log(" {} asset renamed".format(replaced))


rename_assets("Actar","Actor",False)