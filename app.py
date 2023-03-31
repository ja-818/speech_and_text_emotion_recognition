import os
import gradio as gr
from models import infere_speech_emotion, infere_text_emotion, infere_voice2text

with gr.Blocks() as demo:
    gr.HTML('''
        <h1 style="text-align:center;">Speech and Text Emotion Recognition</h1>
        <h2 style="text-align:center;">Determining someone's emotions can be challenging based solely on their tone or words <br> This app uses both to provide a more accurate analysis of emotional expression in a single audio recording</h2>
        ''')
    with gr.Row():
        input = gr.Audio(label="Audio File", type="filepath")
        with gr.Column():
            output0 = gr.Textbox(label="Text from the audio")
            output1 = gr.Textbox(label="Speech emotion")
            output2 = gr.Textbox(label="Text emotion")
    btn = gr.Button("Analyze audio")   
    
    gr.Examples(
        [ 
            os.path.join(os.path.dirname(__file__), "audio/a_good_dream.wav"),
            os.path.join(os.path.dirname(__file__), "audio/hype_in_ai.wav"),
        ],
        input,
        label="Examples of cases in which speech and words can convey different"        
    )
    
    btn.click(fn=infere_voice2text, inputs=input, outputs=output0)
    btn.click(fn=infere_speech_emotion, inputs=input, outputs=output1)
    output0.change(fn=infere_text_emotion, inputs=output0, outputs=output2)

demo.launch()