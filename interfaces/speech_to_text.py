"""Module providing a function to create an Interface for user interaction."""

import gradio as gr

def speech_to_text(model="facebook/wav2vec2-base-960h"):
    """ Generate interface to user interact with the speech to text model
 
        Parameters
        ----------
            model : str
                name of the pre-trained model (default is "facebook/wav2vec2-base-960h")

        Returns
        -------
            gradio.interface.Interface
                gradio Interface for user interaction
    """
    return gr.load(
        f"huggingface/{model}",
        title=None,
        inputs="mic",
        description="Let me try to guess what you're saying!",
    )
