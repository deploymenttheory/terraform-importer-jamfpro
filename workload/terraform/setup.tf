terraform {
  cloud {

    organization = "thejoeker"

    workspaces {
      name = "lbgsandbox"
    }
  }

  required_providers {
    jamfpro = {
      source  = "deploymenttheory/jamfpro"
      version = "0.1.9"
    }
  }
}

provider "jamfpro" {
  jamfpro_instance_fqdn = "https://lbgsandbox.jamfcloud.com"
  auth_method = "oauth2"
  client_id = var.jamfpro_client_id
  client_secret = var.jamfpro_client_secret
  enable_client_sdk_logs = false
  jamfpro_load_balancer_lock = true
}

variable "jamfpro_client_id" {
  description = "The Jamf Pro Client ID for authentication."
  sensitive   = true
  default     = ""
}

variable "jamfpro_client_secret" {
  description = "The Jamf Pro Client Secret for authentication."
  sensitive   = true
  default     = ""
}