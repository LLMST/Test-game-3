#!/usr/bin/env python3
import re, sys

manifest_path = "android/app/src/main/AndroidManifest.xml"

with open(manifest_path, "r") as f:
    content = f.read()

# Add permissions before </manifest>
permissions = ["INTERNET", "ACCESS_NETWORK_STATE"]
if permissions:
    perm_lines = "\n".join(f'    <uses-permission android:name="android.permission.{p}" />' for p in permissions)
    content = content.replace("</manifest>", perm_lines + "\n</manifest>")

# Set screen orientation on main activity
orientation = "landscape"
if 'android:screenOrientation=' in content:
    content = re.sub(r'android:screenOrientation="[^"]*"', f'android:screenOrientation="{orientation}"', content)
else:
    content = content.replace("<activity", f'<activity android:screenOrientation="{orientation}"', 1)

# Set fullscreen theme
if "Theme.NoTitleBar.Fullscreen" not in content:
    content = content.replace("<activity", '<activity android:theme="@android:style/Theme.NoTitleBar.Fullscreen"', 1)

with open(manifest_path, "w") as f:
    f.write(content)

print("Post-sync complete")
