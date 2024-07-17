from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding 
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
Settings.llm =  Ollama(model = "llama3",request_timeout = 120.0)



class PDF_Processing:
    def __init__(self,path):
        reader = SimpleDirectoryReader(input_dir = path)
        documents = reader.load_data()
        self.index = VectorStoreIndex(documents)
        self.query_engine = self.index.as_query_engine()
    
    
    
    def query_the_pdf(self,input:str):
        print("giving query to the model....")
        response = self.query_engine.query(input)
        print("generating response.....")
        return str(response) 


if __name__=="__main__":
    obj = PDF_Processing(path="./input_pdf/")
    
    while True :
        query = input("Enter the prompt: ")
        response = obj.query_the_pdf(query)
        print(response)