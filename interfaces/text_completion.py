import gradio as gr
from transformers import pipeline, set_seed

def text_generation(
        text_prompt:str,
        model:str='gpt2',
        max_length:int=30,
        num_return_sequences:int=1
    ) -> str:
    generator = pipeline('text-generation', model=model)
    response = generator(text_prompt, max_length = max_length, num_return_sequences=1)
    return response[0]['generated_text']

def text_completion():
    textbox = gr.Textbox()
    return gr.Interface(
        fn=text_generation,
        inputs=textbox,
        outputs=textbox
    )

# def text_completion(model="gpt2"):
#     examples = [
#         "We are attending the ENCOMP short course",
#         "The professors from Computer and Electronics Department are"
#     ]
#     return gr.load(
#         f"huggingface/{model}",
#         title=None,
#         examples=examples,
#         description="Write something!",
#     )