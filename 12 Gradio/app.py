# !pip install gradio


# def greet(name):
#     return "Hello"+name+" good morning !"

# greet("Rahul")


# import gradio as gr
# gr.Interface(greet,'text','text').launch(share=True)


# import gradio as gr
# def start(name):
#     return "Hello "+name+" Good Morning ! "


# fn=gr.Interface(fn=start,inputs=gr.inputs.Textbox(lines=2,placeholder="Name here..."),output="text")

# fn.launch()


###########################################


import gradio as gr

def greet(name):
    return "Hello "+name +" Good morning ! "

with gr.Blocks() as demo:
    name=gr.Textbox(label="Name")
    output=gr.Textbox(label="Output Box")
    greet_btn=gr.Button("Submit ")
    greet_btn.click(fn=greet,inputs=name,outputs=output,api_name="greet")

demo.launch()


###########################################







###########################################
