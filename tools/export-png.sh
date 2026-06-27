#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

WALLPAPER_SVG="$ROOT_DIR/assets/wallpaper/linxira-wallpaper.svg"
OUTPUT_DIR="$ROOT_DIR/usr/share/wallpapers/LinxiraOS/contents/images"

if [ ! -f "$WALLPAPER_SVG" ]; then
    echo "Error: Wallpaper SVG not found at $WALLPAPER_SVG"
    exit 1
fi

if ! command -v rsvg-convert &> /dev/null; then
    echo "Error: rsvg-convert not found. Install librsvg2-bin:"
    echo "  sudo apt install librsvg2-bin"
    exit 1
fi

mkdir -p "$OUTPUT_DIR"

RESOLUTIONS=("1920x1080" "2560x1440" "3840x2160")

for res in "${RESOLUTIONS[@]}"; do
    width="${res%x*}"
    height="${res#*x}"
    output="$OUTPUT_DIR/${res}.png"
    
    echo "Exporting $res → $output"
    rsvg-convert -w "$width" -h "$height" "$WALLPAPER_SVG" -o "$output"
    
    size=$(stat -f%z "$output" 2>/dev/null || stat -c%s "$output" 2>/dev/null)
    if [ "$size" -lt 10000 ]; then
        echo "  Warning: File size ($size bytes) is suspiciously small"
    fi
done

echo "Done. Exported ${#RESOLUTIONS[@]} resolutions."
