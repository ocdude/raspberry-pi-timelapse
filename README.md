# raspberry-pi-timelapse
Timelapse camera using a Raspberry Pi and the official camera module

## Usage
Given a `config.ini`, take pictures on a set interval with the camera and upload (or not) to a specific location with scp.

Operates in two modes. In *overwrite* mode, the timelapse produces one image and overwrites it every time a capture is made. In *continuous* mode, sequentially numbered images are produced.

See the supplied `config.ini.example` file for the required items.