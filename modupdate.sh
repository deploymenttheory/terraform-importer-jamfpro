jamftf_target_version=main
jamfpy_target_version=main

########
cd /Users/joseph/github/importer-terraform-jamfpro
jamftf_url="https://github.com/deploymenttheory/jamftf-python-terraform-importer"
jamfpy_url="https://github.com/thejoeker12/jamfpy"

jamftf_pip_target="git+$jamftf_url@$jamftf_target_version"
jamfpy_pip_target="git+$jamfpy_url@$jamfpy_target_version"


# pip uninstall jamftf --no-input
# pip uninstall jamfpy --no-input

pip install $jamftf_pip_target
pip install $jamfpy_pip_target