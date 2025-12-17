# Audio Transcription with OpenAI Whisper

This repository contains a short and easy-to-use **Jupyter Notebook (Python)** for transcribing audio files using the **OpenAI Whisper** speech-to-text model.

The script was originally created for **family and friends** who wanted to transcribe audio without paying for subscription-based transcription services. As a result, it is designed to be **simple, accessible, and usable without advanced IT knowledge**.

---

## Features

* Transcribe audio files to text using OpenAI’s Whisper model
* Uses state-of-the-art speech recognition
* No subscription fees
* Runs in a Jupyter Notebook
* Beginner-friendly and easy to follow

---

## Requirements

* **Python** (handled automatically when using Google Colab)
* **NVIDIA GPU with CUDA support**

  * The **Whisper Large model** requires **more than 10 GB of VRAM**
* **Google Colab** (recommended)

  * Provides free access to compatible GPUs

---

## Recommended Setup (Google Colab)

The easiest way to run this script is with **Google Colab**, which allows you to use a GPU for free:

1. Open the notebook in Google Colab
2. Enable GPU support:

   * `Runtime` → `Change runtime type` → `Hardware accelerator` → `GPU`
3. Upload your audio file
4. Run the notebook cells in order
5. Receive a text transcription of your audio

No local installation or configuration is required.

---

## Models

* The notebook is configured to use the **Whisper Large model** for high-quality transcription.
* If you encounter memory issues, you may switch to a smaller Whisper model (e.g., `medium` or `small`) with lower GPU requirements.

---

## Intended Audience

This project is intended for:

* Non-technical users
* Friends and family
* Anyone who wants a free, local transcription solution
* Users who prefer not to rely on paid transcription services

---

## Disclaimer
* This project is provided as-is for personal use. Transcription accuracy may vary depending on audio quality, language, and background noise.
* The example audio file was taken from the free to use media website Pixabay (https://pixabay.com/sound-effects/002145-a-conversation-with-a-neighbor-53032/) and is therfore under the Pixabay Content License (https://pixabay.com/service/license-summary/).
---

## License

Feel free to use, modify, and share this project for personal or educational purposes.
