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


opts = jamftf.Options(use_resource_type_as_name=False)
# scripts = jamftf.Scripts(validate=True, exclude=[7724, 7723, 7761, 7759, 7725, 7760], options=opts)
# importer = jamftf.Importer(CLIENT, targetted=[scripts], debug=True)

# hcl = importer.HCL()
# print(hcl)

print(opts.options())
