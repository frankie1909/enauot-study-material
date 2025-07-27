from netmiko import ConnectHandler

# Cisco DevNet Always-On IOS XE C9K Sandbox
device = {
    "device_type": "cisco_ios",
    "host": "devnetsandboxiosxec9k.cisco.com",
    "username": "silvan.luschnig",
    "password": "-G23aq5bR4_By",
    "port": 22,
}

try:
    print("[*] Connecting to device...")
    net_connect = ConnectHandler(**device)
    print("[+] Connection established!")

    # Basic monitoring command
    print("\n[*] Running 'show ip interface brief'...\n")
    output = net_connect.send_command("show ip interface brief")
    print(output)

    # Optional: Run config check
    print("\n[*] Running 'show version'...\n")
    version_output = net_connect.send_command("show version")
    print(version_output)

    # run show run
    print("\n[+] Runnin 'show run ....\n")
    running_config_output = net_connect.send_command("show run")
    print(running_config_output)

    # Close connection
    net_connect.disconnect()
    print("\n[+] Disconnected successfully.")

except Exception as e:
    print(f"[!] An error occurred: {e}")
