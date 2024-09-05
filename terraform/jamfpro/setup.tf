terraform {
  cloud {
    organization = get
    workspaces {
      name = var.TF_WORKSPACE_ID
    }
  }

  required_providers {
    jamfpro = {
      source  = "deploymenttheory/jamfpro"
      version = "0.2.0"
    }
  }
}

provider "jamfpro" {
  jamfpro_instance_fqdn = var.jamfpro_instance_fqdn
  auth_method = "oauth2"
  client_id = var.jamfpro_client_id
  client_secret = var.jamfpro_client_secret
  enable_client_sdk_logs = false
  jamfpro_load_balancer_lock = true
}

variable "jamfpro_client_id" {
  description = "The Jamf Pro Client ID for authentication."
  sensitive   = true
  default     = env("JAMFTF_CLIENT_ID")
}

variable "jamfpro_client_secret" {
  description = "The Jamf Pro Client Secret for authentication."
  sensitive   = true
  default     = env("JAMFTF_CLIENT_SEFRET")
}

variable "jamfpro_instance_fqdn" {
  default = env("JAMFTF_PRO_TENANT_ID")
}

variable "tf_workspace" {
  default = env("TF_WORKSPACE_ID")
  
}