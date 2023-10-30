import gradio as gr

def text_to_speech(model="facebook/fastspeech2-en-ljspeech"):
    examples = [
        "I love learning machine learning",
        "How do you do?",
    ]
    return gr.load(
        f"huggingface/{model}",
        title=None,
        examples=examples,
        description="Give me something to say!",
    )
