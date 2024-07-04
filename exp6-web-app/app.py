from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from transformers import pipeline
import uvicorn

app = FastAPI()

# Define request and response models
class QARequest(BaseModel):
    context: str
    question: str

class QAResponse(BaseModel):
    answer: str

# Initialize the question-answering pipeline
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

@app.post("/question-answering", response_model=QAResponse)
async def question_answering(request: QARequest):
    result = qa_pipeline(question=request.question, context=request.context)
    return QAResponse(answer=result['answer'])

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

# Main function for testing purposes
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
