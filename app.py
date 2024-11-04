
import io
import gradio as gr
import time
from pathlib import Path
import google.generativeai as genai

class DataGenerator:
    def __init__(self):
        self.system_prompt = "You are a helpful assistant, create synthetic data based on the user prompt in CSV format."
        self.history = []
        gemini="AIzaSyBcbjx3E-j9nQwNXAasmSi_lUcXl7yVP-U"
        genai.configure(api_key=gemini)
        
    def generate_data(self, prompt):
        try:
            messages = [{"role": "system", "content": self.system_prompt}]
            for user_msg, assistant_msg in self.history:
                messages.append({"role": "user", "content": user_msg})
                messages.append({"role": "assistant", "content": assistant_msg})
            messages.append({"role": "user", "content": prompt})
            
            gemi = genai.GenerativeModel(system_instruction=self.system_prompt, model_name="gemini-1.5-flash")  
            response = gemi.generate_content(prompt) 
            response_content=response.text
           
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            file_path = f"generated_data_{timestamp}.csv"
            with open(file_path, "w", newline='') as f:
                f.write(response_content)
            
            if Path(file_path).exists():
                print(f"File successfully created at: {file_path}")
            else:
                print("File creation failed.")
            
            self.history.append((prompt, response_content))
            print(file_path)
            return file_path
        
        except Exception as e:
            print(f"Error generating data: {e}")
            return None

def create_interface():
    generator = DataGenerator()
    
    with gr.Blocks() as demo:
        gr.Markdown("# Synthetic Data Generator")
        
        with gr.Row():
            prompt = gr.Textbox(
                label="Enter your prompt",
                placeholder="Describe the data you want to generate..."
            )
        with gr.Row():
            out_download = gr.File()
        btn = gr.Button("Generate Data")
        btn.click(fn=generator.generate_data, inputs=[prompt], outputs=[out_download])
    return demo

if __name__ == "__main__":
    demo = create_interface()
    demo.launch(debug=True)

