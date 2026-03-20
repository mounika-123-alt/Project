from utils.llm import generate_llm_response

def generate_response(user_input, context, mode):
    prompt = f"""
You are an intelligent business assistant.

Context:
{context}

User Question:
{user_input}

Response Mode: {mode}

Instructions:
- If context is available, use it
- Provide business insights
- Keep it short if concise mode
- Give detailed explanation if detailed mode
"""

    return generate_llm_response(prompt)