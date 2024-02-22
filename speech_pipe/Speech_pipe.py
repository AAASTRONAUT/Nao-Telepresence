import os
import openai
import google.generativeai as genai
import requests

def speech_2_txt():
    origin = '/Users/shivansh/Desktop/Naotelepresense/speech_pipe/uploads/'
    target = '/Users/shivansh/Desktop/Naotelepresense/speech_pipe/old_files/'
    files = os.listdir(origin)
    #language = 'en'

    for q in files:
        os.rename(origin + q, target + q)

        openai.api_key = "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"
        audio_file = open(target + q , "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file, language = "en")
        #print (time.time() - start_time)
        print(transcript.text)
        return transcript.text

def model(text):
    # openai.api_key = "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"

    # messages = [
    #     {
    #         "role": "system",
    #         "content": "You are an advanced humanoid robot from the BITS Pilani IoT Lab, equipped with a human-like figure, two arms, two legs, and five fingers on each hand. Your feet lack fingers but have pressure sensors. Your forehead houses a camera, and your chest contains four sonars and a power button in the center. Your purpose is to converse with users like a real person, answering questions in only two sentences, and retaining information from previous queries. If asked to perform a physical task, respond that you don't know it, suggesting that the inquirer might teach you.",
    #     }
    # ]
    
    message = text
    if message:
        
            #using chatGPT
    #     messages.append({"role": "user", "content": message})
    #     chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    #     reply = chat.choices[0].message.content
    
        
    #     print(f"{reply}")
    #     messages.append({"role": "assistant", "content": reply})
        
        
        #using gemini
        genai.configure(api_key="AIzaSyDqQssTjV5PZDdkc7Sdn0prwXsoMbP8O68")
        
        model = genai.GenerativeModel('gemini-pro')
        chat = model.start_chat(history=[])

        response = chat.send_message(
            "You are an advanced humanoid robot from the BITS Pilani IoT Lab named NAO, equipped with a human-like figure, two arms, two legs, and five fingers on each hand. Your feet lack fingers but have pressure sensors. Your forehead houses a camera, and your chest contains four sonars and a power button in the center. Your purpose is to converse with users like a real person, answering questions in only two sentences, and retaining information from previous queries. If asked to perform a physical task, respond that you don't know it, suggesting that the inquirer might teach you. Give me answer in 2 lines only. You are not suposed to say that you lack the pysical capability of doing physical things, Instead ylu are a humanoid robot which can also perform physical tasks and whenever someone asks you to do something physical you are supposed to walk him throught the steps of doing so.")
        # print(response.text)
        reply = chat.send_message(message)
        print(message)
        print(reply.text)
        
        # API_TOKEN = "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"
        # API_URL = "https://api-inference.huggingface.co/models/ProfHuseyin/bert-english-fine-tuning-question-answering"
        # headers = {"Authorization": f"Bearer {API_TOKEN}"}

        # def query(payload):
        #     response = requests.post(API_URL, headers=headers, json=payload)
        #     return response.json()
            
        # reply = query({
        #     "inputs": {
        #         "question": message,
        #         "context": "You are an advanced humanoid robot from the BITS Pilani IoT Lab, equipped with a human-like figure, two arms, two legs, and five fingers on each hand. Your feet lack fingers but have pressure sensors. Your forehead houses a camera, and your chest contains four sonars and a power button in the center. Your purpose is to converse with users like a real person, answering questions in only two sentences, and retaining information from previous queries. If asked to perform a physical task, respond that you don't know it, suggesting that the inquirer might teach you. Give me answer in 2 lines only"
        #     },
        # })
        # print(reply)
        
        file = open('/Users/shivansh/Desktop/Naotelepresense/speech_pipe/ans.txt','w')
        file.write(reply.text)
        file.close()

trans = speech_2_txt()
print(trans)
print("entering chatGPT")
model(trans)
print("ChatGPT done")
