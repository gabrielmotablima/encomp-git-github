"""Module providing the unit test class and methods."""


import unittest

import gradio as gr

from interfaces import (
    text_to_speech  as ts,
    speech_to_text  as st,
    spaces
)

class TestInterfaces(unittest.TestCase):
    """ Class intended for unit testing of interfaces
 
        Attibutes
        ----------
            text_to_speech
                text to speech interface

        Methods
        -------
            test_is_instance()
                test if the instances of the interfaces are correct
    """
    text_to_speech = ts.text_to_speech()
    speech_to_text = st.speech_to_text()
    spaces = spaces.spaces()

    def test_is_instance(self):
        """ Test if the interfaces instances are correct"""
        self.assertIsInstance(self.text_to_speech, gr.interface.Interface)
        self.assertIsInstance(self.speech_to_text, gr.interface.Interface)
        self.assertIsInstance(self.spaces, gr.blocks.Blocks)

if __name__ == "__main__":
    unittest.main()
