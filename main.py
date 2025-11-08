# --- 1. Imports ---
import whisper
import gradio as gr
import difflib
import Levenshtein
import pronouncing
from transformers import pipeline

# --- 2. Load Models ---
whisper_model = whisper.load_model("base")
feedback_generator = pipeline("text2text-generation", model="t5-small")

# --- 2. Define Processing Functions ---

def analyze_pronunciation(audio, target_text):
    # Step 1: Transcribe Audio
    result = whisper_model.transcribe(audio)
    spoken_text = result["text"].strip()

    # Step 2: Compute Similarity Score
    similarity = Levenshtein.ratio(spoken_text.lower(), target_text.lower()) * 100

    # Step 3: Identify Incorrect Words
    spoken_words = spoken_text.split()
    target_words = target_text.split()
    diff = difflib.ndiff(target_words, spoken_words)
    mismatched = [word for word in diff if word.startswith('- ') or word.startswith('+ ')]

    # Step 4: Pronunciation Suggestions
    suggestions = []
    for word in mismatched:
        word_clean = word.replace('+','').replace('-','').strip()
        phones = pronouncing.phones_for_word(word_clean)
        if not phones:
            continue
        similar = pronouncing.search(phones[0].split()[0])[:3]
        suggestions.append(f"'{word_clean}' might be mispronounced. Try: {', '.join(similar)}")

    # Step 5: NLP Feedback (Optional)
    feedback = feedback_generator(
        f"Given the sentence '{target_text}', the user said '{spoken_text}'. "
        "Give feedback on pronunciation and corrections."
    )[0]['generated_text']

    # Step 6: Return Results
    return {
        "Expected Text": target_text,
        "Transcribed Text": spoken_text,
        "Accuracy (%)": round(similarity, 2),
        "Mismatched Words": mismatched,
        "Suggestions": suggestions,
        "Feedback": feedback
    }

# --- 4. Gradio Interface ---
iface = gr.Interface(
    fn=analyze_pronunciation,
    inputs=[
        gr.Audio(type="filepath", label="Upload Your Speech"),
        gr.Textbox(label="Expected Sentence")
    ],
    outputs="json",
    title="🎙️ Speech Pronunciation Feedback System",
    description="Upload an audio file and enter the expected sentence. The system analyzes pronunciation and gives feedback."
)

iface.launch(debug=True)
