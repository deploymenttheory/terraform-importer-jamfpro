import jamftf
import jamfpy
import os

# Env Keys for client.
ENV_KEY_TENANT_NAME = "PRO_TENANT_ID"
ENV_KEY_CLIENT_ID = "CLIENT_ID"
ENV_KEY_CLIENT_SECRET = "CLIENT_SECRET"

# Define a client from Jamfpy usage to allow importer to interface with Jamfpro
CLIENT = jamfpy.init_client(
    tenant_name=os.environ.get(ENV_KEY_TENANT_NAME),
    client_id=os.environ.get(ENV_KEY_CLIENT_ID),
    client_secret=os.environ.get(ENV_KEY_CLIENT_SECRET),
    token_exp_threshold_mins=5
)

# Optionally define any options for your resources to use
options = jamftf.Options(use_resource_type_as_name=True)

# Define target resources for Importer to generate
scripts = jamftf.Scripts(options=options)

# Load your resources into the importer
target_resources = [scripts]
importer = jamftf.Importer(CLIENT, target_resources)

# Retrieve the HCL from the Importer
hcl = importer.HCL()

# hcl now holds a string ready to load into a .tf file
print(hcl)