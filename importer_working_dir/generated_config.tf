# __generated__ by Terraform
# Please review these resources and move them into your main configuration files.

# __generated__ by Terraform from "300"
resource "jamfpro_category" "jamfpro_category_0" {
  name     = "Aerospace"
  priority = 9
}

# __generated__ by Terraform from "299"
resource "jamfpro_category" "jamfpro_category_2" {
  name     = "Facilities"
  priority = 9
}

# __generated__ by Terraform from "297"
resource "jamfpro_category" "jamfpro_category_3" {
  name     = "Finance"
  priority = 9
}

# __generated__ by Terraform from "292"
resource "jamfpro_category" "jamfpro_category_4" {
  name     = "HR"
  priority = 9
}

# __generated__ by Terraform from "296"
resource "jamfpro_category" "jamfpro_category_5" {
  name     = "Legal"
  priority = 9
}

# __generated__ by Terraform from "298"
resource "jamfpro_category" "jamfpro_category_6" {
  name     = "Marketing"
  priority = 9
}

# __generated__ by Terraform from "294"
resource "jamfpro_category" "jamfpro_category_7" {
  name     = "Operations"
  priority = 9
}

# __generated__ by Terraform from "293"
resource "jamfpro_category" "jamfpro_category_8" {
  name     = "Security"
  priority = 9
}

# __generated__ by Terraform from "12"
resource "jamfpro_policy" "jamfpro_policy_0" {
  category_id                   = -1
  enabled                       = false
  frequency                     = "Once per computer"
  name                          = "tf-demo-policy-script-demo"
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
      id          = jsonencode(18)
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
    building_ids       = [107]
    computer_group_ids = []
    computer_ids       = []
    department_ids     = []
    jss_user_group_ids = []
    jss_user_ids       = []
  }
}

# __generated__ by Terraform from "15"
resource "jamfpro_script" "jamfpro_script_0" {
  category_id     = jsonencode(-1)
  info            = "Adds target user or group to specified group membership, or removes said membership."
  name            = "tf-demo-v2-script-1"
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

# __generated__ by Terraform from "18"
resource "jamfpro_script" "jamfpro_script_1" {
  category_id     = jsonencode(-1)
  info            = "Adds target user or group to specified group membership, or removes said membership."
  name            = "tf-demo-v2-script-2"
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

# __generated__ by Terraform from "17"
resource "jamfpro_script" "jamfpro_script_2" {
  category_id     = jsonencode(-1)
  info            = "Adds target user or group to specified group membership, or removes said membership."
  name            = "tf-demo-v2-script-3"
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

# __generated__ by Terraform from "16"
resource "jamfpro_script" "jamfpro_script_3" {
  category_id     = jsonencode(-1)
  info            = "Adds target user or group to specified group membership, or removes said membership."
  name            = "tf-demo-v2-script-4"
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

# __generated__ by Terraform from "14"
resource "jamfpro_script" "jamfpro_script_4" {
  category_id     = jsonencode(-1)
  info            = "Adds target user or group to specified group membership, or removes said membership."
  name            = "tf-demo-v2-script-5"
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
