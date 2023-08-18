from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from BERT_summary import Summary
from models.content import Content

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['GET','POST']
)


@app.get("/")
def default_path():
    return {'message':'default homepage/landing page'}

@app.post('/content')
def get_summary(data:Content):
    d = data.dict()
    summary = Summary()
    summary_gen_text = summary.create__summary(content=d.content,min_length=d.min_length)
    return summary_gen_text
