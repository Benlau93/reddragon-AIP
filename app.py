import gradio as gr
import requests

def predict_hate_speech(text):
    # call backend
    url = f"http://host.docker.internal:8000/api?input={text}"
    response = requests.post(url).json()
    output_text = f"The text given has {response} probability of being a hate speech"
    return output_text



with gr.Blocks(theme=gr.themes.Monochrome(), css = "style/style.css") as demo:
    gr.Markdown("Hate Speech Prediction", elem_classes="title")
    input_text = gr.Textbox(label = "Text", placeholder = "Enter text", lines = 10, show_label=False)
    submit_button = gr.Button(value = "Submit", elem_classes="button")
    output_text = gr.Markdown(label = "Is this Hate Speech?", elem_classes="output")
    submit_button.click(fn=predict_hate_speech, inputs=input_text, outputs=output_text, api_name="predict")

if __name__ == "__main__":
    demo.launch(server_port=7860, server_name = "0.0.0.0")