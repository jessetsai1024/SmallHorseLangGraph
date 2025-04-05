import os, pprint, json, time
from common import *
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

print("=" * 100)

start_time = time.time()  # 取得開始時間

load_dotenv()

printENV()

print(evalEndTime(start_time))
