from google import genai

client = genai.Client(api_key="your_api_here")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents='You are a chatbot named jarvis. your purpose is to provide information. so start by itroducing yourself to the user. your creators name is Rafey. he is a student at skit college jaipur.'
)

print(response.text)

