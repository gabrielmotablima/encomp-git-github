import gradio as gr

def spaces(space="ydshieh/Kosmos-2"):
    return gr.load(space, src="spaces")
