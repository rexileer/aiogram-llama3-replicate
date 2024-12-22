import replicate
from dotenv import load_dotenv

load_dotenv()

def generate_ai_image(prompt):
    input = {
        "prompt": prompt,
        "scheduler": "K_EULER"
    }

    output = replicate.run(
        "stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4",
        input=input
    )
    return output

def generate_ai_text(prompt):
    input = {
        "prompt": prompt,
        "prompt_template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nYou are a helpful assistant<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
    }


    output = replicate.run(
       "meta/meta-llama-3-70b-instruct",
       input=input 
    )

    return ''.join(output)
