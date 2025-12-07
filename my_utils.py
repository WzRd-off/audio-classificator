from pydub import AudioSegment

AUDIO_LENGTH_MS = 20_000
TARGET_FORMAT = 'wav'

def process_file(args):
    file_path, output_dir = args
    
    try:

        audio = AudioSegment.from_file(file_path)
        
        chunks = [audio[i:i + AUDIO_LENGTH_MS] for i in range(0, len(audio), AUDIO_LENGTH_MS)]
        

        chunks_to_save = chunks[:-1] 

        if not chunks_to_save:
            return # Если файл был короче 20 сек мы его не сохраняем

        base_name = file_path.stem
        for i, chunk in enumerate(chunks_to_save):
            out_name = f"chunk_{base_name}_{i+1}.{TARGET_FORMAT}"
            out_path = output_dir / out_name
            chunk.export(out_path, format=TARGET_FORMAT)
            
    except Exception as e:
        print(f"Error processing {file_path.name}: {e}")

def sieve(args):
    audio_path, output_dir = args
    try:
        
        audio = AudioSegment.from_file(audio_path)

        base_name = audio_path.stem
        if audio.duration_seconds >= 5:
            save = output_dir / f"chunk_{base_name}.{TARGET_FORMAT}"
            audio.export(save, format=TARGET_FORMAT)

    except Exception as e:
        print(f"Error processing {audio_path.name}: {e}")