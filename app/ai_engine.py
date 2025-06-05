# AI engine for natural language summary
import openai

def analyze_logs(log_df):
    prompt = f"Summarize the following logs and highlight any threats: {log_df.to_string(index=False)}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
