import gradio as gr
from interfaces import (
	text_completion as tc,
	text_to_speech  as ts,
	speech_to_text  as st,
	spaces
)

if __name__ == "__main__":
    app = gr.TabbedInterface([tc.text_completion(),
                              ts.text_to_speech(),
                              st.speech_to_text(),
                              spaces.spaces()],
                             ["Text Completion",
                              "Text-to-Speech",
                              "Speech-to-Text",
                              "Ready-to-use Spaces"])
    app.queue(max_size=20)
    app.launch()