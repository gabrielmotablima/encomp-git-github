"""Module providing the server point of the application."""

import gradio as gr # type: ignore
from interfaces import (
	text_to_speech  as ts,
	speech_to_text  as st
)

if __name__ == "__main__":
    app = gr.TabbedInterface([ts.text_to_speech(),
                              st.speech_to_text()],
                             ["Text-to-Speech",
                              "Speech-to-Text"])
    app.queue(max_size=20).launch(server_name="0.0.0.0", server_port=7860)
