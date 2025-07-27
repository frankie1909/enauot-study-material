from netmiko import ConnectHandler
from time import sleep

# Cisco IOS XE Always-On Sandbox device info
device = {
    "device_type": "cisco_ios",
    "host": "devnetsandboxiosxec9k.cisco.com",
    "username": "silvan.luschnig",
    "password": "-G23aq5bR4_By",
    "port": 22,
}


loopback_interface = "Loopback99"
loopback_ip = "192.168.99.99"
loopback_mask = "255.255.255.255"

loopback_config = [
    f"interface {loopback_interface}",
    "description Created by Netmiko",
    f"ip address {loopback_ip} {loopback_mask}",
    "no shutdown"
]

try:
    print("[*] Connecting...")
    connection = ConnectHandler(**device)
    print("[+] Connected to device.")

    print("[*] Entering config mode and sending commands...")
    output = connection.send_config_set(loopback_config)
    print(output)

    sleep(1)  # Short delay to let config settle

    print("[*] Verifying IP assignment on the loopback...")
    verify_output = connection.send_command("show ip interface brief | include Loopback99")
    print(verify_output)

    if loopback_ip in verify_output:
        print(f"[✅] Success: {loopback_interface} has IP {loopback_ip}")
    else:
        print("[❌] IP address not correctly applied.")

    connection.disconnect()
    print("[+] Session closed.")

except Exception as e:
    print(f"[!] Error: {e}")