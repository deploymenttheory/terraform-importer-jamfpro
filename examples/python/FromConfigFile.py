import jamftf
import jamfpy
import os
import json

import jamftf.exceptions

# Env Key
ENV_KEY_TENANT_NAME = "PRO_TENANT_ID"
ENV_KEY_CLIENT_ID = "CLIENT_ID"
ENV_KEY_CLIENT_SECRET = "CLIENT_SECRET"

# Client
CLIENT = jamfpy.init_client(
    tenant_name=os.environ.get(ENV_KEY_TENANT_NAME),
    client_id=os.environ.get(ENV_KEY_CLIENT_ID),
    client_secret=os.environ.get(ENV_KEY_CLIENT_SECRET),
    token_exp_threshold_mins=5
)

def main():
    # Define dir of config file
    config_dir = "/Users/joseph/github/importer-terraform-jamfpro/examples/python/config.json"

    # Load .json file into a dict using json module
    with open(config_dir, "r") as file:
        jsonData = json.load(file)

    # Parse json config into JamfTF resources including options
    targets = jamftf.parse_config_file(jsonData)

    # Create a new Importer using targets
    importer = jamftf.Importer(client=CLIENT, targetted=targets)

    # Print HCL from Importer (or do whatever you need to with it)
    print(importer.HCL())



if __name__ == "__main__":
    main()