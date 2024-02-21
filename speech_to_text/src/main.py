from whisper_jax import FlaxWhisperPipline
import jax.numpy as jnp

pipeline = FlaxWhisperPipline("openai/whisper-tiny", dtype=jnp.bfloat16, batch_size=16)

outputs = pipeline("./audios/esp_1.mp3",  task="transcribe", return_timestamps=True)


for chunk in outputs["chunks"]:
    print("#" * 50)
    print(f"{chunk['timestamp']}: {chunk['text']}")
    print("#" * 50)
