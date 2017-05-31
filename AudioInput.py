import pyaudio
import wave
import threading

CHUNK = 1024
FORMAT = pyaudio.paInt16
WAVE_OUTPUT_FILENAME = "output.wav"

"""
    Returns when user hits enter.
"""
def waitUntilEnter():
    try:
        s = raw_input("Hit enter when you are done speaking.")
    except AttributeError:
        s = input("Hit enter when you are done speaking.")

"""
    Records audio input from user, saves it as a file, and returns the filename.  If
    an error occurs, it returns None.
"""
def getAudioInput(output_file_name = WAVE_OUTPUT_FILENAME):

    # get info from default input device
    p = pyaudio.PyAudio()
    default_input = p.get_default_input_device_info()

    if default_input is None:
        return #None

    if 'maxInputChannels' not in default_input:
        return #None

    if 'defaultSampleRate' not in default_input:
        return #None

    channels = 2
    rate = 44100
	
    # open input audio stream
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=CHUNK)

    # wait until user hits enter
    try:
        s = raw_input("Hit enter when you are ready to speak.")
    except AttributeError:
        s = input("Hit enter when you are ready to speak.")

    # set up to record
    t = threading.Thread(target=waitUntilEnter)
    t.start()

    # record until user hits enter again
    while True:
        if t.is_alive():
            yield stream.read(CHUNK)
        else:
            break

    # finish recording

    stream.stop_stream()
    stream.close()
    p.terminate()