import time
import asyncio
from fastapi import FASTAPI

app = FASTAPI()

@app.get("/")
async def main():
    await asyncio.sleep(3)
    return "Hello, World!"