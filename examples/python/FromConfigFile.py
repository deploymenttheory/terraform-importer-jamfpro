import jamftf
import jamfpy
import os
import json

# Env Keys

# e.g lbgsandbox
ENV_KEY_TENANT_ID = "JAMFTF_PRO_TENANT_ID"

# oauth
ENV_KEY_CLIENT_ID = "JAMFTF_CLIENT_ID"
ENV_KEY_CLIENT_SECRET = "JAMFTF_CLIENT_SECRET"

# config path INCLUDING filename
ENV_KEY_CONFIG_PATH = "JAMFTF_CONFIG_PATH"

# output DIRECTORY no filename
ENV_KEY_OUT_PATH = "JAMFTF_OUTPUT_PATH"

# All env keys for validation
ENV_KEYS = [
    ENV_KEY_TENANT_ID,
    ENV_KEY_CLIENT_ID,
    ENV_KEY_CLIENT_SECRET,
    ENV_KEY_CONFIG_PATH,
    ENV_KEY_OUT_PATH
]

for i in ENV_KEYS:
    if os.environ.get(i) in [None, ""]:
        raise ValueError("env key %s is empty", i)

# Client - configure as deep as you need to but doesn't need to be complex at thie level
CLIENT = jamfpy.init_client(
    tenant_name=os.environ.get(ENV_KEY_TENANT_ID),
    client_id=os.environ.get(ENV_KEY_CLIENT_ID),
    client_secret=os.environ.get(ENV_KEY_CLIENT_SECRET),
    token_exp_threshold_mins=5
)

def main():
    # Define dir of config file
    config_dir = os.environ.get(ENV_KEY_CONFIG_PATH)

    # Parse json config into JamfTF resources including options
    targets = jamftf.parse_config_file(config_dir)

    # Create a new Importer using targets
    importer = jamftf.Importer(client=CLIENT, targetted=targets, debug=True)

    # Write HCL out to a file (or do what you want with it)
    hcl = importer.HCLd()

    print("waring, this will overwrite existing files of the same name.")
    out_path = os.environ.get(ENV_KEY_OUT_PATH)
    for i, j in hcl.items():
        fn = f"{i}.tf"
        print(f"creating {fn} at {out_path}")
        with open(f"{out_path}/{fn}", "w") as f:
            f.write(j)
        


if __name__ == "__main__":
    main()