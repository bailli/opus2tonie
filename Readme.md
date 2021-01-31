# opus2tonie.py

---

### Current state

A first test produced files which were accepted by the Tonie box.

### Usage

```
usage: opus2tonie.py [-h] [--ts TIMESTAMP] [--ffmpeg FFMPEG]
                     [--opusenc OPUSENC] [--bitrate BITRATE] [--cbr]
                     [--append-tonie-filename] [--no-tonie-header] [--info]
                     [--split]
                     SOURCE [TARGET]

Create Tonie compatible file from Ogg opus file(s).

positional arguments:
  SOURCE                input file or directory
  TARGET                the output file name (default: 500304E0)

optional arguments:
  -h, --help            show this help message and exit
  --ts TIMESTAMP        set custom timestamp / bitstream serial
  --ffmpeg FFMPEG       specify location of ffmpeg
  --opusenc OPUSENC     specify location of opusenc
  --bitrate BITRATE     set encoding bitrate in kbps (default: 96)
  --cbr                 encode in cbr mode
  --append-tonie-filename
                        append [500304E0] to filename
  --no-tonie-header     do not write Tonie header
  --info                Check and display info about Tonie file
  --split               Split Tonie file into opus tracks
```

### Firmware problems

The most recent firmware version of the Tonie box has a few drawbacks:

* Reading custom NFC tags while connected to the internet will result in the deletion of the associated audio data.
* (*not fully checked*) When the box boots (i.e. after re-connecting the battery) it will always enable Wi-Fi and, if it can reach the Tonie cloud, it will set the "hidden" FAT filesystem attribute for custom audio data files. This will have the effect of enabling "live" mode for these files => the NFC tag will always trigger playback of the beginning of the file (no matter whether another NFC tag was used in-between).

Other tidbits:

(*found somewhere else; unconfirmed*) If you replace an official Tonie with custom content and keep the same `timestamp` as the official file, the replaced content will even work when the box is online.  

### Tonie header

The header format is roughly described [here](https://github.com/toniebox-reverse-engineering/toniebox/wiki/Audio-file-format). However, a proto file is not provided.

To generate the python output run:

`protoc --python_out=. tonie_header.proto`

### Input files

If you have `ffmpeg` and `opusenc` in your path (or specify their location) you can use any input files which `ffmpeg` can read. Otherwise you are limited to stereo 48 kHz opus files.

### Some useful resources
* https://en.wikipedia.org/wiki/Ogg_page
* https://github.com/toniebox-reverse-engineering/toniebox/wiki/Audio-file-format
* https://www.xiph.org/ogg/doc/rfc3533.txt
* https://tools.ietf.org/html/rfc7845#section-4
* https://tools.ietf.org/html/rfc6716#section-3.1
