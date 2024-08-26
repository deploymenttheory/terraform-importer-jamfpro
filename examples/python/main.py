import jamftf
import jamfpy
import os

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


# Options setup
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


# Options
opts = jamftf.Options(exclude_ids=exclude)

# Scripts
scripts = jamftf.Scripts(validate=True, options=opts)

# Categories
categories = jamftf.Categories(validate=False, options=opts)


# Importer
importer = jamftf.Importer(CLIENT, targetted=[categories, scripts])

# HCL
print(importer.HCL())

