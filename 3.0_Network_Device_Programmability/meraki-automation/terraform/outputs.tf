output "ap_port_id" {
  value       = meraki_devices_switch_ports.ap_port.port_id
  description = "The switch port ID used for the AP"
}

output "ap_switch_serial" {
  value       = meraki_devices_switch_ports.ap_port.serial
  description = "The switch serial number used"
}
