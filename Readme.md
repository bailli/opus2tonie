# opus2tonie.py

---

### Current state

At the time of writing the script can produce files that can be played by the Tonie box.

### Usage

```
usage: opus2tonie.py [-h] [--ts TIMESTAMP] [--ffmpeg FFMPEG]
                     [--opusenc OPUSENC] [--bitrate BITRATE] [--cbr]
                     [--append-tonie-filename] [--no-tonie-header] [--info]
                     [--split]
                     SOURCE [TARGET]

Create Tonie compatible file from Ogg opus file(s).

positional arguments:
  SOURCE                input file or directory or a file list (.lst)
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

The firmware of the Tonie box has drawbacks **when it can connect to the internet via WiFi**:

* Reading custom NFC tags will result in the deletion of the associated audio data.

* Reading an official Tonie that has custom content stored on the box will delete the custom content and download the original files again, unless the internal timestamps are identical

* On startup, or when idle, it will set the "hidden" FAT filesystem attribute for custom audio data files with incongruous internal timestamps. This enables "live" mode for these files and the NFC tag will always trigger playback from the beginning of the file (no matter whether another NFC tag was used in-between).
  You can only enter the offline mode of the box *after* startup, so to avoid this effect you need to block the box on your wireless network before connecting it to the batteries again. \
  You may also plug an "extension cord" into the internal SD card slot to make it reachable without disconnecting the battery. Then you can eject the card and add new files or fix the FAT fs attribute while the box is in sleep mode.

When you use original Tonie figurines (or their NFC tag) the latter two issues can be circumvented by using the `timestamp` that is officially associated with the Tonie for the custom content.
You can identify this timestamp through `./opus2tonie.py --info` and generate your custom files with the optional `--ts <timestamp>` parameter.

### Tonie header

The header format is roughly described [here](https://github.com/toniebox-reverse-engineering/toniebox/wiki/Audio-file-format). However, a proto file is not provided.

To generate the python output run:

`protoc --python_out=. tonie_header.proto`

### Input files

If you have `ffmpeg` and `opusenc` in your path (or specify their location) you can use any input files which `ffmpeg` can read. Otherwise you are limited to stereo 48 kHz opus files.

A list file (the extension *must be* .lst) can contain either relative or absolute files. Additionally, you can specify (short) text strings which will be synthesized with Google Cloud text2speech (see below)

### text2speech

Lines starting with `text:` in a list file input will be sent to Google Cloud Text-to-Speech. You will need to have the [librecaptcha](https://pypi.org/project/librecaptcha/) package installed. Solving the captcha seems to take a while but it should be only necessary once (for a "session").

You can change the default settings at the top of the script (`T2S_xxx` variables). Possible values can be taken from here: https://cloud.google.com/text-to-speech

### Some useful resources
* https://en.wikipedia.org/wiki/Ogg_page
* https://github.com/toniebox-reverse-engineering/toniebox/wiki/Audio-file-format
* https://www.xiph.org/ogg/doc/rfc3533.txt
* https://tools.ietf.org/html/rfc7845#section-4
* https://tools.ietf.org/html/rfc6716#section-3.1
