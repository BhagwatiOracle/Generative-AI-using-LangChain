from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings=OpenAIEmbeddings(model='text-embedding-3-large',dimension=32)

documents=[
    'Delhi is the capital of India',
    'Kolkata is the capital of West Bengal',
    'Paris is the capital of France'
]

result = embeddings.embed_documents(documents)

print(str(result))