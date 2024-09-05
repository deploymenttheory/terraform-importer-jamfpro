import jamftf
import jamfpy
import os

ENV_KEYS = {
    "tenant_id": "JAMFTF_JPRO_TENANT_ID",
    "client_id": "JPRO_CLIENT_ID",
    "client_secret": "JPRO_CLIENT_SECRET",
    "config_file_path": "JAMFTF_CONFIG_FP",
    "output_dir": "JAMFTF_OUTPUT_DIR",
    "debug_mode": "JAMFTF_DEBUG_MODE"
}

def env_vars() -> dict:
    out = {}
    for j, k in ENV_KEYS.items():
        val = os.environ.get(k)

        if val is None or val == "":
            raise KeyError("missing environment var: %s", k)
        
        out[j] = val

    return out

ENV = env_vars()

def get_client():
    level = 20
    if bool(ENV["debug_mode"]):
        level = 10
    
    return jamfpy.init_client(
        tenant_name=ENV["tenant_id"],
        client_id=ENV["client_id"],
        client_secret=ENV["client_secret"],
        logging_level=level
    )


def get_hcl() -> dict:
    target_resources = jamftf.parse_config_file(ENV["config_file_path"])

    importer = jamftf.Importer(
        client=get_client(),
        targetted=target_resources,
        debug=bool(ENV["debug_mode"])
    )

    return importer.HCLd()


def write_out(hcl_dict: dict) -> None:
    """something"""
    for k, v in hcl_dict.items():

        output_fn = k + ".tf"
        full_path = f"{ENV['output_dir']}/{output_fn}"

        with open(full_path, "w", encoding="UTF-8") as f:
            f.write(v)

def main():
    write_out(get_hcl())

if __name__ == "__main__":
    main()
        
    
