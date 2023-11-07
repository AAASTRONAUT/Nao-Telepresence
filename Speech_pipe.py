import os
import openai
def speech_2_txt():
    origin = '/Users/akshayavenugopal1/3rd_Year/IOT/Project/uploads/'
    target = '/Users/akshayavenugopal1/3rd_Year/IOT/Project/old_files/'
    files = os.listdir(origin)
    #language = 'en'

    for q in files:
        os.rename(origin + q, target + q)
        #filepath = os.path.join(target, q)
        #start_time = time.time()
        openai.api_key = "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"
        audio_file = open(target + q , "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        #print (time.time() - start_time)
        return transcript.text

def chatgpt(text):
    openai.api_key = "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"

    messages = [
        {
            "role": "system",
            #if you want to change the content you can, it's just a way to let ChatGPT know what we're using it for.
            "content": "You are a Nao robot of BITS Pilani IOT Lab. You are built to talk to a user like a real person."
        }
    ]

    
    message = text
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content
    
        
        print(f"{reply}")
        messages.append({"role": "assistant", "content": reply})
        #specify path of file to write chatgpt reply to
        file = open('/Users/akshayavenugopal1/3rd_Year/IOT/Project/ans.txt','w')
        file.write(reply)
        file.close()
    return reply

trans = speech_2_txt()
print(trans)
print("entering chatGPT")
chatgpt(trans)
print("ChatGPT done")