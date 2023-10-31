"""Module providing the server point of the application."""

import gradio as gr # type: ignore
from interfaces import (
	text_to_speech  as ts,
	speech_to_text  as st,
    spaces
)

if __name__ == "__main__":
    spaces_list = ["ydshieh/Kosmos-2"]
    spaces_interfaces = [spaces.spaces(space) for space in spaces_list]

    app = gr.TabbedInterface([ts.text_to_speech(),
                              st.speech_to_text(),
                             *spaces_interfaces],
                             ["Text-to-Speech",
                              "Speech-to-Text",
                              *spaces_list])
    app.queue(max_size=20).launch(server_name="0.0.0.0", server_port=7860)
