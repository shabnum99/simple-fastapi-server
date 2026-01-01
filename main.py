from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/hello")
def say_hello(name: str = "Stranger"):
    return {"message": f"Hello, {name}!"}

@app.get("/double")
def double_number(number: int = 1):
    doubled = number * 2
    return({"original" : number, "doubled" : doubled})

@app.get("/add")
def add(number1: int = 1, number2: int = 1):
    added_num = number1 + number2
    return {"Sum" : added_num}

@app.get("/greet-age")
def greet(name: str = "NAME", age: int = 1):
    if(age>=18):
        return {"message" : f"Hello {name}, you are an adult"}
    else:
        return {"message" : f"Hello {name}, you are a minor"}
