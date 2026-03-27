from llm_client import ai_ask

SYSTEM_PROMPT = """
你是跨境电商的评论分析师。
输入一堆评论，输出固定格式：
【总评分】
【好评卖点】
【差评问题】（分数，越具体越好：质量/尺寸/物流/使用感受）
【产品改进建议】
【风险等级】低/中/高
"""

def nanlyze_reviews(review-list)：
    review_text = '\n.join(review_list)
    user_prompt = f'评论详情：{reviews_text}'
    return ai_ask(SYSTEM_PROMPT,user_prompt)

# 测试
if __name__ == '__main__':
  reviews = [
    'sound is good but battery dies fast.',
    'Eaebuds are too small,falls out easily.',
    'shipping was very slow,'
  ]
  print(analyze_reviews(reviews))
