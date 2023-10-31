"""Module providing the server point of the application."""

import gradio as gr
from interfaces import (
	text_to_speech  as ts,
	speech_to_text  as st,
	spaces
)

if __name__ == "__main__":
    spaces_names = ["ydshieh/Kosmos-2", "LeoLM/leo-hessianai-13b-chat"]
    app = gr.TabbedInterface([ts.text_to_speech(),
                              st.speech_to_text(),
                             *spaces.spaces(spaces_names)],
                             ["Text-to-Speech",
                              "Speech-to-Text",
                              *spaces_names])
    app.queue(max_size=20)
    app.launch(server_name="0.0.0.0", server_port=7860)
