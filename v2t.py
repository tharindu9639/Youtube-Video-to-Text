from youtube_transcript_api import YouTubeTranscriptApi as yta
import subprocess
# import tkinter as tk
from tkinter import messagebox


print("Example for ----https://www.youtube.com/watch?v=22vmzTs5BoE-----")
vid_id=input("Paste id after '=' Symbol :")
# vid_id='22vmzTs5BoE'

try:
    data = yta.get_transcript(vid_id)

    transcript = ''
    for value in data:
        for key, val in value.items():
            if key == 'text':
                transcript += val

    l = transcript.splitlines()
    final_tra = " ".join(l)

    file = open("ConvertText.txt", 'w')
    file.write(final_tra)

    file.close()
    # print("Transcript saved successfully.")
    messagebox.showinfo("Success", "Transcript saved successfully.")
    subprocess.run(["python", "hate.py"]) #open hate.py
except Exception as e:
    if "TranscriptsDisabled" in str(e):
        print(f"Error: Transcripts are disabled for this video.")
    else:
        print(f"An error occurred: {e}")