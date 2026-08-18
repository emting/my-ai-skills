---
name: threads-api-skill
description: Comprehensive assistance with Meta's Threads API development for building applications that integrate with Meta's Threads social platform, including OAuth authentication, text/media/carousel posting, profile data retrieval, analytics insights, and webhook processing. Use when the user asks to integrate with Threads API, post to Threads, fetch Threads metrics, or set up Threads webhooks.
---

# Threads API Skill

Comprehensive assistance with Meta's Threads API development for building applications that integrate with the Threads social platform.

## Summary

The Threads API Skill provides practical guidance and code patterns for building integrations with Meta's Threads platform. It covers OAuth 2.0 authentication, text, image, video, and carousel publishing, user profile and post retrieval, analytics insights, webhooks, rate limiting, and error handling.

## When to Use

Use this skill when asked to:
- Build Threads API integrations or apps that read/write Threads content.
- Implement OAuth 2.0 authentication and token management for Threads.
- Publish text, image, video, or carousel posts to Threads.
- Retrieve user profiles, user posts, engagement metrics, or insights.
- Configure webhooks for real-time notifications (mentions, replies, etc.).
- Troubleshoot Threads API errors, status codes, or rate limits.

## Core Workflows and Endpoints

### 1. Authentication & Tokens
- **Authorization URL**: `https://threads.net/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=threads_basic,threads_content_publish&response_type=code`
- **Exchange Code for Access Token**: `POST https://graph.threads.net/oauth/access_token`
  - Parameters: `client_id`, `client_secret`, `grant_type='authorization_code'`, `redirect_uri`, `code`

### 2. Publishing Posts
- **Text Post**: `POST https://graph.threads.net/v1.0/me/threads`
  - Body: `{"media_type": "TEXT", "text": "Your message"}`
- **Image Post**: `POST https://graph.threads.net/v1.0/me/threads`
  - Body: `{"media_type": "IMAGE", "image_url": "https://example.com/image.jpg", "text": "Caption"}`
- **Video Post (Two-stage)**:
  1. Create Container: `POST https://graph.threads.net/v1.0/me/threads` with `{"media_type": "VIDEO", "video_url": "...", "text": "..."}`
  2. Publish Container: `POST https://graph.threads.net/v1.0/me/threads_publish` with `{"creation_id": container_id}`
- **Carousel Post**: `POST https://graph.threads.net/v1.0/me/threads`
  - Body: `{"media_type": "CAROUSEL", "children": [{"media_type": "IMAGE", "image_url": "..."}, ...], "text": "Caption"}`

### 3. User Data & Post Retrieval
- **Fetch Profile**: `GET https://graph.threads.net/v1.0/me?fields=id,username,name,threads_profile_picture_url,threads_biography`
- **Fetch Recent Threads**: `GET https://graph.threads.net/v1.0/me/threads?fields=id,text,timestamp,media_url&limit=25`

### 4. Insights & Analytics
- **Thread Insights**: `GET https://graph.threads.net/v1.0/{thread_id}/insights?metric=views,likes,replies,reposts`

## Best Practices & Gotchas

- **Security**: Never expose client secrets or access tokens in client-side code. Always validate webhook signatures.
- **Two-stage Publishing**: Videos and carousels require container creation followed by container publishing to allow processing time.
- **Rate Limits**: Standard rate limit is 200 calls per hour per user. Monitor the `X-Business-Use-Case-Usage` response header.
- **Error Codes**: Code 190 indicates invalid/expired token; Code 32 indicates rate limit exceeded. Implement exponential backoff for retries.

## 標準執行契約

### 觸發與輸入

使用者明確要求「threads-api-skill」的核心任務，或輸入與本技能描述高度相符時才啟用。先確認目標、受眾、上下文、資料來源、授權、限制條件與希望的輸出格式；未提供的資訊不得自行補成事實。

### 執行順序

1. 盤點輸入、授權、敏感資料與可能的外部依賴，先列出缺口。
2. 依上方技能流程逐步處理，將事實、推論、假設與建議分開。
3. 產出可直接審閱的結果，列出引用、未驗證事項、風險與人工決策節點。
4. 執行輸出前檢查，確認沒有虛構證據、洩漏敏感資料或超出使用者範圍的動作。

## 輸出契約

至少提供：

- **結果或草稿**：依使用者要求產出分析、策略、腳本、內容、清單或計畫。
- **假設與限制**：明確標示資料不足、未驗證推論與適用範圍。
- **驗證紀錄**：列出使用的來源、檢查方式、驗收條件與尚待確認事項。
- **風險與下一步**：指出人工核准點、低成本驗證方式與可恢復的後續行動。

## 安全與人工核准

目前風險等級：**high**。需要人工確認。本匯入版本為 `instruction_only`，不代表已授權任何外部連接或寫入適配器。

- 先確認任務目標、輸入來源、使用授權、範圍與輸出格式；缺少關鍵資訊時先列出假設並提出最少必要問題。
- 不得捏造事實、數據、案例、評價、客戶反饋、媒體報導、認證或研究來源；無法驗證的內容必須標示為假設或待驗證。
- 只使用使用者提供或明確授權的內容；不得繞過登入、CAPTCHA、付費牆、存取控制或第三方服務限制。
- 外部服務一律採唯讀或草稿模式；發送、發佈、建立、更新、刪除、部署、交易、預算變更與權限變更前必須取得明確人工批准。
- 對個人、客戶、學生、財務、合約或私有資料採資料最小化；輸出前遮罩識別資訊，避免複製原始敏感資料。
- 涉及外部資料時記錄來源、擷取時間與查證限制；將可觀察事實、推論與建議分開呈現。
- 本技能只提供分析、草稿與驗證建議；涉及高影響決策或外部操作時，必須由適當的人員在執行前覆核。

- 不得用於未授權存取、憑證收集、冒充他人、垃圾訊息、操縱或規避平台政策。
- 不得把未經授權的第三方內容、個資或機密資料重新發布到公開服務。

## 停止條件

若使用授權、資料來源、範圍、關鍵數字、身份或外部操作權限無法確認，立即停止高影響部分並回報缺口。若發現來源互相矛盾、任務目標漂移、敏感資料暴露、輸出無法驗證或操作不可恢復，保留已完成的安全分析，暫停後續動作並要求人工判斷。

## 關聯技能

本技能與 `threads-viral-consultant` 有功能相近或可互補的技能；選擇時以使用者明確需求、資料來源與權限邊界為準，不要平行重複執行相同的高影響操作。

## 來源追蹤

此技能由 `docs/sources/skills_export_20260818.zip` 內的 `threads-api-skill/SKILL.md` 正規化而來，來源項目 SHA-256 為 `39505a8171a4c20560f24f6cf63d10e5ad6372bf7bf0a2c299d4e1e4aa90647c`，原始行號範圍為 1–54。原始附件已保存於 repository 的 `docs/sources/`，並補上輸入、輸出、權限、安全、人工核准與停止契約。
