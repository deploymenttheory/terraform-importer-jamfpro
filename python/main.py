import jamftf
import jamfpy
import os

import jamftf.exceptions

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

exclude = [
    7761,
    7759,
    7723,
    7725,
    7724,
    7760
]

cwd = "/Users/joseph/github"
opts = jamftf.Options(exclude_ids=exclude)
scripts = jamftf.Scripts(validate=True, options=opts)
importer = jamftf.Importer(CLIENT, targetted=[scripts])
print(importer.HCL(pretty=False, cwd=cwd))

