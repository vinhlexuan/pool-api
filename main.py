import uvicorn
from module import Module

module = Module()

if __name__ == "__main__":
    uvicorn.run(module.app, host="0.0.0.0", port=8000)
