variable "api_key" {
  type        = string
  description = "Meraki Dashboard API key"
}

variable "org_id" {
  type        = string
  description = "Meraki organization ID"
}

variable "network_id" {
  type        = string
  description = "Network ID where the switch exists"
}

variable "switch_serial" {
  type        = string
  description = "Serial number of the switch the AP connects to"
}

variable "port_number" {
  type        = string
  description = "Port number on the switch to configure"
}

variable "native_vlan_bootstrap" {
  type        = number
  default     = 3165
}

variable "allowed_vlans_bootstrap" {
  type        = string
  default     = "3165"
}
