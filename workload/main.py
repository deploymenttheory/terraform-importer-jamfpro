import importer
import jamfpy
import os
from pprint import pprint

# Env Key
ENV_KEY_TENANT_NAME = "PRO_TENANT_ID"
ENV_KEY_CLIENT_ID = "CLIENT_ID"
ENV_KEY_CLIENT_SECRET = "CLIENT_SECRET"


CLIENT = jamfpy.init_client(
    tenant_name=os.environ.get(ENV_KEY_TENANT_NAME),
    client_id=os.environ.get(ENV_KEY_CLIENT_ID),
    client_secret=os.environ.get(ENV_KEY_CLIENT_SECRET),
    token_exp_threshold_mins=5
)

magic = importer.Importer(CLIENT, use_jamf_name=True)
hcl = magic.scripts.HCL()

with open("new_tf_file.tf", "w") as f:
    for i in hcl:
        f.write(i + "\n\n")