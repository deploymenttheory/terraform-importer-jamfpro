import jamfpy
import os
from pprint import pprint

CLIENT = jamfpy.init_client(
    tenant_name = os.getenv("PRO_TENANT_NAME"),
    client_id = os .getenv("CLIENT_ID"),
    client_secret = os.getenv("CLIENT_SECRET"),
    token_exp_threshold_mins=  2,
    safe_mode = True,
)

IMPORT_BLOCK = f"import {id = {resource_id}to = {resource_path}}"

def import_block(type, name, id, path):
    return IMPORT_BLOCK.format(
        resource_id=id,
        resource_path=path
    )

def get_scripts(exclude: list) -> list:
    ids = []
    apiCall = CLIENT.pro.scripts.get_all()
    if not apiCall[0].ok:
        raise Exception("bad api call")
    
    for s in apiCall[1]:
        if s["id"] not in exclude:
            ids.append(s["id"])

    return ids


def main():
    print(get_scripts([]))
    print(import_block("jamfpro_script", "script1", 54, "jamfpro_script.script1"))


if __name__ == "__main__":
    main()
    print(IMPORT_BLOCK.format(
        id = 45,
        path="jamfpro_script.script5"
    ))