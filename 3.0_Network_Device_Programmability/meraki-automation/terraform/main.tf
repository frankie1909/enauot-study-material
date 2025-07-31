terraform {
  required_providers {
    meraki = {
      source  = "cisco-open/meraki"
      version = "1.1.7-beta"
    }
  }
}

provider "meraki" {}

resource "meraki_devices_switch_ports" "ap_port" {
  serial  = var.switch_serial
  port_id = var.port_number

  name          = "AP Bootstrap Port"
  enabled       = true
  type          = "trunk"
  vlan          = var.native_vlan_bootstrap
  allowed_vlans = var.allowed_vlans_bootstrap
  rstp_enabled  = true
  stp_guard     = "disabled"
}
