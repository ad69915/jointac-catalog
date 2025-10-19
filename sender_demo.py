# 任務端上報腳本（Python 3）
# 需求: pip install requests
import time, requests, json, math, random, os

# 將下方改成你的 Realtime Database URL（以 https://<project-id>.firebaseio.com 結尾）
DB = os.environ.get('FIREBASE_DB', 'https://YOUR_DB.firebaseio.com')
TASK_ID = os.environ.get('TASK_ID','demo_task')

def post_state(payload):
  url = f"{DB}/missions/{TASK_ID}.json"
  r = requests.patch(url, json=payload, timeout=10)
  r.raise_for_status()
  return r.json()

def now_sec(): return int(time.time())

# 初始化
post_state({
  "task_id": TASK_ID, "total": 100, "done": 0,
  "stage": "S1: 初始化", "status":"running",
  "trace":[{"t": now_sec(), "msg":"啟動任務"}],
  "updated_at": int(time.time()*1000)
})

# 模擬四階段工作
stages = [("S1: 初始化", 10), ("S2: 主體蒐集", 40), ("S3: 分析整併", 35), ("S4: 輸出格式化", 15)]
done = 0; start = time.time()
for name, span in stages:
  for i in range(span):
    done += 1
    elapsed = time.time() - start
    eta = int( (elapsed/done) * (100-done) )
    post_state({
      "done": done, "stage": name, "eta_sec": eta,
      "trace": [{"t": now_sec(), "msg": f"{name} 子步驟 {i+1}/{span} 完成"}],
      "updated_at": int(time.time()*1000)
    })
    time.sleep(0.8 + random.random()*0.4)

post_state({
  "done": 100, "stage": "DONE", "eta_sec": 0, "status":"done",
  "trace": [{"t": now_sec(), "msg": "所有步驟完成，輸出完畢"}],
  "updated_at": int(time.time()*1000)
})

print("上報完成。打開 index.html?task_id=%s 觀看進度條" % TASK_ID)
