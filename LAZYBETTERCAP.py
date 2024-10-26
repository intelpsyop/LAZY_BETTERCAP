import subprocess

class LazyBettercap:
    def __init__(self):
        self.banner()

    def banner(self):
        print("Welcome to LAZY BETTERCAP\nAutomate Bettercap tasks with ease!")
        print("\nAvailable modules:")
        print(" - net.probe: Network device discovery")
        print(" - arp.spoof: ARP Spoofing attack")
        print(" - dns.spoof: DNS Spoofing attack")
        print(" - dhcp6.spoof: DHCPv6 Spoofing attack")
        print(" - http.proxy: HTTP Proxy for traffic manipulation")
        print(" - https.proxy: HTTPS Proxy for traffic manipulation")
        print(" - sniffer: Packet capture and analysis")
        print(" - wifi: WiFi attacks and monitoring")
        print(" - ble: Bluetooth Low Energy attacks")
        print(" - hid.injector: HID USB attacks (BadUSB)")
        print(" - beef: BeEF-XSS integration")
        print(" - events.stream: Live event monitoring")
        print("\nExamples of usage:")
        print(" - start net.probe")
        print(" - start arp.spoof --target 192.168.1.100")
        print(" - stop all")
        print("Type 'help' for more options.\n")

    def execute(self, command):
        """
        Executes the Bettercap command via subprocess.
        """
        print(f"\nExecuting command: {command}\n")
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        if process.returncode == 0:
            print(output.decode())
        else:
            print(f"Error: {error.decode()}")

    def start_module(self, module_name, params=""):
        """
        Dynamically builds and executes Bettercap commands based on the selected module and optional parameters.
        """
        cmd = f'bettercap -eval "{module_name} on; {params}"'
        self.execute(cmd)

    def stop_module(self, module_name):
        """
        Stops a specific Bettercap module.
        """
        cmd = f'bettercap -eval "{module_name} off;"'
        self.execute(cmd)

    def stop_all(self):
        """
        Stops all active Bettercap modules.
        """
        cmd = 'bettercap -eval "net.sniff off; arp.spoof off; dns.spoof off; dhcp6.spoof off; http.proxy off; https.proxy off;"'
        self.execute(cmd)

    def run(self):
        while True:
            user_input = input("LAZY BETTERCAP> ").strip().lower()

            if user_input.startswith("start"):
                parts = user_input.split()
                module = parts[1]

                # Handling optional parameters, like targets
                params = ""
                if "--target" in user_input:
                    target_index = user_input.index("--target") + 8
                    target = user_input[target_index:].split()[0]
                    if module == "arp.spoof":
                        params = f"set arp.spoof.targets {target};"
                    elif module == "dns.spoof":
                        params = f"set dns.spoof.all true;"

                self.start_module(module, params)

            elif user_input.startswith("stop"):
                parts = user_input.split()
                if len(parts) == 2:
                    module = parts[1]
                    self.stop_module(module)
                elif parts[1] == "all":
                    self.stop_all()
                    
            elif user_input == "exit":
                print("Exiting LAZY BETTERCAP...")
                break

            elif user_input == "help":
                self.banner()
            else:
                print("Invalid command. Type 'help' for usage.")

if __name__ == "__main__":
    lazy_bettercap = LazyBettercap()
    lazy_bettercap.run()
