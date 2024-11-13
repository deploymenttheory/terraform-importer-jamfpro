"""
Module which relies on ENV vars and config file to programatically generate HCL
import statements using information gathed from Jamf Pro
"""

import os
import jamftf
import jamfpy


# Consts
CONFIG_FN = "jamftf_config.json"

# Environment vars
JP_TENANT_NAME = os.environ.get("JP_TENANT_NAME")
JP_CLIENT_ID = os.environ.get("JP_CLIENT_ID")
JP_CLIENT_SECRET = os.environ.get("JP_CLIENT_SECRET")
WORKING_DIR = os.environ.get("WORKING_DIR")


def check_env():
    """
    check_env ensures no env vars are empty or unset.
    Raises KeyError if one is.
    """
    env_vars = [
        JP_TENANT_NAME,
        JP_CLIENT_ID,
        JP_CLIENT_SECRET,
        WORKING_DIR
    ]

    if any(i == "" or i is None for i in env_vars):
        raise KeyError("one or more env vars are empty")


JP_CLIENT = jamfpy.init_client(
        tenant_name=JP_TENANT_NAME,
        client_id=JP_CLIENT_ID,
        client_secret=JP_CLIENT_SECRET,
        logging_level=30
    )


def get_hcl() -> dict:
    """
    Parses the config file, feeds the targets to the importer. 

    Importer generates the HCL and returns in dict format
    """
    target_resources = jamftf.parse_config_file(f"{WORKING_DIR}/{CONFIG_FN}")

    importer = jamftf.Importer(
        client=JP_CLIENT(),
        targetted=target_resources,
        debug=False
    )

    return importer.HCLd()


def write_out(hcl_dict: dict) -> None:
    """
    Uses HCL dict to create filenames and populate them with import statemens
    """
    for res_type, v in hcl_dict.items():

        path = f"{WORKING_DIR}/{res_type}.tf"

        os.mkdir(os.path.dirname(path), exist_ok=True)

        with open(path, "w+", encoding="UTF-8") as f:
            f.write(v)


def main():
    """
    gets & writes hcl to files
    """
    check_env()

    write_out(get_hcl())


if __name__ == "__main__":
    main()
