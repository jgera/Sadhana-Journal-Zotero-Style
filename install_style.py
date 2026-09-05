"""
Zotero CSL Style Installer
==========================
Robust, cross-platform utility to install CSL citation styles directly into Zotero.

Features:
- Auto-detects custom Zotero data directory from prefs.js (or default ~/Zotero)
- Validates CSL XML well-formedness and extracts metadata
- Checks for known collision bugs (e.g., Zotero renamed-styles.json)
- Detects if Zotero is running and prompts for restart
- Works on Windows, macOS, and Linux
"""

import os
import sys
import shutil
import re
import glob
import platform
import xml.etree.ElementTree as ET
import subprocess


def log_info(msg):
    print(f"[INFO] {msg}")


def log_success(msg):
    print(f"[SUCCESS] {msg}")


def log_warn(msg):
    print(f"[WARNING] {msg}")


def log_error(msg):
    print(f"[ERROR] {msg}")


def get_zotero_profiles_dir():
    system = platform.system()
    home = os.path.expanduser("~")
    if system == "Windows":
        app_data = os.environ.get("APPDATA")
        if app_data:
            return os.path.join(app_data, "Zotero", "Zotero", "Profiles")
    elif system == "Darwin":
        return os.path.join(home, "Library", "Application Support", "Zotero", "Profiles")
    else:  # Linux / Unix
        return os.path.join(home, ".zotero", "zotero")
    return None


def detect_zotero_data_dir():
    """Detects the active Zotero data directory from prefs.js or falls back to ~/Zotero."""
    home = os.path.expanduser("~")
    default_dir = os.path.join(home, "Zotero")

    profiles_dir = get_zotero_profiles_dir()
    if profiles_dir and os.path.isdir(profiles_dir):
        prefs_files = glob.glob(os.path.join(profiles_dir, "*", "prefs.js"))
        for prefs_file in prefs_files:
            try:
                with open(prefs_file, "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        # Match: user_pref("extensions.zotero.dataDir", "C:\\Users\\...\\Zotero");
                        match = re.search(r'user_pref\(\s*["\']extensions\.zotero\.dataDir["\']\s*,\s*["\'](.*?)["\']\s*\)', line)
                        if match:
                            custom_dir = match.group(1).replace("\\\\", "\\")
                            if os.path.isdir(custom_dir):
                                return os.path.abspath(custom_dir)
            except Exception:
                pass

    if os.path.isdir(default_dir):
        return os.path.abspath(default_dir)

    return None


def is_zotero_running():
    """Checks whether Zotero application is currently running."""
    system = platform.system()
    try:
        if system == "Windows":
            out = subprocess.check_output("tasklist /FI \"IMAGENAME eq zotero.exe\" /NH", shell=True, text=True, errors="ignore")
            return "zotero.exe" in out.lower()
        else:
            out = subprocess.check_output(["pgrep", "-i", "zotero"], text=True, errors="ignore")
            return len(out.strip()) > 0
    except Exception:
        return False


def validate_csl_file(csl_path):
    """Validates CSL file syntax and extracts title, ID, and filename."""
    if not os.path.isfile(csl_path):
        raise FileNotFoundError(f"CSL file not found at: {csl_path}")

    try:
        tree = ET.parse(csl_path)
    except ET.ParseError as e:
        raise ValueError(f"Invalid XML syntax in CSL file: {e}")

    root = tree.getroot()
    ns = {"csl": "http://purl.org/net/xbiblio/csl"}

    title_elem = root.find(".//csl:info/csl:title", ns)
    id_elem = root.find(".//csl:info/csl:id", ns)

    if title_elem is None or not title_elem.text:
        raise ValueError("CSL file is missing <title> in <info> section.")
    if id_elem is None or not id_elem.text:
        raise ValueError("CSL file is missing <id> in <info> section.")

    title = title_elem.text.strip()
    style_id = id_elem.text.strip()

    # Check for legacy collision
    if style_id.strip("/").endswith("/styles/sadhana"):
        log_warn("Style ID ends with '/styles/sadhana'. This causes Zotero to treat it as deprecated.")

    # Generate a clean filename from ID
    id_slug = style_id.split("/")[-1]
    if not id_slug.endswith(".csl"):
        id_slug += ".csl"

    return title, style_id, id_slug


def install_style(csl_path=None):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if not csl_path:
        default_candidates = [
            os.path.join(script_dir, "sadhana-journal.csl"),
            os.path.join(script_dir, "sadhana.csl"),
        ]
        for candidate in default_candidates:
            if os.path.isfile(candidate):
                csl_path = candidate
                break

    if not csl_path or not os.path.isfile(csl_path):
        log_error("Could not find a .csl file to install. Please provide the path to the style file.")
        sys.exit(1)

    log_info(f"Source style file: {csl_path}")

    # Validate CSL
    try:
        title, style_id, id_slug = validate_csl_file(csl_path)
        log_info(f"Style Title : {title}")
        log_info(f"Style ID    : {style_id}")
    except Exception as e:
        log_error(f"Validation failed: {e}")
        sys.exit(1)

    # Locate Zotero styles directory
    zotero_data_dir = detect_zotero_data_dir()
    if not zotero_data_dir:
        home = os.path.expanduser("~")
        zotero_data_dir = os.path.join(home, "Zotero")
        log_warn(f"Zotero directory not auto-detected. Attempting default path: {zotero_data_dir}")

    styles_dir = os.path.join(zotero_data_dir, "styles")
    try:
        os.makedirs(styles_dir, exist_ok=True)
    except Exception as e:
        log_error(f"Failed to create styles directory '{styles_dir}': {e}")
        sys.exit(1)

    # Destination paths: both the id_slug and the source filename for convenience
    dest_path = os.path.join(styles_dir, id_slug)
    try:
        shutil.copyfile(csl_path, dest_path)
        log_success(f"Installed style to: {dest_path}")
    except Exception as e:
        log_error(f"Failed to copy style: {e}")
        sys.exit(1)

    # Check running process
    if is_zotero_running():
        print("\n" + "=" * 65)
        log_warn("Zotero is currently running!")
        log_info("Please restart Zotero (close and re-open it) for the new style to appear in:")
        log_info("  Edit > Settings > Cite > Style Manager")
        print("=" * 65 + "\n")
    else:
        print("\n" + "=" * 65)
        log_success("Style installed successfully!")
        log_info("Open Zotero > Settings > Cite > Style Manager to see:")
        log_info(f"  '{title}'")
        print("=" * 65 + "\n")


if __name__ == "__main__":
    csl_arg = sys.argv[1] if len(sys.argv) > 1 else None
    install_style(csl_arg)
