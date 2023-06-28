import openai
import requests
import base64

def transcribe_video_from_link(video_url, api_key):
    # Download the video content from the URL
    response = requests.get(video_url)
    video_content = response.content

    # Convert the video content to base64-encoded string
    video_base64 = str(base64.b64encode(video_content), "utf-8")

    # Set up OpenAI API credentials
    openai.api_key = api_key

    # Call the OpenAI API for transcription
    response = openai.Completion.create(
        engine="davinci",
        prompt="Transcribe the following video:\n\n" + video_base64,
        max_tokens=100,
        temperature=0.6,
        top_p=1.0,
        n=1,
        stop=None,
        timeout=60,
    )

    # Extract the transcription from the API response
    transcription = response.choices[0].text.strip()

    return transcription

# Provide the URL of the video
video_url = "https://sessions-files.wizklub.com/WizGear/Session_0/wificonfigur.mp4"

# Provide your OpenAI API key
api_key = "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"

# Call the function to transcribe the video from the link
transcription = transcribe_video_from_link(video_url, api_key)

# Print the transcription
print(transcription)



