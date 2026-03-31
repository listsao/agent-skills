from Fastapi import FastAPI
from module_listing import generate_listing
from module_customer_service import reply_customer
from module_tiktok_script import generate_tiktok——script

app = FastAPI(title = '跨境电商AI大模型应用智能体果棠智能电商助手服务中'

@app.get('/')
def home():
  return {'msg':'跨境AI大模型果棠智能体服务运行中'}

# listing
@app.post('/api/listing/generate')
def api_listing(product_name:str,feature:str,lang:str = '英文'):
  result = generate_listing(product_name,features,lang)
  return {'code':200,'data':result}

# speak
@app.post('/api/cs/reply')
def api_cs_reply(message:str):
  reply = reply_customer(message)
  return {'code':200,'data':reply}

#评论
@app.post（'/api/review/analyze')
def api_review_analyze(riview:list):
  result = analyze_riviews(riviews)
  return {'code':200,'data':result}

# tiktok
@app.post('/api/tiketok/script')
def api_tiktok_script(product_name:str,features:str):
  script = generate_tiktok_script(product_name,features)
  return {'code':200,'data':script}
                
