# Whisper

## Introduction

This guide provides instructions for loading and using OpenAI's Whisper, an
automatic speech recognition system. Whisper is available on Rackham,
Snowy and Bianca. It can either be used through a User Interface or loaded as a Module.


## User Interface (GUI)

### Step 1: Accessing your project  

1. Register an account on NAISS SUPR, apply for a project and apply for an account at UPPMAX by following steps mentioned in [UPPMAX (get started)](https://www.uu.se/en/centre/uppmax/get-started/create-account-and-apply-for-project/user-account) webpage. A direct link for applying for a project for sensitive data (Bianca) is [here](https://supr.naiss.se/round/senssmall2024/create_proposal/?). Give adequate information while create your proposal or follow [this template](#proposal-template). Finally, setup a [two factor authentication](https://www.uu.se/en/centre/uppmax/get-started/2-factor) for your newly created UPPMAX account.  
2. Check access to your project on [Bianca via ThinLinc](https://bianca.uppmax.uu.se/).


### Step 2: Data transfer from local to project  

1. Transfer your data from your local machine to Wharf using SFTP clients 
    like [WinSCP](../cluster_guides/transfer_bianca.md#winscp-windows) 
    client (Windows only), 
    [FileZilla](../cluster_guides/transfer_bianca.md#filezilla-linuxmacoswindows) 
    client (Mac, Windows or Linux) 
    or other ways via [terminal](../cluster_guides/transfer_bianca.md).

### Step 3: Transcribing/Translating  

1. Login to [Bianca via ThinLinc](https://bianca.uppmax.uu.se/).
1. Right click on the Desktop and select "Open Terminal Here" and enter the following command to load Whisper-gui module:  

    ```console
    [jayan@sens2024544-bianca jayan]$ module load Whisper-gui
    ```

    This creates `proj` and `wharf` folders on your Desktop. `wharf` contains the data that was transferred in Step 2 and transfer this to `proj` folder.

1. Enter the `proj` folder, right click and select "Open Terminal Here". Enter following command to run the Whisper service GUI:  

    ```console
    [jayan@sens2024544-bianca proj]$ module load Whisper-gui
    [jayan@sens2024544-bianca proj]$ whisper-gui.sh
    ```

    Next time you start transcribing/translating by logging in again to Bianca, you can start from this step and skip the previous one, since `proj` folder is already created.

1. Select appropriate options, or use the following for the best results:  
   device: gpu  
   SLURM job name: [give any name without space]  
   Total audio length in minutes : [give a rough average if transcribing files in bulk]  
   Model: large-v2  
   by word timestamps: by_sentence

### Step 4: Monitoring jobs  

1. Monitor your job by entering `jobinfo` on terminal or on `[job_name].out` that gets created in your output folder. Where `[job_name]` is the SLURM job name that you gave earlier.


### Step 5: Data transfer from project to local

1. Transfer your output results from project folder (Bianca: `/cygnus/proj/`) to Wharf.
2. Use an SFTP client (WinSCP/FileZilla or through terminal) like you did in Step 2.

### Output files

By default you receive 5 types of output files for each file you transcribe/translate:
With timestamps: `.srt`, `.vtt`, `.tsv`  
Without timestamps: `.txt`  
With detailed model metadata: `.json`.

On Mac, `.srt` and `.vtt` can be opened in Word by:  
Tap with two fingers. Select Encoding as "UTF-8". Change the name of the file like `some_name.docx` and change type of file to `.docx`. Open the file and then Save As a new file.

### Advance settings

### Languages available

Use the following 2 letter code to perform transcribing when asked in the GUI:  
`en`: "english",
    `zh`: "chinese",
    `de`: "german",
    `es`: "spanish",
    `ru`: "russian",
    `ko`: "korean",
    `fr`: "french",
    `ja`: "japanese",
    `pt`: "portuguese",
    `tr`: "turkish",
    `pl`: "polish",
    `ca`: "catalan",
    `nl`: "dutch",
    `ar`: "arabic",
    `sv`: "swedish",
    `it`: "italian",
    `id`: "indonesian",
    `hi`: "hindi",
    `fi`: "finnish",
    `vi`: "vietnamese",
    `he`: "hebrew",
    `uk`: "ukrainian",
    `el`: "greek",
    `ms`: "malay",
    `cs`: "czech",
    `ro`: "romanian",
    `da`: "danish",
    `hu`: "hungarian",
    `ta`: "tamil",
    `no`: "norwegian",
    `th`: "thai",
    `ur`: "urdu",
    `hr`: "croatian",
    `bg`: "bulgarian",
    `lt`: "lithuanian",
    `la`: "latin",
    `mi`: "maori",
    `ml`: "malayalam",
    `cy`: "welsh",
    `sk`: "slovak",
    `te`: "telugu",
    `fa`: "persian",
    `lv`: "latvian",
    `bn`: "bengali",
    `sr`: "serbian",
    `az`: "azerbaijani",
    `sl`: "slovenian",
    `kn`: "kannada",
    `et`: "estonian",
    `mk`: "macedonian",
    `br`: "breton",
    `eu`: "basque",
    `is`: "icelandic",
    `hy`: "armenian",
    `ne`: "nepali",
    `mn`: "mongolian",
    `bs`: "bosnian",
    `kk`: "kazakh",
    `sq`: "albanian",
    `sw`: "swahili",
    `gl`: "galician",
    `mr`: "marathi",
    `pa`: "punjabi",
    `si`: "sinhala",
    `km`: "khmer",
    `sn`: "shona",
    `yo`: "yoruba",
    `so`: "somali",
    `af`: "afrikaans",
    `oc`: "occitan",
    `ka`: "georgian",
    `be`: "belarusian",
    `tg`: "tajik",
    `sd`: "sindhi",
    `gu`: "gujarati",
    `am`: "amharic",
    `yi`: "yiddish",
    `lo`: "lao",
    `uz`: "uzbek",
    `fo`: "faroese",
    `ht`: "haitian creole",
    `ps`: "pashto",
    `tk`: "turkmen",
    `nn`: "nynorsk",
    `mt`: "maltese",
    `sa`: "sanskrit",
    `lb`: "luxembourgish",
    `my`: "myanmar",
    `bo`: "tibetan",
    `tl`: "tagalog",
    `mg`: "malagasy",
    `as`: "assamese",
    `tt`: "tatar",
    `haw`: "hawaiian",
    `ln`: "lingala",
    `ha`: "hausa",
    `ba`: "bashkir",
    `jw`: "javanese",
    `su`: "sundanese",
    `yue`: "cantonese"

### Proposal template

Under the Basic Information section on NAISS SUPR, provide the following compulsory details pertaining to your project in the following fashion:  

* **Project Title** : Whisper service for [Name of the project]

* **Abstract**: [What is the project about, give links, funding info, duration etc.]  

* **Resource Usage**:  [Explain where transcriptions/translations are needed like interview recordings on device/ zoom or other forms of audio/video recordings from offline/online sources. Give the average and maximum number of recordings to be transcribed/translated. Give the average and maximum size of recordings in mins/hours. Mention if it is a transcribing or translation requirement. Mention the language spoken in the recordings, if known, and a rough estimate of number of recordings for each of these languages. Ignore the "core-hours" and "hours required to analyse one sample" requirement.]  

* **Abridged Data Management Plan**:  [Address all points. Mention the recording file types example: .mp3, .mp4, .wav etc.]  

* **Primary Classification**: [Either follow the  Standard för svensk indelning av forskningsämnen link given or search by entering the field of research such as 'Social Work', 'Human Geography' etc. ]  

* **Requested Duration**: [Mention the duration for which Whisper service is strictly required. Mentioning more duration than actually required might reflect negatively when a new allocation is requested for the same or new project next time. It is possible to request for a shorter duration of 1 month at first and then ask for a new one once the need arises again in the future.]


## Module Loading

To load the Whisper module, run the following command:


```console
[jayan@sens2024544-bianca jayan]$ module load Whisper/0.5.1
```

This will also load the necessary dependencies, including `python`
and `ffmpeg`.

```console
[jayan@sens2024544-bianca jayan]$ module list
Currently Loaded Modules:
  1) uppmax       3) mp-tools/latest   5) FFmpeg/5.1.2
  2) git/2.34.1   4) python/3.11.4     6) Whisper/0.5.1
```  

### Command-line

The `whisper` command can be used to transcribe audio files. For example:

```console
[jayan@sens2024544-bianca jayan]$ whisper audio.flac audio.mp3 audio.wav --model medium
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

```console
[jayan@sens2024544-bianca jayan]$ ll /sw/apps/Whisper/0.5.1/rackham/models
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

