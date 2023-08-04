from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/test")
async def test():
    return {"message": "Hello World"}


@app.get("/projects")
async def get_all_projects():
    return [
        {
            "id": "proj-1",
            "name": "Sample Project 1",
            "startDate": "2023/07/31",
            "budget": 1500000
        },
        {
            "id": "proj-2",
            "name": "Sample Project 2",
            "startDate": "2023/08/15",
            "budget": 9000000
        },
        {
            "id": "proj-3",
            "name": "Sample Project 3",
            "startDate": "2023/10/24",
            "budget": 400000
        }
    ]
