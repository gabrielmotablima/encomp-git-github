import gradio as gr

def speech_to_text(model="facebook/wav2vec2-base-960h"):
    return gr.load(
        f"huggingface/{model}",
        title=None,
        inputs="mic",
        description="Let me try to guess what you're saying!",
    )
