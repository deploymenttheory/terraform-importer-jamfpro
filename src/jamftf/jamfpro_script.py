import jamfpy

from .resource_types import RESOURCE_TYPE_SCRIPT
from .hcl import generate_imports

class Resource:
    def __init__(self, client: jamfpy.JamfTenant, use_jamf_name: bool = False):
        self.use_jamf_name = use_jamf_name
        self.client = client

class Script(Resource):
    resource_type = RESOURCE_TYPE_SCRIPT

    # Priv
    def _get(self, exclude: list = []):  
        out = []
        resp, data = self.client.pro.scripts.get_all()

        if not resp.ok:
            raise Exception("bad api call")
        
        count = 0
        for i in data:
            if i["id"] not in exclude:
                if self.use_jamf_name:
                    name = i["name"]
                else:
                    name = f"{self.resource_type.split('_', 1)[1]}-{count}"

                out.append({
                    "id": i["id"],
                    "name": name
                })

                count += 1
        
        return out
    

    # Public
    def HCL(self):
        return generate_imports({
            "resource_type": self.resource_type,
            "resources": self._get()
        })


        
