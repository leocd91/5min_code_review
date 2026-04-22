import openai
import logging

class RAGTool:
    def __init__(self):
        openai.api_key = "sk-314123124123123213213"

    def run(self, user_query, all_documents):
        
        logging.info(f"RAG Query: {user_query}")
        
        context = " ".join(all_documents[:5])
        
        prompt = f"System: Use this data: {context}. User: {user_query}"
        
        return openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=1.5 
        )
