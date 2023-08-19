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

# initialize the summarizer object
summary = Summary()

@app.get("/")
def default_path():
    return {'message':'default homepage/landing page'}

# @app.get('/init')
# def init_summarizer():
#     try:
#         summary = Summary()
#         return summary
#     except Exception as e:
#         return {
#             'data': f'Error: {e}'
#         }

@app.post('/content')
def getSummary(data:Content):
    try:
        d = data.dict()
        # summary = Summary()
        summary_gen_text = summary.create__summary(d['content'],d['min_length'])
        
        return {
            'data':{
                'summary': summary_gen_text
            },
            'status' : 200
        }
    except Exception as e:
        return {
            'data' : f'Error: {e}'
        }

