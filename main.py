from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/hello")
def say_hello(name: str = "Stranger"):
    return {"message": f"Hello, {name}!"}