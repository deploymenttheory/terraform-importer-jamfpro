import jamftf
import jamfpy
import os

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

script_options = jamftf.Options(use_resource_type_as_name=False)

importer = jamftf.Importer(CLIENT, targetted=[
    jamftf.Scripts(options=script_options),
    jamftf.Categories()
])


print(importer.HCL())