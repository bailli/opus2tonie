# opus2tonie.py

---

### Usage

```
./opus2tonie.py -h
usage: opus2tonie.py [-h] [--file FILE | --dir DIR] [--append-tonie-filename]
                     [--no-tonie-header]
                     TARGET

Create Tonie compatible file from Ogg opus file(s).

positional arguments:
  TARGET                the output file name

optional arguments:
  -h, --help            show this help message and exit
  --file FILE           read only a single source file
  --dir DIR             read all files in directory
  --append-tonie-filename
                        append [500304E0] to filename
  --no-tonie-header     do not write Tonie header
```

### Tonie header

The header format is roughly described [here](https://github.com/toniebox-reverse-engineering/toniebox/wiki/Audio-file-format). However, a proto file is not provided.

To generate the python output run:

`protoc --python_out=. tonie_header.proto`

### Creating opus files

As input only stereo opus files with 48 kHz sampling rate are accepted. The original software seems to use 96 kbit/s VBR encoding.

You can create input files from mp3 using ffmpeg und opusenc:

```bash
for f in ./*.mp3; do 
  ffmpeg -i "$f" -f wav -ar 48000 - | opusenc --quiet --vbr --bitrate 96 - "$(basename -s mp3 "$f")opus"
done
```

### Some useful resources
* https://en.wikipedia.org/wiki/Ogg_page
* https://github.com/toniebox-reverse-engineering/toniebox/wiki/Audio-file-format
* https://www.xiph.org/ogg/doc/rfc3533.txt
* https://tools.ietf.org/html/rfc7845#section-4
* https://tools.ietf.org/html/rfc6716#section-3.1
