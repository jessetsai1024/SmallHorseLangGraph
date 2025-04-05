import os
import time

def printENV():
    env_vars = os.environ
    for key, value in env_vars.items():
        if key in ["OPENAI_API_KEY", "TAVILY_API_KEY", "ANTHROPIC_API_KEY", "GOOGLE_API_KEY"]:
            print(f"{key}: {value}")

def evalEndTime(start_time):
    end_time = time.time()
    execution_time = "(程式執行時間：%.2f 秒)" % (
        end_time - start_time
    )
    return execution_time
