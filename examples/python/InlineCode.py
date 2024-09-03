import jamftf
import jamfpy
import os

# Env Key
ENV_KEY_TENANT_NAME = "PRO_TENANT_ID"
ENV_KEY_CLIENT_ID = "CLIENT_ID"
ENV_KEY_CLIENT_SECRET = "CLIENT_SECRET"


# Client
CLIENT = jamfpy.init_client(
    tenant_name=os.environ.get(ENV_KEY_TENANT_NAME),
    client_id=os.environ.get(ENV_KEY_CLIENT_ID),
    client_secret=os.environ.get(ENV_KEY_CLIENT_SECRET),
    token_exp_threshold_mins=5,
)


# Optionally define some Jamf resourcs to exclude by their IDs
exclude = {
    "jamfpro_script": [
        7761,
        7759,
        7723,
        7725,
        7724,
        7760
    ],
    "jamfpro_category": [
        163
    ]
}



# Define resources, validation setting and attach options defined earlier
scripts = jamftf.Scripts(validate=False, exclude=exclude["jamfpro_script"])
categories = jamftf.Categories(validate=False)

# Create a new importer using the Jamf Resources you have made above
importer = jamftf.Importer(CLIENT, targetted=[categories, scripts], debug=True)

# Generate HCL from the imporer
hcl = importer.HCLd()

for k in hcl:
    with open(f"tf-{k}.tf", "w") as f:
        f.write(hcl[k])

