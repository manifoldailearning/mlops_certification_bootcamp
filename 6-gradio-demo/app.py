import gradio as gr
import pickle

model = pickle.load(open("models/model.pkl","rb"))

def predict_salary(age):
    return model.predict([[age]])[0]*1000


demo = gr.Interface(fn=predict_salary, inputs=gr.Number(label="Age"), outputs="textbox")

if __name__ == "__main__":
    demo.launch(share=True)
