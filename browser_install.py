""" Import necessary modules for the program to work """
import subprocess

""" Install whichever browser the user selected from browser_select_screen """
def install_browser(selected_browser):
    browser_map = {
        "Chrome": "Google.Chrome",
        "Brave": "Brave.Brave",
        "Firefox": "Mozilla.Firefox",
        "Librewolf": "Librewolf.Librewolf"
    }

    if selected_browser not in browser_map:
        print(f"Unknown browser selected: {selected_browser}")
        return

    browser_id = browser_map[selected_browser]
    
    for app, app_id in [("Browser", browser_id), ("VLC Media Player", "VideoLAN.VLC")]:
        print(f"Installing {app} via Winget...")
        try:
            subprocess.run(
                ["winget", "install", app_id, "--silent", "--accept-package-agreements", "--accept-source-agreements"],
                check=True
            )
            print(f"{app} installation completed.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {app}: {e}")
