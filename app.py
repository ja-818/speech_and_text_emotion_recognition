import os
import gradio as gr
from models import infere_speech_emotion, infere_text_emotion, infere_voice2text

# Create a Gradio app object
with gr.Blocks() as demo:
    gr.Markdown(
        ''' 
        # Speech and Text Emotion Recognition
        ## Determining someone's emotions can be challenging based solely on their tone or words
        ### This app uses both to provide a more accurate analysis of emotional expression in a single audio recording
        '''
        )
    
    # Upload audio input and output fields
    with gr.Tab("Upload audio"):
        with gr.Row():
            upload_input = gr.Audio(label="Audio File", source="upload")
            with gr.Column():
                upload_output_1 = gr.Textbox(label="Text from the audio")
                upload_output_2 = gr.Textbox(label="Speech emotion")
                upload_output_3 = gr.Textbox(label="Text emotion")
        btn0 = gr.Button("Analyze audio")
    # Input-output logic based on button click
    btn0.click(fn=infere_voice2text, inputs=upload_input, outputs=upload_output_1)
    btn0.click(fn=infere_speech_emotion, inputs=upload_input, outputs=upload_output_2)
    upload_output_1.change(fn=infere_text_emotion, inputs=upload_output_1, outputs=upload_output_3)
    
    # Record audio input and output fields
    with gr.Tab("Record audio"):   
        with gr.Row():
            record_input = gr.Audio(label="Audio recording", source="microphone")
            with gr.Column():
                record_output_1 = gr.Textbox(label="Text from the audio")
                record_output_2 = gr.Textbox(label="Speech emotion")
                record_output_3 = gr.Textbox(label="Text emotion")
        btn1 = gr.Button("Analyze audio")   
    # Input-output logic based on button click
    btn1.click(fn=infere_voice2text, inputs=record_input, outputs=record_output_1)
    btn1.click(fn=infere_speech_emotion, inputs=record_input, outputs=record_output_2)
    record_output_1.change(fn=infere_text_emotion, inputs=record_output_1, outputs=record_output_3)
    
    # Examples to be used as input 
    gr.Examples(
        [ 
            os.path.join(os.path.dirname(__file__), "audio/a_good_dream.wav"),
            os.path.join(os.path.dirname(__file__), "audio/hype_in_ai.wav"),
        ],
        upload_input,
        label="Examples in which speech and words express different emotions:"        
    )
    


demo.launch()