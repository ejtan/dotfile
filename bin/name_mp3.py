#! /usr/bin/env python3

# Script to rename .mp3 tracks to a specified format

from mutagen.id3 import ID3
import os
import sys
import re


def get_track_number(track_data):
    return track_data["TRCK"].text[0].split("/")[0].zfill(2)


def get_track_title(track_data):
    return re.sub(r"\s*/\s*", "-", track_data["TIT2"].text[0])


def rename_files(music_dir):
    for album_dir in os.listdir(music_dir):
        album_path = os.path.join(music_dir, album_dir)

        for track in os.listdir(album_path):
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
    if len(sys.argv) == 1:
        rename_files(os.path.expanduser("~/Music"))
    elif len(sys.argv) == 2:
        rename_files(sys.argv[1])

if __name__ == "__main__":
    main()
