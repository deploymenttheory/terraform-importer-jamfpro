"""
handles all hcl related operations
"""

def import_block(resource_type, name, id):
    """
    returns valid import block
    """

    # if any([i for i in [resource_type, name, id] == ""]):
    #     raise ValueError("one or more arguments are empty")

    return "import {\nid = " + str(id) + "\nto = " + f"{resource_type}.{name}" + "\n}" 



def generate_imports(data: dict) -> list:
    """
    data should follow this structure:
    data: {
        "resource_type": TYPE AS IN PROVIDER
        "resources": [
            {
                "id": ID,
                "name": NAME
            },
            {
                "id": ID,
                "name": NAME
            }
        ]
    }
    """
    out_list = []

    for d in data["resources"]:
        out_list.append(
            import_block(
                resource_type=data["resource_type"],
                name = d["name"],
                id = d ["id"]
            )
        )

    return out_list
