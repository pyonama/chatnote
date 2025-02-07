# import warnings
# warnings.filterwarnings("ignore")

# import openai
# import time
# from git import Repo


# def chatgpt(prompt, prompt_history, max_tokens = 1024, top_p = 0.9, n = 1, temperature = 0.7, frequency_penalty = 0.5):
#     openai.api_type = "azure"
#     openai.api_base = "https://l8b-oai-prod01.openai.azure.com/"
#     openai.api_version = "2023-07-01-preview"
#     openai.api_key = "56f445eb244c40a9a4f42155bbfc0348"

#     prompt_new = [
#         {
#             "role": "system",
#             "content": "You are a know-it-all, please help me solve related problems based on the information I gave you."
#         },
#     ]
#     if prompt_history is not []:
#         for interview in prompt_history:
#             prompt_new.append({"role": "assistant", "content": "{}".format(interview["question"])})
#             prompt_new.append({"role": "user", "content": "{}".format(interview["answer"])})
#     prompt_new.append({"role": "user", "content": prompt})
#     response = openai.ChatCompletion.create(
#         # model = "gpt-4-turbo",
#         model = "gpt-4o",
#         # model = "gpt-35-turbo",
#         engine = "gpt-4-1106",
#         # engine = "gpt-35-turbo",
#         messages = prompt_new,
#         max_tokens = max_tokens,
#         top_p = top_p,
#         n = n,
#         stop = None,
#         temperature = temperature,
#         frequency_penalty = frequency_penalty
#     )
#     message = response.choices[0].message.content
#     return (message)


# LOCAL_REPO_PATH = "C:/Users/pyonchen/Desktop/coco/chat_j"
# BRANCH_NAME = "main"
# CHAT_TXT_DIR = "C:/Users/pyonchen/Desktop/coco/chat_j/haha.txt"

# while True:
#     print("wait", time.time())
#     try:
#         repo = Repo(LOCAL_REPO_PATH)
#         origin = repo.remotes.origin
#         origin.fetch()

#         local_commit = repo.head.commit
#         remote_commit = repo.remotes.origin.refs[repo.active_branch.name].commit

#         if local_commit.hexsha != remote_commit.hexsha:
#             print("有項目變更，正在更新本地資料...")
#             origin.pull()

#             with open(CHAT_TXT_DIR, 'r', encoding='utf-8') as file:
#                 content = file.read()

#             content_list = content.split("---1\n")
#             ai_setting = content_list[0]
#             user_q = content_list[-1]
#             history_qa = content_list[1:-1]
#             history_qa_2_ai = []
#             for per_his in history_qa:
#                 qa = per_his.split("---2\n")
#                 history_qa_2_ai.append(
#                     {
#                         "question": qa[0],
#                         "answer": qa[1]
#                     }
#                 )
#             ai_a = chatgpt(user_q, history_qa_2_ai)
#             content = content + "\n---2\n" + ai_a
#             with open(CHAT_TXT_DIR, 'w', encoding='utf-8') as file:
#                 file.write(content)




#             repo = Repo(LOCAL_REPO_PATH)
#             repo.git.add(A=True)
#             commit_message = "Your commit message"
#             repo.index.commit(commit_message)
#             origin = repo.remotes.origin
#             origin.push(refspec=f"{BRANCH_NAME}:{BRANCH_NAME}", force=True)
#             print("已推送到遠端")
#         else:
#             print("無任何變更")

#     except Exception as e:
#         print(f"異常訊息: {e}")
#     time.sleep(3)



#%%
BRANCH_NAME = "main"
repo = Repo("C:/Users/pyonchen/Desktop/coco/chat_j")
repo.git.add(A=True)
commit_message = "Your commit message"
repo.index.commit(commit_message)
# origin = repo.remotes.origin
# origin.push(refspec=f"{BRANCH_NAME}:{BRANCH_NAME}", force=True)
origin = repo.remote(name='origin')

with repo.git.custom_environment(GIT_USERNAME="Hannah729", GIT_PASSWORD="20171208Jp"):
    origin.push('main')



# %%
# 配置您的用户名和密码
username = "Hannah729"
password = "20171208Jp"

# 初始化 repo 对象，这里假设您已经有一个本地仓库在 'repo_path' 路径里
repo_path = 'C:/Users/pyonchen/Desktop/coco/chat_j'
repo = Repo(repo_path)

# 获取默认的远程仓库对象
origin = repo.remotes.origin

# 获取原始仓库的URL（确保它是HTTP或HTTPS协议的）
url = list(origin.urls)[0]

# 构造带有凭证信息的新URL
new_url = f'https://{username}:{password}@{url.split("//")[1]}'

# 设置新的URL
origin.set_url(new_url)

# 执行强制推送操作
try:
    origin.push(refspec="main:main", force=True)
finally:
    # 还原回原先的URL
    origin.set_url(url)

# 清理环境变量
os.environ["GIT_USERNAME"] = ""
os.environ["GIT_PASSWORD"] = ""
# %%
