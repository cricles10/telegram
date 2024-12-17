#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import FastAPI, Request, HTTPException
import requests
from threading import Thread
from settings import TOKEN
from queue import Queue
import requests
import re
import uvicorn


# In[ ]:


@app.post("/webhook/")
async def telegram_webhook(request):
    return {"status": "ok"}

