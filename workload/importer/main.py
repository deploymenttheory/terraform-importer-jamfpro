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


def import_block(resource_type, name, id):
    return "import {\nid = " + id + "\nto = " + f"{resource_type}.{name}" + "\n}" 

def get_scripts(exclude: list = []) -> list:
    ids = []
    apiCall = CLIENT.pro.scripts.get_all()
    if not apiCall[0].ok:
        raise Exception("bad api call")
    
    for s in apiCall[1]:
        if s["id"] not in exclude:
            ids.append(s["id"])

    return ids


def generate_imports(id_list: list, resource_type: str) -> list:
    out_list = []
    type_singular = resource_type.split("_", 1)[1]
    count = 1
    for i in id_list:
        out_list.append(
            import_block(
                id=i,
                resource_type=resource_type,
                name=f"{type_singular}_{count}"
            )
        )
        count += 1

    return out_list


def main():
    hcl = generate_imports(get_scripts(), "jamfpro_script")
    for i in hcl:
        print(i)


if __name__ == "__main__":
    main()
    