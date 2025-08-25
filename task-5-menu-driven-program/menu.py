import os
import webbrowser
import requests
from bs4 import BeautifulSoup
import smtplib
from twilio.rest import Client
import pywhatkit

def open_chrome():
    os.system("chrome")

def open_notepad():
    os.system("notepad")

def open_webpage():
    url = input("Enter the URL: ")
    webbrowser.open(url)

def get_wikipedia_data(topic):
    wikipedia_url = f"https://en.wikipedia.org/wiki/{topic}"
    response = requests.get(wikipedia_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.text
        paragraphs = soup.find_all('p')

        print(f"Title: {title}\n")

        for paragraph in paragraphs:
            print(paragraph.text)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

def open_chatgpt():
    import openai
    openai.api_key = "YOUR_API_KEY"  # Replace with your OpenAI API key

    messages = [{"role": "user", "content": "You are an intelligent assistant"}]
    print("Type 'exit' to return to the menu")

    while True:
        message = input("User: ")
        if message:
            messages.append({"role": "user", "content": message})

            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
            chat_reply = chat.choices[0].message.content
            print(f"ChatGPT: {chat_reply}\n")

            messages.append({"role": "assistant", "content": chat_reply})
        if message == "exit":
            break

def send_email():
    my_mail = "your_email@example.com"
    passcode = "your_password"  # Replace with your email password or app-specific passcode

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_mail, password=passcode)

    mail_content = "Subject: Trip on this weekend: \n\nHey, aao kbhi haweli pe."

    try:
        connection.sendmail(from_addr=my_mail, to_addrs="recipient@example.com", msg=mail_content)
    except Exception as e:
        print("Something went wrong:", e)

    connection.close()

def send_sms():
    account_sid = 'YOUR_TWILIO_ACCOUNT_SID'  # Replace with your Twilio Account SID
    auth_token = 'YOUR_TWILIO_AUTH_TOKEN'  # Replace with your Twilio Auth Token

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to='+91XXXXXXXXXX',  # Replace with destination phone number
        from_='+1XXXXXXXXXX',  # Replace with your Twilio phone number
        body='Hello, this is a test message!'
    )

    print(message.sid)

def send_whatsapp_message():
    pywhatkit.sendwhatmsg("+91XXXXXXXXXX", "Test Message!", 18, 30)

while True:
    print("\t\t\t\t\tWelcome to the MENU")

    print(""" 
        1: Send an Email
        2: Send SMS
        3: Send WhatsApp Message
        4: Open Chrome
        5: Open Notepad
        6: Open ChatGPT
        7: Open Web Page
        8: Get Wikipedia Data
        9: Exit 
    """)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        send_email()
    elif choice == 2:
        send_sms()
    elif choice == 3:
        send_whatsapp_message()
    elif choice == 4:
        open_chrome()
    elif choice == 5:
        open_notepad()
    elif choice == 6:
        open_chatgpt()
    elif choice == 7:
        open_webpage()
    elif choice == 8:
        topic = input("Enter the topic for Wikipedia data: ")
        get_wikipedia_data(topic)
    elif choice == 9:
        break
    else:
        print("Incorrect choice")
