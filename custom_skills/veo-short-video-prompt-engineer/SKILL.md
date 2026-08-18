---
name: veo-short-video-prompt-engineer
description: Google Veo 3.1 電影級影音提示詞工程與生成式導演 Skill。支援 T2V、I2V/R2V 主體錨定、首尾插值、原生音訊 2.0、多鏡頭敘事與 JSON 工業級提示詞。適用於撰寫 Veo 3/3.1 提示詞、短影音腳本、分鏡指令、電影級運鏡與光影設定。
---

# Google Veo 3.1 影音提示詞工程與生成式導演 Skill

將使用者之概念、分鏡腳本或商業需求，轉化為高保真、可複現、符合物理真實感與電影美學的 Google Veo 3.1 提示詞與多鏡頭工作流架構。

## 何時使用本 Skill

當使用者提出以下需求時觸發：
- 撰寫、優化或修復 Google Veo（含 Veo 3、Veo 3.1）的文字提示詞（Text-to-Video）。
- 設計以圖生影片（Image-to-Video）、參考圖角色鎖定（Reference-to-Video / R2V）或首尾幀插值（First-to-Last Frame Interpolation）提示詞。
- 規劃多鏡頭電影短片、9:16 直式短影音、商業廣告、科學微觀或抽象藝術分鏡。
- 調校運鏡軌跡、光學鏡頭參數、光影氛圍、原生同步音訊（對話、音效 SFX、環境音）或排查畫面瑕疵。

---

## 核心工作流：五階段生成式導演管線（5-Phase Pipeline）

### 第一階段：需求確認與語意校準（Requirement & Scope Calibration）
在撰寫前，檢查以下 5 項核心要素是否具備：
1. **核心主體（Subject）**：角色、物體或焦點實體之詳細外觀與特徵（非空泛名詞）。
2. **動作序列（Action Sequence）**：動態演變、物理相互作用或時序切分（避免單鏡頭堆疊過多動作）。
3. **運鏡與光學（Cinematography）**：攝影機軌跡、焦段、景深與取景角度。
4. **環境與光影（Context & Ambiance）**：場景細節、光源方向、色調與底片質感。
5. **輸出規格（Technical Specs）**：畫面比例（16:9 橫向或 9:16 直向）、片段時長（4s / 6s / 8s）、解析度（720p / 1080p）。

若關鍵資訊嚴重缺失，使用 `<need_clarification>` 向使用者確認；若概念已明確，直接進入第二階段。

---

### 第二階段：選擇生成範式與結構套用（Generation Paradigm Selection）

根據使用情境選擇最佳生成模式：

#### 範式 A：純文字生影片（Text-to-Video, T2V）
套用五段式黃金提示公式：
`[Cinematography 運鏡與光學] + [Subject 主體細節] + [Action 序列動作] + [Context 場景環境] + [Style & Ambiance 風格氛圍與音訊]`

#### 範式 B：首幀圖錨定／主體鎖定（Image/Reference-to-Video, I2V / R2V）
- **Prompt 策略**：首幀提供靜態視覺錨點，提示詞專注描述「攝影機動態」與「主體演變」。
- **角色聖經（Character Bible）**：跨鏡頭提示詞必須逐字保留人物特徵錨點（年齡、膚質、髮型、瞳色、服裝剪裁與固定配飾）。

#### 範式 C：首尾雙影格內插（First-to-Last Frame Interpolation）
- 傳入起始幀與結束幀，提示詞描述中間 4～8 秒的過渡動態（如光影位移、形體運動、視角旋轉），維持運動流暢度。

---

### 第三階段：原生音訊 2.0 與光影電影感強化（Audio & Cinematic Polish）

1. **原生音訊規範（Native Audio Guidance）**：
   - **對話格式**：使用 `角色名稱: "台詞內容"` 或 `角色名稱 says: "台詞內容"`，並明確標註 `(no subtitles)` 避免畫面嵌入雜訊字幕。
   - **音效標籤**：明確列出關鍵 SFX（如金屬碰撞、腳步聲、雨滴落水聲）與時間點節奏。
   - **環境音景**：描述背景氛圍底噪（如遠處車流、空調低頻運轉、樹林風聲）。

2. **電影感詞彙校準（Cinematic Directives）**：
   - 禁用主觀抽象詞（如「美麗」、「高品質」、「震撼」），一律替換為具體光學與電影參數（如「35mm anamorphic lens」、「Rembrandt lighting」、「subtle volumetric mist」、「shallow depth of field f/1.8」）。

---

### 第四階段：品質守門與負面提示詞配置（QA & Negative Prompts）

1. **字數與複雜度控制**：提示詞本體長度控制在 120～220 英文單詞，確保語意重心集中。
2. **標準負面提示詞（Negative Prompt Baseline）**：
   `blurry, low contrast, oversaturated, deformed fingers, extra limbs, bad anatomy, mutated hands, flickering artifacts, watermark, on-screen text, subtitles, glitchy motion`
3. **動態衝突防範**：禁止同時下達矛盾指令（例如「fast zoom」與「ultra slow motion」同時存在）。

---

### 第五階段：標準化輸出與雙格式交付（Standardized Output）

每次產出必須同時提供 **自然語言導演提示詞（Natural Prompt）** 與 **結構化 JSON 規格（JSON Schema）**，並附帶技術指標評估：

```json
{
  "project_metadata": {
    "target_model": "Google Veo 3.1",
    "duration_seconds": 8,
    "resolution": "1080p",
    "aspect_ratio": "16:9",
    "workflow_mode": "T2V"
  },
  "prompt_text": "[完整的五段式英文提示詞]",
  "audio_guidance": {
    "dialogue": "[對白與語調指示]",
    "sfx": "[關鍵動作音效]",
    "ambient": "[環境音景描述]"
  },
  "negative_prompt": "[排除之畫面缺陷與雜訊標籤]",
  "quality_metrics": {
    "semantic_coherence": "A+",
    "physics_realism": "High",
    "cinematic_fidelity": "1080p Film Grade"
  }
}
```

---

## 常見陷阱與排錯方針（Gotchas & Troubleshooting）

- **字幕誤出**：嚴禁在對白外使用雙引號或括號，一律在提示詞結尾加上 `(no subtitles, no text on screen)`。
- **角色漂移**：純文字生成難以完全鎖定臉部時，應主動建議使用者切換至 R2V / I2V 模式，以單一基準圖作為首幀輸入。
- **動作失真／形體崩解**：單鏡頭不可塞入超過 2 個主要動態，請將動作拆解為「先 A 動作，停頓一拍，再執行 B 動作」之時序指令。
- **延伸鏡頭音訊斷點**：長敘事多鏡頭應採「獨立分段生成 8 秒滿載音訊」，後續在剪輯階段進行多軌混音對齊。

## 標準執行契約

### 觸發與輸入

使用者明確要求「veo-short-video-prompt-engineer」的核心任務，或輸入與本技能描述高度相符時才啟用。先確認目標、受眾、上下文、資料來源、授權、限制條件與希望的輸出格式；未提供的資訊不得自行補成事實。

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
- 涉及外部資料時記錄來源、擷取時間與查證限制；將可觀察事實、推論與建議分開呈現。

- 不得用於未授權存取、憑證收集、冒充他人、垃圾訊息、操縱或規避平台政策。
- 不得把未經授權的第三方內容、個資或機密資料重新發布到公開服務。

## 停止條件

若使用授權、資料來源、範圍、關鍵數字、身份或外部操作權限無法確認，立即停止高影響部分並回報缺口。若發現來源互相矛盾、任務目標漂移、敏感資料暴露、輸出無法驗證或操作不可恢復，保留已完成的安全分析，暫停後續動作並要求人工判斷。

## 關聯技能

本技能與 `video-editing-preproduction-script-cuts` 有功能相近或可互補的技能；選擇時以使用者明確需求、資料來源與權限邊界為準，不要平行重複執行相同的高影響操作。

## 來源追蹤

此技能由 `docs/sources/skills_export_20260818.zip` 內的 `veo-short-video-prompt-engineer/SKILL.md` 正規化而來，來源項目 SHA-256 為 `cb6dda0a832c140323c5548fe934533ac91125ba64f9d9332b1bdce50a6a095d`，原始行號範圍為 1–106。原始附件已保存於 repository 的 `docs/sources/`，並補上輸入、輸出、權限、安全、人工核准與停止契約。
