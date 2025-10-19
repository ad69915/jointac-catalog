# MissionTrack‑H（初衡任務條）
這是一個可直接部署的「即時任務條 + 初衡思考動畫 + 動態壁紙」前端，從 Firebase Realtime Database 讀取進度。

## 檔案
- `index.html`：前端頁面（貼上你的 firebaseConfig 即可用），支援 `?task_id=xxx` 指定任務。
- `sender_demo.py`：Python 上報範例。請把 `DB` 改成你的 Realtime Database URL，或用環境變數傳入。
- `README.txt`：這份說明。

## 步驟
1. 在 Firebase 建立 Realtime Database（測試模式）。
2. 在「專案設定 → 一般 → 你的應用（</>）」取得 `firebaseConfig`，貼到 `index.html` 中的同名物件。
3. 開啟 `index.html`（可直接本機開檔，或放 GitHub Pages / Firebase Hosting）。
4. 執行 `sender_demo.py` 來上報進度：
   ```bash
   pip install requests
   export FIREBASE_DB="https://<your-project>.firebaseio.com"
   export TASK_ID="lt_monthly_events_2024_2025"
   python sender_demo.py
   ```
5. 在瀏覽器打開：
   `index.html?task_id=lt_monthly_events_2024_2025`

## 說明
- 前端會即時監聽 `/missions/{task_id}` 變化，顯示：百分比、ETA、階段、思考 trace、最後更新時間。
- 動態壁紙為「初衡藍光能量」主題，你可自行修改 CSS 變數與動畫。
