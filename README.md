##Anny Assistente Virtual

Estudo de caso para criação de assistente Virtual para programadores

Linguagem de programação:

-- Python 3.8 

Plataforma Linux:

 --Mint

## PyAudio como erro no Mint:
Linux distributions (like Ubuntu and Mint), install PyAudio using APT:
     execute ==> sudo apt-get install python-pyaudio python3-pyaudio in a terminal.
If the version in the repositories is too old, install the latest release using Pip: execute sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && sudo pip install pyaudio (replace pip with pip3 if using Python 3).


### Objetivos: 
- Reconhecimento de fala: 
    - Google (online) => descartado pela demanda de conexão e alto tempo de resposta. 

    - Vosk => Funcionalidade Offline

- Sintese de Voz:
    - PyTTSx3 
        : ## apresentando saidas, mas sem saida de audio

- Utilização de IA:
    -