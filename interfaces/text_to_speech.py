"""Module providing a function to create an Interface for user interaction."""

import gradio as gr # type: ignore

def text_to_speech(model:str="facebook/fastspeech2-en-ljspeech"):
    """ Generate interface to user interact with the text to speech model
        
        Parameters
        ----------
            model : str
                name of the pre-trained model (default is "facebook/fastspeech2-en-ljspeech")

        Returns
        -------
            gradio.interface.Interface
                gradio Interface for user interaction
    """
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
