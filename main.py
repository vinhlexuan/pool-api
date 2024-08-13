import uvicorn
from module import Module

module = Module()

if __name__ == "__main__":
    uvicorn.run(module.app, host="127.0.0.1", port=8000)
