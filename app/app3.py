import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
from diffusers import StableDiffusionPipeline
import torch

def generate_image(text):
    # Create an image with PIL
    model_id = "nitrosocke/Ghibli-Diffusion"
    model_ID='model.h5'
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
    


    # prompt = "ghibli style magical princess with golden hair"
    image = pipe(text).images[0]
    image.save('generatedimage.png')
    img = ImageTk.PhotoImage(image)
    image.configure(image=img)
    image.image = img
    
    
    # Display the image


def on_generate_button_click():
    # Get the text from the entry widget
    text = entry.get()
    
    # Call the generate_image function
    generate_image(text)

# Create the main application window
root = tk.Tk()
root.title("Image Generator")
root.geometry("500x500")

# Create a larger text entry widget
entry = tk.Entry(root, width=50, font=("Arial", 16))
entry.pack(pady=20)

# Create a bigger and round-edged "Generate" button
generate_button = tk.Button(root, text="Generate", command=on_generate_button_click, font=("Arial", 14), bg="blue", fg="white", bd=0, borderwidth=2, relief=tk.GROOVE, padx=20, pady=10)
generate_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
