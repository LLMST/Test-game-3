#!/bin/bash
set -e

for SIZE_DIR in mipmap-mdpi mipmap-hdpi mipmap-xhdpi mipmap-xxhdpi mipmap-xxxhdpi; do
  TARGET="android/app/src/main/res/$SIZE_DIR"
  mkdir -p "$TARGET"
  cp "resources/android/icon/$SIZE_DIR/ic_launcher.png" "$TARGET/ic_launcher.png"
  cp "resources/android/icon/$SIZE_DIR/ic_launcher_round.png" "$TARGET/ic_launcher_round.png"
  cp "resources/android/icon/$SIZE_DIR/ic_launcher_foreground.png" "$TARGET/ic_launcher_foreground.png"
done

echo "Icons copied"