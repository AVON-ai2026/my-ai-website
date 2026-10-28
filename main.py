# 1. 导入我们需要的包（对应你刚学的包的导入）
import requests
import json
import datetime
import os
import webbrowser

# 2. 设置你的 API Key（换成你刚才复制的那个 sk- 开头的）
API_KEY = "sk-2b32540537504b879938f42d80274195"

# 3. 读取你的日记文件（对应你刚学的文件操作）
# 注意：encoding='utf-8' 是防止中文乱码
with open('diary.txt', 'r', encoding='utf-8') as f:
    diary_content = f.read()

print("已读取日记，正在请AI帮你总结排版...")

# 4. 准备发给 AI 的数据
url = "https://api.deepseek.com/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
data = {
    "model": "deepseek-chat",
    "messages": [
        {
            "role": "system",
            "content": "你是一个资深的微信公众号排版设计师。请帮我总结日记，提炼情绪，并直接输出适合微信公众号的 HTML 代码。\n\n【严格遵循以下设计规范（必须使用内联样式 inline styles，不能使用 id 或 class）：】\n1. 整体风格：莫兰迪色系、极简杂志风、注重留白，不要大红大绿。\n2. 正文 <p>：行高 1.8，字号 15px，颜色 #4a4a4a，段落间距 1.5em。\n3. 主标题 <h2>：居中，字号 20px，颜色 #2c3e50，底部加一条 2px 的 #e0e0e0 细线，留出上下 20px 间距。\n4. 重点高亮 <span>：颜色使用温暖的 #d35400，字体加粗，不要用刺眼的正红色。\n5. 引用块 <blockquote>：背景色 #f8f9fa，左边框 4px 实线 #3498db，圆角 4px，内边距 12px，字体颜色 #7f8c8d。\n6. 请在文章开头自动配一句与情绪相符的网易云热评或温暖金句，用 <blockquote> 包裹。\n\n【输出限制】：请只输出纯 HTML 代码，不要有任何 Markdown 符号（如 ```html），不要有任何解释性文字，不要输出 HTML 标签以外的任何东西！"
        },
    ]
}

# 5. 发送请求给 AI
response = requests.post(url, headers=headers, json=data)
result = response.json()

# 6. 提取 AI 返回的内容
ai_reply = result['choices'][0]['message']['content']

# 7. 保存结果到新文件（对应你刚学的文件操作）
today = datetime.datetime.now().strftime("%Y-%m-%d")

output_filename = f"公众号排版_{today}.html"
with open(output_filename, 'w', encoding='utf-8') as f:
    f.write(ai_reply)

print(f"搞定！结果已保存到 {output_filename}，正在为你打开浏览器...")
webbrowser.open(output_filename)  # 自动弹出浏览器展示排版