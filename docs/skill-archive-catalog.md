# 附件 Skills 整併目錄

> 本目錄由 `scripts/import_skill_archive.py` 產生。它將 `Skills_Full_Configurations_Backup_20260818.md` 的 66 項技能逐一正規化為 `custom_skills/<id>/SKILL.md` 與 `manifest.json`，並補上輸入、輸出、權限、安全、人工核准與停止契約。

## 整併原則

所有匯入技能均採 `instruction_only` runtime，預設以分析、草稿或唯讀方式運作。附件中的原始內容保留為技能核心流程，但補上不可捏造、資料最小化、來源追蹤、外部寫入人工核准與停止條件。涉及相近能力的技能不覆蓋既有實作，而是以獨立 ID 納管並在 manifest 中標示關聯，避免破壞既有相容性。

| # | ID | 類別 | 描述 | 風險 | 網路能力 | 關聯既有技能 |
|---:|---|---|---|---|:---:|---|
| 1 | `agent-task-packaging` | 一、 AI Agent 架構、治理與自動化 | Agent 任務封包 Skill｜把模糊需求變成可委派可驗收的任務，含 Outcome、Criteria 與 Stop Rules。 | low | 否 | — |
| 2 | `ai-agent-task-delegation-framework` | 一、 AI Agent 架構、治理與自動化 | AI Agent 任務委派總則（雷小蒙模式），將重複任務交給 Agent 跑，人只下指令與驗收（<2 小時）。 | low | 否 | — |
| 3 | `ai-security-agent-governance` | 一、 AI Agent 架構、治理與自動化 | AI 資安與 Agent 治理 Skill，檢查 AI Agent、自動化流程與企業平台的身份、權限、Shadow AI、資料外洩與煞車系統。 | high | 是 | — |
| 4 | `ai-virtual-board-supervisor-agent` | 一、 AI Agent 架構、治理與自動化 | AI 虛擬董事會 Supervisor Agent Skill，調度 CFO、CHRO、COO、CPRO、CSO，彙整跨職能建議並保留人工決策節點。 | high | 否 | — |
| 5 | `dual-agent-human-sop` | 一、 AI Agent 架構、治理與自動化 | 雙 Agent 協作 Human 操作 SOP｜Hermes × OpenClaw × Obsidian，建立任務卡、審核報告與沉澱流程。 | high | 是 | — |
| 6 | `enterprise-sovereign-ai-adoption` | 一、 AI Agent 架構、治理與自動化 | 企業主權 AI 平台導入 Skill，評估 AI 任務應採雲端、受控或私有部署，設計資料、權限、稽核與 MVP 路線圖。 | high | 否 | — |
| 7 | `mimo-hermes-openclaw-diagnosis` | 一、 AI Agent 架構、治理與自動化 | 協助設定與排錯 Xiaomi MiMo、Hermes Agent、OpenClaw 的模型連線，確認 API Key 類型、Base URL、provider 名稱與模型名稱。 | high | 是 | — |
| 8 | `openclaw-agent-handbook` | 一、 AI Agent 架構、治理與自動化 | OpenClaw Agent 專屬手冊，做為穩定執行者依照 Hermes Plan 完成任務、記錄結果、回報差異與提出 Skill 候選。 | high | 是 | — |
| 9 | `opus-5-skill-calibration-standards` | 一、 AI Agent 架構、治理與自動化 | Opus 5 世代 Skill 校準準則，作為整座 Skill 庫全面體檢、減法優化與約束補強的標準。 | high | 是 | — |
| 10 | `warp-ai-multi-agent` | 一、 AI Agent 架構、治理與自動化 | Warp AI Multi-Agent War Room Launch Configuration. Use when the user asks to configure Warp terminal launch configurations, set up multi-pane CLI agent layouts, or troubleshoot Warp terminal AI agent workflows. | high | 是 | — |
| 11 | `ai-project-feasibility-assessment` | 二、 商業策略、創業與定價 | AI 專案落地評估 Skill，用商業價值與八維度框架評估 AI 專案是否值得導入、如何設計 MVP 與驗收指標。 | low | 否 | — |
| 12 | `business-efficiency-scaling-strategy` | 二、 商業策略、創業與定價 | 商業效率與規模化做局 Skill，用 3S（系統化、持續性、規模化）與剛需象限診斷生意並設計做局策略。 | low | 否 | — |
| 13 | `business-model-canvas-diagnosis` | 二、 商業策略、創業與定價 | 商業模式九宮格診斷 Skill，用九宮格診斷價值主張、客群、通路、活動、資源、成本與收益並找出斷點。 | high | 否 | `analyzing-business-models` |
| 14 | `client-filtering-brand-positioning` | 二、 商業策略、創業與定價 | 客戶篩選與品牌定位 Skill，依市場規模、品牌定位與期待管理判斷該服務誰、不服務誰與如何有限客製化。 | high | 否 | — |
| 15 | `moosie-ai-startup-brand-assets` | 二、 商業策略、創業與定價 | Moosie Education AI 新創申請與品牌資產整理，包含英文官網、LinkedIn、Pitch deck 與對外品牌敘事。 | medium | 是 | — |
| 16 | `moosie-niche-demolisher` | 二、 商業策略、創業與定價 | 【Research Skill】Moosie｜Category-of-One Niche Demolisher，找出高需求、低競爭的 Instagram 補教品牌子定位。 | high | 是 | — |
| 17 | `mvp-validation-iteration` | 二、 商業策略、創業與定價 | 產品 MVP 驗證與迭代 Skill，用需求四象限、MVP、假廣告、預購、用戶訪談與放棄率分析驗證產品。 | medium | 否 | — |
| 18 | `pricing-strategy-conversion-system` | 二、 商業策略、創業與定價 | 定價策略與成交系統 Skill，設計價格、報價情境、成交流程與回購系統。 | medium | 否 | `designing-pricing-systems` |
| 19 | `startup-cashflow-pnl-planning` | 二、 商業策略、創業與定價 | 創業現金流與損益表規劃 Skill，建立個人、副業與創業損益表，拆解業績目標、情境與悲觀現金流底線。 | high | 否 | — |
| 20 | `startup-venture-builder` | 二、 商業策略、創業與定價 | Startup Venture Builder for opportunity discovery, market validation, MVP roadmap, business modeling, sales system, and investor stress testing. Use when the user asks for startup idea validation, business model design, MVP roadmap, landing page copy, or startup stress testing. | medium | 否 | — |
| 21 | `ai-content-monetization-side-hustle` | 三、 行銷、品牌、公關與溝通 | AI 自媒體斜槓變現 Skill，用 AI 完成市場研究、個人定位、內容轉化、產品階梯與自動化成交設計。 | high | 是 | — |
| 22 | `customer-service-email-routing` | 三、 行銷、品牌、公關與溝通 | 信件與客服分流回覆 Skill，收信分類、依知識庫產出草稿並進行風險分級與人審放行。 | high | 是 | — |
| 23 | `marketing-brief-competitor-analyst` | 三、 行銷、品牌、公關與溝通 | Analyze marketing briefs, research real-time market competitors, and deliver strategic brand messaging positioning recommendations. Use when the user asks to analyze marketing briefs, research competitors, or refine brand positioning. | medium | 是 | — |
| 24 | `negotiation-strategy-script` | 三、 行銷、品牌、公關與溝通 | 談判準備與出牌策略 Skill，用談判八問、議題組合、出牌策略、回應劇本與 BATNA 完成談判前準備。 | high | 否 | — |
| 25 | `parent-communication-trust-building` | 三、 行銷、品牌、公關與溝通 | 家長訊息回覆與信任建立 Skill（Moosie 老師版），產出四段結構（同理、具體觀察、做法、下一步）的 LINE 回覆草稿。 | high | 否 | — |
| 26 | `personal-brand-sponsorship` | 三、 行銷、品牌、公關與溝通 | 個人品牌與廠商合作 Skill，協助創作者建立個人品牌定位、內容策略、廠商邀約判斷、合約檢查與業配文案。 | high | 否 | — |
| 27 | `pr-brand-crisis-management` | 三、 行銷、品牌、公關與溝通 | 公關品牌與危機處理 Skill，設計公關策略、品牌核心訊息、PESO 媒體組合、利益關係人管理與危機處理 SOP。 | high | 否 | — |
| 28 | `article-to-social-content-pack` | 四、 社群經營、內容創作與文案 | 將長文、對話、影音逐字稿或核心主題，一鍵改寫並拆解為多平台社群內容切片大禮包。內容包含 1200 字深度長文（WHY-HOW-WHAT 金字塔架構）、10 個高點擊吸睛標題、IG 5-6 頁圖文卡片視覺與短影音腳本、Midjourney 英文 AI 繪圖提示詞，以及 Threads 5 則金句串文。支援自動匯出與同步至 Google Drive/Docs/Sheets。適用於使用者要求將文章轉為社群貼文、做多平台內容矩陣、產出 IG 圖文、Threads 串文、短影音腳本或匯出貼文檔案時。 | medium | 是 | — |
| 29 | `couple-podcast-hosting` | 四、 社群經營、內容創作與文案 | 夫妻對談 Podcast 主持流程 Skill，提供提問、追問與收尾腳本、三幕劇節奏與降溫技巧。 | low | 否 | — |
| 30 | `newsletter-topic-selection-writing` | 四、 社群經營、內容創作與文案 | 電子報選題與撰寫 Skill，每週固定選題、主文撰寫、標題/預覽文字、導流 CTA 與待審寄送流程。 | low | 否 | — |
| 31 | `precise-narrative-storytelling` | 四、 社群經營、內容創作與文案 | 精準敘事 Skill｜把真實經驗變成好故事，用衝突找亮點、4P 萃取故事 DNA、故事九宮格三幕劇展開。 | low | 否 | — |
| 32 | `social-content-batch-production` | 四、 社群經營、內容創作與文案 | 社群經營內容量產 Skill，從既有素材拆解產出一週社群貼文排程，包含平台改寫、標題鉤子與圖文建議。 | medium | 是 | — |
| 33 | `social-data-retrospective-private-domain` | 四、 社群經營、內容創作與文案 | 社群數據覆盤與私域經營 Skill，建立社群內容週期、IG/FB 數據覆盤、電子報與公域轉私域導流。 | high | 否 | — |
| 34 | `speak-human-tw` | 四、 社群經營、內容創作與文案 | 「說人話」繁體中文去 AI 味改寫技能。識別 AI 寫作痕跡，校正中國用語與半形標點，提升自然度與台灣繁體語感。 | low | 否 | — |
| 35 | `threads-viral-consultant` | 四、 社群經營、內容創作與文案 | Threads content strategy and conversion consultant. Use when the user asks to create Threads posts, optimize Threads profile bio, design Threads content funnel, analyze viral Threads posts, or build Threads DM conversion scripts. | medium | 是 | — |
| 36 | `video-editing-preproduction-script-cuts` | 四、 社群經營、內容創作與文案 | 影片剪輯前製與腳本切點 Skill，從帶時間碼逐字稿產出保留/刪除區段、章節、標題與短影音選段。 | high | 否 | — |
| 37 | `website-landing-page-builder` | 四、 社群經營、內容創作與文案 | 網站／落地頁建置 Skill，用 Agent 直接產出可上線的互動式單頁（敘事、版面、前後對照、成本試算、CTA）。 | high | 否 | — |
| 38 | `youtube-learning-summary-exporter` | 四、 社群經營、內容創作與文案 | 批量抓取指定 YouTube 頻道最新影片逐字稿，轉換為結構化速讀摘要、問答解析與行動建議，並自動匯出至 Google Drive 資料夾。當使用者要求整理 YT 頻道最新影片、製作影片學習筆記、產出逐字稿精華或匯出自學筆記至 Drive 時使用。 | high | 是 | — |
| 39 | `checklist-manifesto-agent` | 五、 決策思維、心智模型與領導 | 清單革命 Agent Skill，依據《清單革命》與 Boorman 六原則，協助使用者設計、使用與診斷 5-9 項 Checklist。 | low | 是 | — |
| 40 | `decision-consulting-matrix` | 五、 決策思維、心智模型與領導 | 決策諮詢 Skill（顧問級提問與方案比較），把重大選擇拆成方案矩陣：條件釐清、成本效益、風險、逆轉成本與建議。 | medium | 否 | — |
| 41 | `decision-making-superpowers` | 五、 決策思維、心智模型與領導 | obra/superpowers 決策類 skill，協助把模糊問題、選項與權衡條件整理成可判斷、可比較、可執行的決策流程。 | medium | 否 | `making-decisions` |
| 42 | `minerva-82-hcs-daily-coach` | 五、 決策思維、心智模型與領導 | Minerva 82 HCs 每日教練 Agent Skill，將 Minerva 82 HCs 心智習慣轉成每日學習、練習、應用與反思。 | low | 否 | — |
| 43 | `problem-reframing-constraints` | 五、 決策思維、心智模型與領導 | 問對問題與限制條件 Skill，透過現況分析、目標設定、障礙與限制條件，把模糊困境拆成可處理的核心問題。 | low | 否 | — |
| 44 | `questioning-leadership-dialogue` | 五、 決策思維、心智模型與領導 | 提問式領導 Skill｜用好問題帶人、溝通與對話，以好奇心為核心，用 5WH 與 ALAR 四步驟引導對話。 | low | 否 | — |
| 45 | `rumor-buster` | 五、 決策思維、心智模型與領導 | 根據 Allport & Postman 謠言心理學框架，系統性分析謠言與未經證實訊息的形成背景、傳播動機、失真機制（平化、銳化、同化），並產出結構化查證與破解應對策略。適用於假新聞、網路謠言、陰謀論分析與危機溝通。 | high | 是 | — |
| 46 | `ai-research-lab` | 六、 教學研究、學習與知識庫 | research-lab AI 研究實驗室 Skill v3.1，將複雜主題拆成可驗證、可收斂、可決策的研究流程。 | medium | 是 | `research-lab` |
| 47 | `course-outline-source-enricher` | 六、 教學研究、學習與知識庫 | Extract, verify, and format URLs and web references within course outlines, appending them into structured source lists. Use when the user asks to add web references, sources, or links to a course syllabus or outline. | low | 否 | — |
| 48 | `pdf-study-guide-generator` | 六、 教學研究、學習與知識庫 | Transform class notes into a comprehensive structured study guide, generate 5 practice questions, and compile them into a PDF. Use when the user asks to summarize notes into a PDF study guide with practice questions. | medium | 是 | — |
| 49 | `progressive-quiz-generator` | 六、 教學研究、學習與知識庫 | Generate 5 quizzes with progressive difficulty and distinct sub-topics based on user reference data. Use when the user asks to create progressive tests, multi-level quizzes, or topic-focused assessments from study materials. | low | 否 | — |
| 50 | `research-to-insight` | 六、 教學研究、學習與知識庫 | Research-to-Insight 多來源研究轉洞察技能包，把文章、PDF、網頁、簡報等轉成 10 種結構化成果。 | medium | 是 | — |
| 51 | `single-source-of-truth-knowledgebase` | 六、 教學研究、學習與知識庫 | 知識庫建置與單一真相源 Skill，將散落資訊收斂成可被 Agent 取用的單一真相源（Single Source of Truth）。 | medium | 是 | — |
| 52 | `notion-ai-workflow-design` | 七、 專案管理、流程與日常運營 | 協助判斷工作流程應沉澱成文件、Skill、資料庫自動化、N8N 或 AI Agent，並設計 Notion AI 工作流。 | high | 是 | — |
| 53 | `notion-smart-doc-role-adapter` | 七、 專案管理、流程與日常運營 | 智能文件角色適應器，根據 Notion 文件類型、內容成熟度與意圖，切換編輯、顧問、SOP 設計師等角色。 | medium | 是 | `adapting-notion-docs` |
| 54 | `product-launch-gate-checklist` | 七、 專案管理、流程與日常運營 | 產品上線關卡檢查 Skill｜八階段 Exit Criteria，核對 Phase 0-7 上線關卡條件，判定 Go/No-Go。 | high | 否 | — |
| 55 | `routine-task-report-aggregation` | 七、 專案管理、流程與日常運營 | 雜事處理與報表彙整 Skill，定時抓取各平台數據、彙整成週報／月報，並把散落待辦收斂進單一任務庫。 | low | 是 | — |
| 56 | `design-proposal-portfolio-persuasion` | 八、 設計與視覺提案 | 設計提案與作品集說服力 Skill，將設計專案整理成有脈絡的提案與作品集，並用十個設計心法檢查品質。 | high | 是 | — |
| 57 | `logotype-design-logic-practice` | 八、 設計與視覺提案 | 標準字設計：從生活創意到邏輯實踐，拆成識別性、造型性、系統性三原則，提供 Brief、檢核表與規範。 | medium | 是 | — |
| 58 | `presentation-structure-visual-script` | 八、 設計與視覺提案 | 簡報製作 Skill（結構→視覺→講稿），先定敘事骨架與每頁一個訊息，再產出版面與講稿備忘。 | low | 否 | — |
| 59 | `500dishes-restaurant-info-enrichment` | 九、 數據分析、財務與垂直領域 | 500盤餐廳對外資訊補齊 Skill，針對得獎餐廳補齊 Google Maps、官方社群、官網狀態與網站開發潛力。 | medium | 是 | — |
| 60 | `merchant-info-verification` | 九、 數據分析、財務與垂直領域 | 店家官網與社群資料查核 Skill，批次查核店家官網、地址、Google Maps 與官方 Instagram 等公開資料。 | medium | 是 | — |
| 61 | `product-revenue-growth-tracker` | 九、 數據分析、財務與垂直領域 | Calculate revenue growth rates across product lines, build dynamic spreadsheets, and generate trend charts. Use when the user asks to compute revenue growth rates or plot product line revenue trends. | medium | 是 | — |
| 62 | `real-estate-market-modeler` | 九、 數據分析、財務與垂直領域 | Analyze real estate transactions, research local market trends and forecasts, and build a financial valuation/modeling Google Sheet. Use when the user asks to evaluate real estate deals, research nearby property trends, or build real estate valuation spreadsheets. | medium | 是 | — |
| 63 | `reconcile` | 九、 數據分析、財務與垂直領域 | 處理財務、帳務或資料對帳（Reconciliation）的技能，協助核對資料差異、產出對帳報告與差異分析。 | high | 是 | — |
| 64 | `renovation-expense-tracker` | 九、 數據分析、財務與垂直領域 | Process renovation receipts, categorize contractor engineering items and costs, and generate an expense tracking Google Sheet. Use when the user asks to organize renovation receipts or build a renovation project cost tracking spreadsheet. | medium | 是 | — |
| 65 | `gemini-spark-instructions` | 十、 核心設定與個人指令 | User instructions and operational guidelines for Gemini Spark based on onboarding personal research. | low | 是 | — |
| 66 | `user-instructions` | 十、 核心設定與個人指令 | Personalized instructions and context for Gemini Spark to work with Guan Hong Chen (陳冠宏), integrating domain-specific user skills and Full-Sprint AI Research methodology for automated workflow execution. | high | 是 | — |
