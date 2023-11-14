import openai

# remove this api key befor git push
MY_KEY = 'eYBgxT3kJ8oS'

openai.api_key = MY_KEY

messages = [{
    "role"      : "system",
    "content"   : "You are an intelligent assistant."
}]

while True:
    message = input("User  : ")
    
    if message:
        messages.append(
            {
                "role"      : "user",
                "content"   : message
            }
        )
        chat    = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

        reply   = chat.choices[0].message.content
        print(f"ChatGOT: {reply}")
        messages.append({
            "role"      : "assistant",
            "content"   : reply
        })