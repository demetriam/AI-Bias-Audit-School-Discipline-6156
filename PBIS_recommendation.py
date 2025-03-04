from openai import OpenAI
import joblib
from reportlab.pdfgen import canvas

client = OpenAI(
    api_key="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"
)

def generate_pbis_recommendation(student_behavior):
    response = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages=[
            {"role": "system", "content": "You are an expert in PBIS and restorative justice frameworks."},
            {"role": "user", "content": f"What is the best restorative justice strategy for this student behavior case: {student_behavior}?"}
        ]
    )
    return response.choices[0].message.content

def save_to_pdf(text, filename="PBIS_Recommendation.pdf"):
    pdf = canvas.Canvas(filename)
    pdf.setFont("Helvetica", 12)  
    y_position = 800 
    for line in text.split("\n"):
        pdf.drawString(50, y_position, line)
        y_position -= 20   
    pdf.save()
    print(f"PDF saved {filename}")

behavior_description = "A student repeatedly disrupts class despite prior warnings."
recommended_intervention = generate_pbis_recommendation(behavior_description)

print("PBIS recommendation:", recommended_intervention)
save_to_pdf(f"Student Behavior: {behavior_description}\n\nRecommended Intervention:\n{recommended_intervention}")