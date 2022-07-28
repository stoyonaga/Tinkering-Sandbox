# Purpose of this File
This directory will serve as a temporary cache for the images, prior to generating the gif.
Additionally, you add the proceeding line of code into main.py, in order to better maintain this cache and keep everything clean for repeated method reruns.

```python
os.system("mv output/out.gif /mnt/...")
```
# Installation

## Configuration / Setup

After you clone this repository and cd into neon-gifs, run the following command in the terminal:
```bash
sh install.sh
```

## Uninstall

After you cd into neon-gifs, run the following command in the terminal:
```bash
sh uninstall.sh
```

# Software Environments
This script has been developed and tested to run under the following constraints:

* Python 3.8.10
* Ubuntu 20.04.4 LTS 
* WSL 2
* Software Packages -- ffmpeg, Pillow

