#! /usr/bin/env python3

# Script to rename .mp3 tracks to a specified format

from mutagen.id3 import ID3
import os
import sys
import re
import argparse


def rename_files(music_dir):
    for root, dirs, files in os.walk(music_dir):
        album_path = root
        for track in files:
            if track.endswith('.mp3'):
                original_filename = os.path.join(album_path, track)
                track_data = ID3(original_filename)

                # Grab track number and pad zeros if needed
                track_num = track_data["TRCK"].text[0].split("/")[0].zfill(2)

                # Grab track title and strip "/" if it is in the track title
                track_title = re.sub(r"\s*/\s*", "-", track_data["TIT2"].text[0])

                # Generate filepath
                filename = track_num + ". " + track_title + ".mp3"
                target_filename = os.path.join(album_path, filename)

                # Rename
                os.rename(original_filename, target_filename)


def main():
    parser = argparse.ArgumentParser(description="Formats music files into formated filenames.")
    parser.add_argument('dirs', metavar='directory', type=str, nargs='*',
                        help='Input directories', default=['~/Music'])
    args = parser.parse_args()

    for music_dir in args.dirs:
        rename_files(os.path.expanduser(music_dir))


if __name__ == "__main__":
    main()
