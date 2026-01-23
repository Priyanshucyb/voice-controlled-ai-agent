import subprocess
import time

ADB_PATH = r"C:\Users\coret\Downloads\scrcpy-win64-v3.3.4\scrcpy-win64-v3.3.4\adb.exe"


def run_action(action: dict):
    act = action.get("action")

    try:
        # WIFI
        if act == "WIFI_OFF":
            subprocess.run([ADB_PATH, "shell", "svc", "wifi", "disable"], check=True)
            return "[REAL] WiFi OFF"

        if act == "WIFI_ON":
            subprocess.run([ADB_PATH, "shell", "svc", "wifi", "enable"], check=True)
            return "[REAL] WiFi ON"

        # DATA
        if act == "DATA_OFF":
            subprocess.run([ADB_PATH, "shell", "svc", "data", "disable"], check=True)
            return "[REAL] Data OFF"

        if act == "DATA_ON":
            subprocess.run([ADB_PATH, "shell", "svc", "data", "enable"], check=True)
            return "[REAL] Data ON"

        # DND – METHOD 1 (zen_mode)
        if act == "DND_ON":
            subprocess.run([ADB_PATH, "shell", "settings", "put", "global", "zen_mode", "1"], check=True)
            return "[REAL] DND ON (zen_mode)"

        if act == "DND_OFF":
            subprocess.run([ADB_PATH, "shell", "settings", "put", "global", "zen_mode", "0"], check=True)
            return "[REAL] DND OFF (zen_mode)"

        # SILENT MODE – METHOD 2 (notification service)
        if act == "SILENT_ON":
            subprocess.run([ADB_PATH, "shell", "cmd", "notification", "set_dnd", "priority"], check=True)
            return "[REAL] Silent mode ON"

        if act == "SILENT_OFF":
            subprocess.run([ADB_PATH, "shell", "cmd", "notification", "set_dnd", "off"], check=True)
            return "[REAL] Silent mode OFF"

        # FLASH (QS toggle – OEM dependent)
        if act == "FLASH_TOGGLE":
            subprocess.run([ADB_PATH, "shell", "cmd", "statusbar", "expand-settings"], check=True)
            time.sleep(1.2)
            subprocess.run([ADB_PATH, "shell", "input", "tap", "540", "1700"], check=True)
            return "[REAL] Flash toggle attempted"

        # CALL
        if act == "MAKE_CALL":
            n = action.get("number")
            subprocess.run(
                [ADB_PATH, "shell", "am", "start",
                 "-a", "android.intent.action.DIAL",
                 "-d", f"tel:{n}"],
                check=True
            )
            return "[REAL] Dialer opened"

        # CHROME SEARCH
        if act == "OPEN_CHROME_SEARCH":
            q = action.get("query", "google").replace(" ", "%20")
            subprocess.run(
                [ADB_PATH, "shell", "am", "start",
                 "-a", "android.intent.action.VIEW",
                 "-d", f"https://www.google.com/search?q={q}",
                 "com.android.chrome"],
                check=True
            )
            return "[REAL] Chrome search opened"

        # YOUTUBE
        if act == "OPEN_YOUTUBE":
            q = action.get("query", "music").replace(" ", "%20")
            subprocess.run(
                [ADB_PATH, "shell", "am", "start",
                 "-a", "android.intent.action.VIEW",
                 "-d", f"https://www.youtube.com/results?search_query={q}"],
                check=True
            )
            return "[REAL] YouTube opened"

        # SCREENSHOT
        if act == "TAKE_SCREENSHOT":
            f = f"/sdcard/screenshot_{int(time.time())}.png"
            subprocess.run([ADB_PATH, "shell", "screencap", "-p", f], check=True)
            return "[REAL] Screenshot saved"

        # TRAIN
        if act == "OPEN_TRAIN_APP":
            pkg = action.get("package")
            subprocess.run(
                [ADB_PATH, "shell", "monkey", "-p", pkg,
                 "-c", "android.intent.category.LAUNCHER", "1"],
                check=True
            )
            return "[REAL] Train app opened"

    except Exception as e:
        return f"[ERROR] {e}"

    return "[MOCK] No action"
