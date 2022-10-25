from pathlib import Path

import click
import eyed3

@click.command()
@click.option("--input-dir", prompt="Input directory", help="Directory containing music files to organize.")
@click.option("--artist", help="Artist to set")
@click.option("--album-artist", help="Album Artist to set")
@click.option("--album", help="Album to set")
def fix(input_dir, artist, album_artist, album):
    input = Path(input_dir)
    print(f"Setting tags in {input_dir}")

    for filename in input.glob("**/*.mp3"):
        audiofile = eyed3.load(filename)
        if artist:
            print(f"Setting artist to {artist} for {filename}")
            audiofile.tag.artist = artist
            audiofile.tag.save()
        if album_artist:
            print(f"Setting album artist to {album_artist} for {filename}")
            audiofile.tag.album_artist = album_artist
            audiofile.tag.save()
        if album:
            print(f"Setting album to {album} for {filename}")
            audiofile.tag.album = album
            audiofile.tag.save()



if __name__ == '__main__':
    fix()