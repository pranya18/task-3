import modules.port_scanner as port_scanner
import modules.banner_grabber as banner_grabber
import modules.password_tester as password_tester
import modules.net_info as net_info

def main():
    print("\n=== Python Penetration Testing Toolkit ===")
    print("1. Port Scanner")
    print("2. Banner Grabber")
    print("3. Password Strength Tester")
    print("4. Network Info")
    choice = input("Select a module: ")

    if choice == "1":
        target = input("Enter target host (e.g., 127.0.0.1): ")
        port_scanner.scan_ports(target)
    elif choice == "2":
        host = input("Enter host: ")
        port = int(input("Enter port: "))
        banner_grabber.grab_banner(host, port)
    elif choice == "3":
        password = input("Enter a password to test: ")
        password_tester.test_password(password)
    elif choice == "4":
        net_info.show_info()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
