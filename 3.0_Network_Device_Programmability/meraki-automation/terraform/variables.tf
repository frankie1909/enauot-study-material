variable "api_key" {
  type        = string
  description = "Meraki Dashboard API key"
  sensitive   = true
}

variable "org_id" {
  type        = string
  description = "Meraki organization ID"
}

variable "network_id" {
  type        = string
  description = "Meraki network ID"
}

variable "switch_serial" {
  type        = string
  description = "Switch serial number"
}

variable "port_number" {
  type        = string
  description = "Port number (e.g. '47')"
}

variable "native_vlan_bootstrap" {
  type        = number
  default     = 3165
}

variable "allowed_vlans_bootstrap" {
  type        = string
  default     = "3165"
}
