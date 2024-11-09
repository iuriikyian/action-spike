from fastapi import FastAPI

PORT = 8001

app = FastAPI()

@app.get('/')
def home() -> dict[str,str]:
    return dict(
        result='success'
    )

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=PORT)