"""Module providing a function to create an Interface for user interaction."""

import gradio as gr

def spaces(spaces=["ydshieh/Kosmos-2"]):
    """ Generate interface to user interact with some ready-to-use space
 
        Parameters
        ----------
            space : str
                name of the ready-to-use space (default is "ydshieh/Kosmos-2")

        Returns
        -------
            gradio.interface.Interface
                gradio Interface for user interaction
    """
    return [gr.load(space, src="spaces") for space in spaces]
