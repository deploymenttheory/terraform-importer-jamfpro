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


# Create an options object containing your exclusions
opts = jamftf.Options(exclude_ids=exclude)

# Define resources, validation setting and attach options defined earlier
scripts = jamftf.Scripts(validate=True, options=opts)
categories = jamftf.Categories(validate=False, options=opts)

# Create a new importer using the Jamf Resources you have made above
importer = jamftf.Importer(CLIENT, targetted=[categories, scripts])

# Generate HCL from the imporer
hcl = importer.HCL()

