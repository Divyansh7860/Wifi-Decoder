import subprocess

def get_wifi_profiles():
    """Fetches all Wi-Fi profiles from the system."""
    try:
        command_output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        profiles = [line.split(":")[1].strip() for line in command_output if "All User Profile" in line]
        return profiles
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving Wi-Fi profiles: {e}")
        return []

def get_profile_password(profile):
    """Fetches the password for a given Wi-Fi profile."""
    try:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
        passwords = [line.split(":")[1].strip() for line in result if "Key Content" in line]
        return passwords[0] if passwords else ""
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving password for profile {profile}: {e}")
        return ""

def main():
    profiles = get_wifi_profiles()
    if not profiles:
        print("No Wi-Fi profiles found.")
        return

    print("{:<30} | {:<}".format("Profile Name", "Password"))
    print("-" * 50)
    
    for profile in profiles:
        password = get_profile_password(profile)
        print("{:<30} | {:<}".format(profile, password))

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()