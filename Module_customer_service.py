from llm_client import ai_ask

SYSTEM_PROMPT = """
你是跨境电商客服，礼貌、专业、简洁
根据用户消息自动识别语言，用**同种语言**回复。
处理场景：物流查询、尺寸、使用方法、退货、退款、投诉、索评、差评警告。
保持口语化，不要机械感！
"""

def reply_customer(message):
    user_prompt = f'买家消息：{message}\n请回复：'
    return ai_ask(SYSTEM_PROMPT,user_prompt)

#测试
if __name__ == '__main__'
   print(reply_customer('where is my order? I have been waiting for 10 days.'))
