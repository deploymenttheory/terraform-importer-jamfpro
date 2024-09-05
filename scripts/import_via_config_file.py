"""
Module which relies on ENV vars and config file to programatically generate HCL
import statements using information gathed from Jamf Pro
"""

import os
import jamftf
import jamfpy

ENV_KEYS = {
    "tenant_id": "JAMFTF_JPRO_TENANT_ID",
    "client_id": "JPRO_CLIENT_ID",
    "client_secret": "JPRO_CLIENT_SECRET",
    "config_file_path": "JAMFTF_CONFIG_FP",
    "output_dir": "JAMFTF_OUTPUT_DIR",
    "debug_mode": "JAMFTF_DEBUG_MODE"
}

def env_vars() -> dict:
    """
    Loops through ENV_KEYS and retrieves values from the env

    Will raise a KeyError if any vars are empty or unset.
    """
    out = {}
    for j, k in ENV_KEYS.items():
        val = os.environ.get(k)

        if val is None or val == "":
            raise KeyError("missing environment var: %s, %s", j, k)

        out[j] = val

    return out

ENV = env_vars()

def get_client():
    """
    Inits a base config jamfpy client for API operations
    """

    level = 10 if ENV["debug_mode"].lower() == "true" else 30

    return jamfpy.init_client(
        tenant_name=ENV["tenant_id"],
        client_id=ENV["client_id"],
        client_secret=ENV["client_secret"],
        logging_level=level
    )


def get_hcl() -> dict:
    """
    Parses the config file, feeds the targets to the importer. 

    Importer generates the HCL and returns in dict format
    """
    target_resources = jamftf.parse_config_file(ENV["config_file_path"])

    debug = ENV["debug_mode"].lower() == "true"

    importer = jamftf.Importer(
        client=get_client(),
        targetted=target_resources,
        debug=debug
    )

    return importer.HCLd()


def write_out(hcl_dict: dict) -> None:
    """
    Uses HCL dict to create filenames and populate them with import statemens
    """
    for k, v in hcl_dict.items():

        output_fn = k + ".tf"
        full_path = f"{ENV['output_dir']}/{output_fn}"

        with open(full_path, "w+", encoding="UTF-8") as f:
            f.write(v)

def main():
    """
    gets & writes hcl to files
    """
    write_out(get_hcl())


if __name__ == "__main__":
    main()
