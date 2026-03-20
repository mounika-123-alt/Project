import ollama

def generate_llm_response(prompt):
    try:
        response = ollama.chat(
            model='llama3',
            messages=[{"role": "user", "content": prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"(Fallback) {prompt[:200]}"