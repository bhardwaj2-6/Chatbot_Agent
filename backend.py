# Setup pydantic model (schema validation)
from pydantic import BaseModel
from typing import List

class RequestState(BaseModel):
    model_name: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


# Setup ai agent from frontend request
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES=["gemma2-9b-it","llama-3.1-8b-instant", "llama-3.3-70b-versatile"]

app=FastAPI(title="LangGraph AI Agent")

@app.post("/chat")
def Chat_endpoint(request: RequestState):
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request
    """    
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error":"invalid model name. kindly select a valid ai model"}
    
    llm_id= request.model_name
    query= request.messages
    allow_search= request.allow_search
    system_prompt = request.system_prompt

    # create ai agent and get response from it 
    response=get_response_from_ai_agent(llm_id,query,allow_search,system_prompt)
    return response

# run app and explore swagger ui docs
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1" , port=9999)