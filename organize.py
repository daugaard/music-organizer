from pathlib import Path
from itertools import chain

import click
import tinytag as tinytag
from tinytag import TinyTag

@click.command()
@click.option("--input-dir", prompt="Input directory", help="Directory containing music files to organize.")
@click.option("--output-dir", prompt="Output directory", help="Directory to put organized music files.")
def organize(input_dir, output_dir):
    input = Path(input_dir)
    output = Path(output_dir)
    print(f"Organizing music in {input_dir} into {output_dir}")

    for filename in chain(input.glob("**/*.mp*"), input.glob("**/*.m4a"), input.glob("**/*.wma")):
        try:
            tags = TinyTag.get(filename)
        except tinytag.tinytag.TinyTagException:
            tags = None
        new_path = output
        if tags is None:
            print(f"WARNING: Could not load tags for {filename} moving to unknown directory")
            new_path = new_path / "unknown" / filename.parent.name / filename.name
        elif tags.albumartist and tags.albumartist not in ["Various", "Soundtrack", "Various Artists"]:
            new_path = new_path / tags.albumartist.replace("/", "-")
            if tags.album:
                new_path = new_path / tags.album
            new_path = new_path / filename.name
        elif tags.albumartist in ["Various", "Soundtrack", "Various Artists"]:
            if tags.album:
                new_path = new_path / tags.album
            new_path = new_path / filename.name
        elif tags.artist:
            new_path = new_path / tags.artist.replace("/", "-")
            if tags.album:
                new_path = new_path / tags.album
            new_path = new_path / filename.name
        else:
            print(f"WARNING: Could not find artist for {filename} moving to unknown directory")
            new_path = new_path / "unknown" / filename.parent.name / filename.name
        print(f"Moving {str(filename)} to {new_path}")


if __name__ == '__main__':
    organize()