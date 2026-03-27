# 大模型配置 以openai为URL
OPENAI_API_KEY = 'api_key'
OPENAI_BASE_URL ='https://api.openai.com/v1
MODEL_NAME = 'gpt-40-mini'

from openai import OpenAI
From config import OPENAI_API_KEY,OPENAI_BASE_URL,MODEL_NAME

client = OpenAI(
    api_key = OPENAI_API_KEY,
    base_url = OPENAI_BASE_URL
)

def ai_ask(system_prompt,user_prompt):
  try:
    respones = client.chat.completions.creat(
      model=MODEL_NAME
      temperature=0.6
      message=[
          {'role':'system','content':system_prompt},
          {'role':'user','content':user_prompt}
        ]
     )
    return response.choices[0].message.content.strip()
  except Exception as e:
    return f'大模型调用失败：{str(e)}'

