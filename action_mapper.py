def map_action(intent: str, text: str):
    t = text.lower().replace("-", "").strip()

    # ================= SETTINGS =================
    if intent == "SETTINGS":

        # WIFI
        if "wifi" in t and ("off" in t or "band" in t):
            return {"action": "WIFI_OFF"}
        if "wifi" in t and ("on" in t or "chalu" in t):
            return {"action": "WIFI_ON"}

        # MOBILE DATA
        if ("data" in t or "internet" in t) and ("off" in t or "band" in t):
            return {"action": "DATA_OFF"}
        if ("data" in t or "internet" in t) and ("on" in t or "chalu" in t):
            return {"action": "DATA_ON"}

        # DND (keep both)
        if ("dnd" in t or "do not disturb" in t) and ("on" in t or "chalu" in t):
            return {"action": "DND_ON"}
        if ("dnd" in t or "do not disturb" in t) and ("off" in t or "band" in t):
            return {"action": "DND_OFF"}

        # SILENT MODE (fallback)
        if ("silent" in t or "mute" in t) and ("on" in t or "chalu" in t):
            return {"action": "SILENT_ON"}
        if ("ringer" in t or "sound" in t) and ("on" in t or "chalu" in t):
            return {"action": "SILENT_OFF"}

        # FLASH (best-effort)
        if "flash" in t or "torch" in t:
            return {"action": "FLASH_TOGGLE"}

    # ================= CALL =================
    if intent == "CALL":
        num = "".join(c for c in t if c.isdigit())
        if num:
            return {"action": "MAKE_CALL", "number": num}

    # ================= BROWSER (CHROME SEARCH) =================
    if intent == "BROWSER":
        q = (
            t.replace("chrome", "")
             .replace("browser", "")
             .replace("search", "")
             .replace("karo", "")
             .replace("open", "")
             .strip()
        )
        return {"action": "OPEN_CHROME_SEARCH", "query": q or "google"}

    # ================= YOUTUBE =================
    if intent == "MEDIA":
        q = (
            t.replace("youtube", "")
             .replace("pe", "")
             .replace("par", "")
             .replace("per", "")
             .replace("chalao", "")
             .replace("play", "")
             .strip()
        )
        return {"action": "OPEN_YOUTUBE", "query": q or "music"}

    # ================= SCREENSHOT =================
    if intent == "SYSTEM":
        return {"action": "TAKE_SCREENSHOT"}

    # ================= TRAIN =================
    if intent == "TRAVEL":
        return {"action": "OPEN_TRAIN_APP", "package": "com.whereismytrain.android"}

    return {"action": "NO_ACTION"}
