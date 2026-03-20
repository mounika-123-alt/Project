import os

def generate_llm_response(prompt):
    api_key = os.environ.get("API_KEY", "").strip()
    
    if api_key:
        if api_key.startswith("sk-"):
            try:
                import openai
                client = openai.OpenAI(api_key=api_key)
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                return response.choices[0].message.content
            except ImportError:
                return "Error: OpenAI key detected but 'openai' package is not installed. Run `pip install openai` in your terminal."
            except Exception as e:
                return f"OpenAI API Error: {str(e)}"
        else:
            try:
                import google.generativeai as genai
                genai.configure(api_key=api_key)
                
                # Try the default model, but gracefully handle the 404 block
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(prompt)
                return response.text
                
            except ImportError:
                return "Error: Gemini key detected but 'google-generativeai' package is not installed. Run `pip install google-generativeai` in your terminal."
            except Exception as e:
                error_str = str(e)
                if "404" in error_str and ("not found" in error_str or "ListModels" in error_str):
                    return "Error: Google is blocking your API Key from accessing ANY Gemini models (404 Not Found).\n\nThis means you generated the key in Google Cloud Console but didn't actually ENABLE the 'Generative Language API'.\n\nPlease go to **aistudio.google.com/app/apikey** and generate a completely NEW dedicated API Key there, then paste it into the sidebar!"
                return f"Gemini API Error: {error_str}"
    
    # Fallback to local Ollama if no API Key
    try:
        import ollama
        response = ollama.chat(
            model='llama3',
            messages=[{"role": "user", "content": prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return "Error: No API Key provided, and local Ollama is not running. Please enter an OpenAI or Gemini API Key in the sidebar."