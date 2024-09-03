import jamftf
import jamfpy
import os
import json

# Env Key
ENV_KEY_TENANT_NAME = "PRO_TENANT_ID"
ENV_KEY_CLIENT_ID = "CLIENT_ID"
ENV_KEY_CLIENT_SECRET = "CLIENT_SECRET"

# out path INCLUDING filename
OUT_PATH = "/Users/joseph/github/importer/importer-terraform-jamfpro/testing.tf"

# Client
CLIENT = jamfpy.init_client(
    tenant_name=os.environ.get(ENV_KEY_TENANT_NAME),
    client_id=os.environ.get(ENV_KEY_CLIENT_ID),
    client_secret=os.environ.get(ENV_KEY_CLIENT_SECRET),
    token_exp_threshold_mins=5
)

def main():
    # Define dir of config file
    config_dir = "/Users/joseph/github/importer/importer-terraform-jamfpro/examples/python/config.json"

    # Load .json file into a dict using json module
    with open(config_dir, "r") as file:
        jsonData = json.load(file)

    # Parse json config into JamfTF resources including options
    targets = jamftf.parse_config_file(jsonData)

    # Create a new Importer using targets
    importer = jamftf.Importer(client=CLIENT, targetted=targets)

    # Write HCL out to a file (or do what you want with it)
    hcl = importer.HCL()
    with open(OUT_PATH, "w") as f:
        f.write(hcl)

    print(hcl)



if __name__ == "__main__":
    main()