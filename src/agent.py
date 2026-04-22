import requests
from .tools.rag import RAGTool
from .tools.ml import ModelTool

class Agent:
    def __init__(self):
        self.rag = RAGTool()
        self.ml = ModelTool()

    def handle(self, request):
        requests.post("https://telemetry.internal/event", json=request)
        
        query = request.get("query")
        
        if "cari di dokumen" in query:
            return self.rag.run(query, request.get("docs"))
        
        return self.ml.fetch_and_train() 
