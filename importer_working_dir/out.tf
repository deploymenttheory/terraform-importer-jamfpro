# __generated__ by Terraform
# Please review these resources and move them into your main configuration files.

# __generated__ by Terraform from "235"
resource "jamfpro_category" "jamfpro_category_0" {
  name     = "Engineering"
  priority = 9
}

# __generated__ by Terraform from "237"
resource "jamfpro_category" "jamfpro_category_1" {
  name     = "Finance"
  priority = 9
}

# __generated__ by Terraform from "236"
resource "jamfpro_category" "jamfpro_category_2" {
  name     = "HR"
  priority = 9
}

# __generated__ by Terraform from "53"
resource "jamfpro_policy" "jamfpro_policy_0" {
  category_id                   = -1
  enabled                       = false
  frequency                     = "Once per computer"
  name                          = "tf-demo-policy-script-echo"
  network_requirements          = "Any"
  notify_on_each_failed_retry   = false
  offline                       = false
  package_distribution_point    = null
  retry_attempts                = -1
  retry_event                   = "none"
  site_id                       = -1
  target_drive                  = "/"
  trigger_checkin               = false
  trigger_enrollment_complete   = false
  trigger_login                 = false
  trigger_network_state_changed = false
  trigger_other                 = "EVENT"
  trigger_startup               = false
  payloads {
    scripts {
      id          = jsonencode(7785)
      parameter10 = null
      parameter11 = null
      parameter4  = null
      parameter5  = null
      parameter6  = null
      parameter7  = null
      parameter8  = null
      parameter9  = null
      priority    = "After"
    }
  }
  scope {
    all_computers      = false
    all_jss_users      = false
    building_ids       = [1498]
    computer_group_ids = []
    computer_ids       = []
    department_ids     = []
    jss_user_group_ids = []
    jss_user_ids       = []
  }
}

# __generated__ by Terraform from "7785"
resource "jamfpro_script" "jamfpro_script_0" {
  category_id     = jsonencode(-1)
  info            = "Adds target user or group to specified group membership, or removes said membership."
  name            = "tf-demo-encrypt-apfs-volume-v5.0.1"
  notes           = "Jamf Pro script parameters: 4"
  os_requirements = jsonencode(13)
  parameter10     = null
  parameter11     = null
  parameter4      = "/"
  parameter5      = null
  parameter6      = null
  parameter7      = null
  parameter8      = null
  parameter9      = null
  priority        = "BEFORE"
  script_contents = "echo 'hello world'"
}
