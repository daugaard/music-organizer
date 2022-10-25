# Music Organizer

Tools to organize a music collection based on ID3 tags.

Supported filetypes: `mp3`, `m4a`, `wma`
_All other files are ignored and not moved_

## Usage
```
$ python organize.py --input-dir some-dir --output-dir some-other-dir
```

Will copy any supported files into output dir using the following rules:

- If album artist is set, and album artist is not `Various` or `Soundtrack`
  - Target: `output_dir/album artist/album name/filename`
- Else if album artist is `Various` or `Soundtrack`
  - Target: `output_dir/album name/filename`
- Else if artist set
  - Target: `output_dir/artist/album name/filename`
- Else:
  - Target: `output_dir/unknown/old parent dirname/filename` 
