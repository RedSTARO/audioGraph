import librosa
import matplotlib.pyplot as plt
import numpy as np

def generate_spectrogram(audio_file, output_image, which):

    y, sr = librosa.load(audio_file)

    # STFT 短时傅里叶变换
    D = np.abs(librosa.stft(y))


    freqs = librosa.fft_frequencies(sr=sr)
    times = librosa.frames_to_time(np.arange(D.shape[1]))


    plt.figure(figsize=(10, 4))
    plt.plot(times, D.T)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title(f'Spectrogram Curve {which} side')
    plt.savefig(output_image)

which="L"
generate_spectrogram(f'{which}.mp3', f'{which}.jpg', which)
which="R"
generate_spectrogram(f'{which}.mp3', f'{which}.jpg', which)
