def detect_intent(text: str):
    t = text.lower().replace("-", "").strip()

    if (
        "wifi" in t
        or "data" in t
        or "internet" in t
        or "dnd" in t
        or "do not disturb" in t
        or "silent" in t
        or "mute" in t
        or "ringer" in t
        or "sound" in t
        or "flash" in t
        or "torch" in t
    ):
        return "SETTINGS"

    if "call" in t:
        return "CALL"

    if "youtube" in t:
        return "MEDIA"

    if "chrome" in t or "browser" in t or "search" in t:
        return "BROWSER"

    if "screenshot" in t or "screen shot" in t:
        return "SYSTEM"

    if "train" in t or "rail" in t:
        return "TRAVEL"

    return "GENERAL"
