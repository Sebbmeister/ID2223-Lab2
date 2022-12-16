import gradio as gr
from transformers import pipeline

pipe = pipeline(model="SebLih/whisper-SV3") # change to "your-username/the-name-you-picked"

def transcribe(audio):
    text = pipe(audio)["text"]
    return text

iface = gr.Interface(
    fn=transcribe, 
    inputs=gr.Audio(source="microphone", type="filepath"), 
    outputs="text",
    title="Whisper Small Swedish",
    description="Realtime speech recognition and transcription of Swedish language through the use of a Whisper small model.",
)

iface.launch(share=True)