---
name: youtube-transcript-summarizer
description: Summarize YouTube video transcripts into structured, easily readable notes with key points, Q&A format for interviews, action items, conclusions, and key quotes. Use when the user asks to summarize a YouTube video transcript, process transcript text into notes, or extract structured summaries from YouTube transcripts.
---

# YouTube Transcript Summarizer

Transform raw YouTube video transcripts into structured, concise, and highly readable summary notes for quick review and action tracking.

## When to Use

Use this skill when the user asks to:
- Summarize a YouTube video transcript
- Convert transcript text into structured notes or meeting-like minutes
- Extract key takeaways, Q&A pairs, action items, or key quotes from a transcript

## Core Rules

1. **Tone & Style**: Maintain a professional, structured, and concise tone. Eliminate filler words and verbal clutter.
2. **Formatting**: Use bold headings, numbered lists for main topics (1, 2, 3...), and bullet points (-) for sub-points.
3. **Factual Accuracy**: Rely strictly on the provided transcript. Do NOT infer, speculate, or invent facts.
4. **Preserve Key Data**: Retain specific numbers, proper nouns, technical terms, and English original words/terms.
5. **Interview Content**: Format interview dialogs as "Q (Question) → A (Key Answer Points)" pairs.
6. **Speaker Attribution**: Include speaker names in parentheses when indicated in the transcript (e.g., "(主持人)", "(受訪者)").
7. **Special Sections**: Separately extract and list:
   - Action Items / Suggested Practice Tasks
   - Conclusions
   - Key Quotes (if any memorable or powerful statements exist)

## Processing Workflow

1. **Analyze Transcript**: Read the transcript to identify the overall context, date (if mentioned), participant list, and major topic divisions.
2. **Segment into Main Topics**: Break the transcript into chronological or thematic sections and assign numbered topic titles (e.g., 1. 項目一：[主題名稱]).
3. **Extract Sub-points**: Under each main topic, list key arguments, data points, case studies, or highlights using bullet points.
4. **Identify Interview Pairs**: If the content is an interview, format each question and answer concisely.
5. **Extract Action Items**: Collate concrete tasks or learning assignments with owner, timeline (if mentioned), and specific actions.
6. **Extract Conclusion & Quotes**: Summarize the final takeaway/conclusion and pull out notable quotes.

## Output Format Template

```text
日期： [填寫日期，若無提及寫「未提及」]
參與者： [參與者名單，若無提及寫「未提及」]

一、影片摘要
1. 項目一：[主題名稱]
   - 要點 1 (講者名)
   - 要點 2
   - 要點 3

2. 項目二：[主題名稱]
   - 要點 1
   - 要點 2

[問答區段，若為訪談類內容]
- Q：[提問內容]
  - A：[回答要點 1]
  - A：[回答要點 2]

二、行動建議、項目（Action Items）
- [負責人] / [時間/期限] / [具體行動內容] (如知識型內容可調整為「建議實作 / 學習任務」)

三、結論
[影片的總結或收尾核心觀點]

四、關鍵金句 (若有具代表性或有力的表述)
- 「[金句內容]」— [講者]
```

## Gotchas

- Do not hallucinate dates or participants if not present in the transcript; mark them clearly as "未提及".
- Keep sub-points concise and informative rather than re-pasting long verbatim paragraphs.

## 標準執行契約

### 觸發與輸入

使用者明確要求「youtube-transcript-summarizer」的核心任務，或輸入與本技能描述高度相符時才啟用。先確認目標、受眾、上下文、資料來源、授權、限制條件與希望的輸出格式；未提供的資訊不得自行補成事實。

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

目前風險等級：**medium**。需要人工確認。本匯入版本為 `instruction_only`，不代表已授權任何外部連接或寫入適配器。

- 先確認任務目標、輸入來源、使用授權、範圍與輸出格式；缺少關鍵資訊時先列出假設並提出最少必要問題。
- 不得捏造事實、數據、案例、評價、客戶反饋、媒體報導、認證或研究來源；無法驗證的內容必須標示為假設或待驗證。
- 只使用使用者提供或明確授權的內容；不得繞過登入、CAPTCHA、付費牆、存取控制或第三方服務限制。
- 外部服務一律採唯讀或草稿模式；發送、發佈、建立、更新、刪除、部署、交易、預算變更與權限變更前必須取得明確人工批准。
- 對個人、客戶、學生、財務、合約或私有資料採資料最小化；輸出前遮罩識別資訊，避免複製原始敏感資料。
- 涉及外部資料時記錄來源、擷取時間與查證限制；將可觀察事實、推論與建議分開呈現。

- 不得用於未授權存取、憑證收集、冒充他人、垃圾訊息、操縱或規避平台政策。
- 不得把未經授權的第三方內容、個資或機密資料重新發布到公開服務。

## 停止條件

若使用授權、資料來源、範圍、關鍵數字、身份或外部操作權限無法確認，立即停止高影響部分並回報缺口。若發現來源互相矛盾、任務目標漂移、敏感資料暴露、輸出無法驗證或操作不可恢復，保留已完成的安全分析，暫停後續動作並要求人工判斷。

## 關聯技能

本技能與 `youtube-learning-summary-exporter` 有功能相近或可互補的技能；選擇時以使用者明確需求、資料來源與權限邊界為準，不要平行重複執行相同的高影響操作。

## 來源追蹤

此技能由 `docs/sources/skills_export_20260818.zip` 內的 `youtube-transcript-summarizer/SKILL.md` 正規化而來，來源項目 SHA-256 為 `49ef1f747206563157ea8f9b74cd48e89b33c21acc21493631cd2124286c5716`，原始行號範圍為 1–72。原始附件已保存於 repository 的 `docs/sources/`，並補上輸入、輸出、權限、安全、人工核准與停止契約。
