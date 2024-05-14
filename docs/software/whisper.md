
## Introduction

This guide provides instructions for loading and using OpenAI's Whisper, an
automatic speech recognition system. Whisper is available on Rackham,
Snowy and Bianca.

## Module Loading

To load the Whisper module, run the following command:

```bash
module load Whisper/0.5.1
```

This will also load the necessary dependencies, including `python`
and `ffmpeg`.

```bash
$ module list
Currently Loaded Modules:
  1) uppmax       3) mp-tools/latest   5) FFmpeg/5.1.2
  2) git/2.34.1   4) python/3.11.4     6) Whisper/0.5.1
```

## Usage

Whisper as an inference service is available in the form of Graphical User Interface (GUI).
Whisper can also be run as a command-line tool or as a Python library.

### GUI

1. Login to [Rackham](https://rackham-gui.uppmax.uu.se/) or [Bianca](https://bianca.uppmax.uu.se/) via ThinLinc.
2. Load Whisper module as instructed in [Module Loading](http://docs.uppmax.uu.se/software/whisper/#module-loading) section.
3. Transfer your data from your local machine to Wharf ([WinSCP](http://docs.uppmax.uu.se/cluster_guides/transfer_bianca/#winscp-windows) client, [FileZilla](http://docs.uppmax.uu.se/cluster_guides/transfer_bianca/#filezilla-linuxmacoswindows) client or other ways via [terminal](http://docs.uppmax.uu.se/cluster_guides/transfer_bianca/)) and then to your project folder (Bianca: `/cygnus/proj/`) .
4. Go to your project folder where you will also find `whisper-gui.sh` file, right click inside this folder and select "Open Terminal Here" and run the following command: `./whisper-gui.sh &`. This will run the Whisper service.
5. Select appropriate options, or use the following for the best results:
   device: gpu
   SLURM job name: [give any name without space]
   Total audio length in minutes : [give a rough average if transcribing files in bulk]
   Model: large-v2
   by word timestamps: by_sentence
6. Monitor your job using `jobinfo` command on terminal or on `[job_name].out` that gets created in the same folder. Where `[job_name]` is the SLURM job name that you gave earlier.

### Command-line

The `whisper` command can be used to transcribe audio files. For example:

```bash
whisper audio.flac audio.mp3 audio.wav --model medium
```

### Python

```python title="example.py"
import whisper

# Load the model
model = whisper.load_model("base")

# Transcribe an audio file
result = model.transcribe("/path/to/audiofile.mp3")

# Output the transcription
print(result["text"])

```

### Available Models

For making offline usage of Whisper more convenient, we provide
pre-trained models as part of the Whisper module. You can list
all the available models by:

```bash
$ ll /sw/apps/Whisper/0.5.1/rackham/models
total 13457440
-rw-rw-r-- 1 sw  145261783 Nov 10 14:22 base.en.pt
-rw-rw-r-- 1 sw  145262807 Nov 10 14:23 base.pt
-rw-rw-r-- 1 sw 3086999982 Nov 10 14:39 large-v1.pt
-rw-rw-r-- 1 sw 3086999982 Nov 10 14:40 large-v2.pt
-rw-rw-r-- 1 sw 3087371615 Nov 10 14:27 large-v3.pt
-rw-rw-r-- 1 sw 1528006491 Nov 10 14:24 medium.en.pt
-rw-rw-r-- 1 sw 1528008539 Nov 10 14:25 medium.pt
-rw-rw-r-- 1 sw  483615683 Nov 10 14:23 small.en.pt
-rw-rw-r-- 1 sw  483617219 Nov 10 14:23 small.pt
-rw-rw-r-- 1 sw   75571315 Nov 10 14:22 tiny.en.pt
-rw-rw-r-- 1 sw   75572083 Nov 10 14:22 tiny.pt
```
