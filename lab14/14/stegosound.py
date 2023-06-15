import wave


def encode(message, wav_path, new_wav_path):
    audio = wave.open(wav_path, mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    message = message + int((len(frame_bytes)-(len(message)*8*8))/8)*'#'
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in message])))
    
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit

    frame_modified = bytes(frame_bytes)
    
    newAudio = wave.open(new_wav_path, 'wb')
    newAudio.setparams(audio.getparams())
    newAudio.writeframes(frame_modified)

    newAudio.close()
    audio.close()


def decode(wav_path):
    audio = wave.open(wav_path, mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
    decoded = string.split("###")[0]
    audio.close()
    return decoded
