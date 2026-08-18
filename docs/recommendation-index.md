# Skills 推薦索引與排序

> 本索引依 GitHub `main` 的 `fead9bd` commit 產生，資料來源為 `docs/evaluations/github-skills-test-results.json`。它是技能選擇的治理與安全輔助，不是專業品質、成功率或投資報酬率保證。

## 使用方式

優先依排名與分級選擇候選 skill，再閱讀該 skill 的 `SKILL.md` 與 `manifest.json`。如果任務涉及外部服務、帳戶、個資、部署、付費、發送、發佈、刪除或其他高影響行為，必須以 manifest 的人工核准點、停止條件與 rollback 規則為準，不得只依賴排名直接執行。

## 排名方法

| 分級 | 數量 | 判定 |
|---|---:|---|
| A｜優先推薦 | 21 | 測試通過、low risk、無 connector、無外部寫入。 |
| A-｜條件優先推薦 | 30 | 測試通過、通常無外部寫入，但為 medium risk；需人工覆核。 |
| B｜條件推薦 | 57 | 測試通過但有 high risk、connector 或外部寫入邊界。 |
| C｜暫不推薦 | 0 | 測試失敗或無法安全驗證；本次為 0。 |

| 維度 | 統計 |
|---|---:|
| 技能總數 | 108 |
| 測試通過 | 108/108 |
| 風險分布 | low 23；medium 34；high 51 |
| 外部操作 | 0 次；所有 instruction-only 技能只做唯讀 dry-run |

## 完整排名

| 排名 | Skill ID | 名稱 | Runtime | Risk | 分數 | 分級 | 測試範圍 | Connector | 外部寫入 | 狀態 |
|---:|---|---|---|---|---:|---|---|---:|---|---|
| 1 | `agent-big-e-life-coach` | agent-big-e-life-coach | `instruction_only` | low | 100.00 | A｜優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Provide life coaching, emotional regulation, spiritual gamification, and podcast script creation in the persona of Podcast Host Big E (大E). Use when the user asks for Big E life coaching, podcast episode scripts, emotional management guides, or reflective growth notes.
| 2 | `agent-task-packaging` | Agent Task Packaging | `instruction_only` | low | 100.00 | A｜優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Agent 任務封包 Skill｜把模糊需求變成可委派可驗收的任務，含 Outcome、Criteria 與 Stop Rules。
| 3 | `ai-agent-task-delegation-framework` | Ai Agent Task Delegation Framework | `instruction_only` | low | 100.00 | A｜優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：AI Agent 任務委派總則（雷小蒙模式），將重複任務交給 Agent 跑，人只下指令與驗收（<2 小時）。
| 4 | `ai-project-feasibility-assessment` | ai-project-feasibility-assessment\ | `instruction_only` | low | 100.00 | A｜優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：AI 專案落地評估 Skill，用商業價值與八維度框架評估 AI 專案是否值得導入、如何設計 MVP 與驗收指標。
| 5 | `business-efficiency-scaling-strategy` | Business Efficiency Scaling Strategy | `instruction_only` | low | 100.00 | A｜優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：商業效率與規模化做局 Skill，用 3S（系統化、持續性、規模化）與剛需象限診斷生意並設計做局策略。
| 6 | `checklist-manifesto-agent` | Checklist Manifesto Agent | `instruction_only` | low | 100.00 | A｜優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：清單革命 Agent Skill，依據《清單革命》與 Boorman 六原則，協助使用者設計、使用與診斷 5-9 項 Checklist。
| 7 | `couple-podcast-hosting` | Couple Podcast Hosting | `instruction_only` | low | 100.00 | A｜優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：夫妻對談 Podcast 主持流程 Skill，提供提問、追問與收尾腳本、三幕劇節奏與降溫技巧。
| 8 | `course-outline-source-enricher` | Course Outline Source Enricher | `instruction_only` | low | 100.00 | A｜優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Extract, verify, and format URLs and web references within course outlines, appending them into structured source lists. Use when the user asks to add web references, sources, or links to a course syllabus or outline.
| 9 | `gemini-spark-instructions` | Gemini Spark Instructions | `instruction_only` | low | 100.00 | A｜優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：User instructions and operational guidelines for Gemini Spark based on onboarding personal research.
| 10 | `making-decisions` | Making Decisions | `instruction_only` | low | 100.00 | A｜優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Structure ambiguous choices into clear decision statements, comparable options, weighted evaluation criteria, uncertainty maps, recommendations, counterarguments, and low-cost validation experiments.
| 11 | `minerva-82-hcs-daily-coach` | Minerva 82 Hcs Daily Coach | `instruction_only` | low | 100.00 | A｜優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Minerva 82 HCs 每日教練 Agent Skill，將 Minerva 82 HCs 心智習慣轉成每日學習、練習、應用與反思。
| 12 | `newsletter-topic-selection-writing` | Newsletter Topic Selection Writing | `instruction_only` | low | 100.00 | A｜優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：電子報選題與撰寫 Skill，每週固定選題、主文撰寫、標題/預覽文字、導流 CTA 與待審寄送流程。
| 13 | `precise-narrative-storytelling` | Precise Narrative Storytelling | `instruction_only` | low | 100.00 | A｜優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：精準敘事 Skill｜把真實經驗變成好故事，用衝突找亮點、4P 萃取故事 DNA、故事九宮格三幕劇展開。
| 14 | `presentation-structure-visual-script` | Presentation Structure Visual Script | `instruction_only` | low | 100.00 | A｜優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：簡報製作 Skill（結構→視覺→講稿），先定敘事骨架與每頁一個訊息，再產出版面與講稿備忘。
| 15 | `presentation-yaml-design-architect` | presentation-yaml-design-architect | `instruction_only` | low | 100.00 | A｜優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Transform presentation topics or draft text into a structured presentation design blueprint in YAML format (PRESENTATION_DESIGN.yaml) specifying global design specs, color schemes, layout rules, page-by-page visual descriptions, and content generation prompts. Use when the user asks to generate presentation design blueprints, YAML slide architectures, or structured presentation visual specs.
| 16 | `problem-reframing-constraints` | Problem Reframing Constraints | `instruction_only` | low | 100.00 | A｜優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：問對問題與限制條件 Skill，透過現況分析、目標設定、障礙與限制條件，把模糊困境拆成可處理的核心問題。
| 17 | `progressive-quiz-generator` | Progressive Quiz Generator | `instruction_only` | low | 100.00 | A｜優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Generate 5 quizzes with progressive difficulty and distinct sub-topics based on user reference data. Use when the user asks to create progressive tests, multi-level quizzes, or topic-focused assessments from study materials.
| 18 | `questioning-leadership-dialogue` | Questioning Leadership Dialogue | `instruction_only` | low | 100.00 | A｜優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：提問式領導 Skill｜用好問題帶人、溝通與對話，以好奇心為核心，用 5WH 與 ALAR 四步驟引導對話。
| 19 | `speak-human-tw` | Speak Human Tw | `instruction_only` | low | 100.00 | A｜優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：「說人話」繁體中文去 AI 味改寫技能。識別 AI 寫作痕跡，校正中國用語與半形標點，提升自然度與台灣繁體語感。
| 20 | `to_prd` | To PRD | `instruction_only` | low | 100.00 | A｜優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Turn conversation and codebase context into a structured PRD in Markdown.
| 21 | `write_a_skill` | Write a Skill | `instruction_only` | low | 100.00 | A｜優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Create a new agent skill with structure, trigger guidance, and supporting resources.
| 22 | `adapting-notion-docs` | 智能文件角色適應器 | `instruction_only` | low | 98.00 | B｜條件推薦 | contract_and_read_only_dry_run | 1 | False | PASS |
  描述：Adapt to Notion document type, content maturity, and user intent, then switch into the most useful assistant role to summarize, restructure, rewrite, fill gaps, critique, convert formats, or produce action-ready documentation.
| 23 | `routine-task-report-aggregation` | Routine Task Report Aggregation | `instruction_only` | low | 95.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | True | PASS |
  描述：雜事處理與報表彙整 Skill，定時抓取各平台數據、彙整成週報／月報，並把散落待辦收斂進單一任務庫。
| 24 | `500dishes-restaurant-info-enrichment` | 500Dishes Restaurant Info Enrichment | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：500盤餐廳對外資訊補齊 Skill，針對得獎餐廳補齊 Google Maps、官方社群、官網狀態與網站開發潛力。
| 25 | `agent-bible-sq3r-fast-guide` | agent-bible-sq3r-fast-guide | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Guide users through high-speed Bible reading using the SQ3R-Fast methodology (Survey, Question, Read, Recite, Review) and structured taxonomy tags (#god/attr,
| 26 | `ai-research-lab` | Ai Research Lab | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：research-lab AI 研究實驗室 Skill v3.1，將複雜主題拆成可驗證、可收斂、可決策的研究流程。
| 27 | `analyzing-business-models` | Analyzing Business Models | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Diagnose businesses, products, personal brands, services, courses, consulting offers, and projects with the Business Model Canvas to evaluate sustainability, weak links, and North Star metrics tied to revenue.
| 28 | `article-to-social-content-pack` | Article To Social Content Pack | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：將長文、對話、影音逐字稿或核心主題，一鍵改寫並拆解為多平台社群內容切片大禮包。內容包含 1200 字深度長文（WHY-HOW-WHAT 金字塔架構）、10 個高點擊吸睛標題、IG 5-6 頁圖文卡片視覺與短影音腳本、Midjourney 英文 AI 繪圖提示詞，以及 Threads 5 則金句串文。支援自動匯出與同步至 Google Drive/Docs/Sheets。適用於使用者要求將文章轉為社群貼文、做多平台內容矩陣、產出 IG 圖文、Threads 串文、短影音腳本或匯出貼文檔案時。
| 29 | `daily-devotional-prayer-guide` | daily-devotional-prayer-guide | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Guide users through a structured 4-phase daily spiritual devotional and prayer workflow (preparation, SOAP meditation, deep reflection questions, and responsive prayer). Use when the user asks for daily devotional guidance, Bible verse meditation, SOAP reflection, or structured prayer prompts.
| 30 | `data_analysis` | Data Analysis Skill | `python` | medium | 92.00 | A-｜條件優先推薦 | offline_executable_smoke_test | 0 | False | PASS |
  描述：Analyze CSV or Excel files and generate privacy-conscious Markdown reports with redacted previews.
| 31 | `decision-consulting-matrix` | Decision Consulting Matrix | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：決策諮詢 Skill（顧問級提問與方案比較），把重大選擇拆成方案矩陣：條件釐清、成本效益、風險、逆轉成本與建議。
| 32 | `decision-making-superpowers` | Decision Making Superpowers | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：obra/superpowers 決策類 skill，協助把模糊問題、選項與權衡條件整理成可判斷、可比較、可執行的決策流程。
| 33 | `designing-pricing-systems` | Designing Pricing Systems | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Design pricing strategy, quotation logic, sales conversion flows, repurchase systems, CRM follow-up, discounts, trials, referrals, and social proof for products and services.
| 34 | `interactive-skill-learning-curriculum` | interactive-skill-learning-curriculum | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Research optimal learning methods for any target skill and design an interactive curriculum with videos, podcasts, reading materials, and checkable milestones. Use when the user asks to teach a skill, create a learning roadmap, or build an interactive course curriculum.
| 35 | `logotype-design-logic-practice` | Logotype Design Logic Practice | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：標準字設計：從生活創意到邏輯實踐，拆成識別性、造型性、系統性三原則，提供 Brief、檢核表與規範。
| 36 | `marketing-brief-competitor-analyst` | Marketing Brief Competitor Analyst | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Analyze marketing briefs, research real-time market competitors, and deliver strategic brand messaging positioning recommendations. Use when the user asks to analyze marketing briefs, research competitors, or refine brand positioning.
| 37 | `mcp_builder` | MCP Builder | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Guide MCP server setup, Warp integration, and validation steps for new tools or services.
| 38 | `merchant-info-verification` | Merchant Info Verification | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：店家官網與社群資料查核 Skill，批次查核店家官網、地址、Google Maps 與官方 Instagram 等公開資料。
| 39 | `moosie-ai-startup-brand-assets` | Moosie Ai Startup Brand Assets | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Moosie Education AI 新創申請與品牌資產整理，包含英文官網、LinkedIn、Pitch deck 與對外品牌敘事。
| 40 | `multi-agent-research-workflow` | multi-agent-research-workflow | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：An advanced multi-agent research workflow inspired by Claude Research architecture, enhanced with Full Sprint engineering controls. Use when conducting deep multi-perspective research, executing parallel subagent investigation tasks, or synthesizing research into actionable software engineering sprint contracts.
| 41 | `mvp-validation-iteration` | Mvp Validation Iteration | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：產品 MVP 驗證與迭代 Skill，用需求四象限、MVP、假廣告、預購、用戶訪談與放棄率分析驗證產品。
| 42 | `pricing-strategy-conversion-system` | Pricing Strategy Conversion System | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：定價策略與成交系統 Skill，設計價格、報價情境、成交流程與回購系統。
| 43 | `product-idea-scoring-matrix` | product-idea-scoring-matrix | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Generate 100 product or SaaS ideas based on skills/interests and score each across market demand, execution difficulty, differentiation, startup cost, and time-to-first-revenue. Use when the user asks for 100 product ideas, SaaS ideation, or startup idea scoring matrix.
| 44 | `product-revenue-growth-tracker` | Product Revenue Growth Tracker | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Calculate revenue growth rates across product lines, build dynamic spreadsheets, and generate trend charts. Use when the user asks to compute revenue growth rates or plot product line revenue trends.
| 45 | `real-estate-market-modeler` | Real Estate Market Modeler | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Analyze real estate transactions, research local market trends and forecasts, and build a financial valuation/modeling Google Sheet. Use when the user asks to evaluate real estate deals, research nearby property trends, or build real estate valuation spreadsheets.
| 46 | `renovation-expense-tracker` | Renovation Expense Tracker | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Process renovation receipts, categorize contractor engineering items and costs, and generate an expense tracking Google Sheet. Use when the user asks to organize renovation receipts or build a renovation project cost tracking spreadsheet.
| 47 | `research-lab` | research-lab — AI 研究實驗室 | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Break complex research, investigation, market analysis, product analysis, competitor analysis, technical trend research, business model analysis, growth strategy, SEO/GEO, education, AI, or tutoring topics into verifiable breadth scans, depth dives, cross-validation, and decision-ready reports.
| 48 | `research-to-insight` | Research To Insight | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Research-to-Insight 多來源研究轉洞察技能包，把文章、PDF、網頁、簡報等轉成 10 種結構化成果。
| 49 | `single-source-of-truth-knowledgebase` | Single Source Of Truth Knowledgebase | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：知識庫建置與單一真相源 Skill，將散落資訊收斂成可被 Agent 取用的單一真相源（Single Source of Truth）。
| 50 | `social-content-batch-production` | Social Content Batch Production | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：社群經營內容量產 Skill，從既有素材拆解產出一週社群貼文排程，包含平台改寫、標題鉤子與圖文建議。
| 51 | `startup-venture-builder` | Startup Venture Builder | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Startup Venture Builder for opportunity discovery, market validation, MVP roadmap, business modeling, sales system, and investor stress testing. Use when the user asks for startup idea validation, business model design, MVP roadmap, landing page copy, or startup stress testing.
| 52 | `threads-viral-consultant` | Threads Viral Consultant | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Threads content strategy and conversion consultant. Use when the user asks to create Threads posts, optimize Threads profile bio, design Threads content funnel, analyze viral Threads posts, or build Threads DM conversion scripts.
| 53 | `veo-short-video-prompt-engineer` | veo-short-video-prompt-engineer | `instruction_only` | medium | 92.00 | A-｜條件優先推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Google Veo 3.1 電影級影音提示詞工程與生成式導演 Skill。支援 T2V、I2V/R2V 主體錨定、首尾插值、原生音訊 2.0、多鏡頭敘事與 JSON 工業級提示詞。適用於撰寫 Veo 3/3.1 提示詞、短影音腳本、分鏡指令、電影級運鏡與光影設定。
| 54 | `notion-smart-doc-role-adapter` | Notion Smart Doc Role Adapter | `instruction_only` | medium | 90.00 | B｜條件推薦 | contract_and_read_only_dry_run | 1 | False | PASS |
  描述：智能文件角色適應器，根據 Notion 文件類型、內容成熟度與意圖，切換編輯、顧問、SOP 設計師等角色。
| 55 | `website-custom-optimizer` | Website Custom Optimizer | `instruction_only` | medium | 90.00 | B｜條件推薦 | contract_and_read_only_dry_run | 1 | False | PASS |
  描述：Diagnose and optimize websites, landing pages, product pages, service pages, enrollment pages, internal portals, and knowledge bases for clarity, trust, SEO, UX, CRO, mobile experience, performance, accessibility, launch readiness, and execution planning.
| 56 | `youtube-transcript-summarizer` | youtube-transcript-summarizer | `instruction_only` | medium | 90.00 | B｜條件推薦 | contract_and_read_only_dry_run | 1 | False | PASS |
  描述：Summarize YouTube video transcripts into structured, easily readable notes with key points, Q&A format for interviews, action items, conclusions, and key quotes. Use when the user asks to summarize a YouTube video transcript, process transcript text into notes, or extract structured summaries from YouTube transcripts.
| 57 | `pdf-study-guide-generator` | Pdf Study Guide Generator | `instruction_only` | medium | 87.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | True | PASS |
  描述：Transform class notes into a comprehensive structured study guide, generate 5 practice questions, and compile them into a PDF. Use when the user asks to summarize notes into a PDF study guide with practice questions.
| 58 | `agent-cyber-bully-lecturer` | agent-cyber-bully-lecturer | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Provide cybersecurity education, threat analysis, and defense recommendations in the persona of 'Cyber Frenchie Principal' (法鬥校長), using humorous canine analogies and security verification hierarchies. Use when the user asks for cybersecurity advice, phishing prevention, OWASP vulnerabilities, or security sniff logs.
| 59 | `agent-senior-prd-architect-sophia` | agent-senior-prd-architect-sophia | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Draft comprehensive, rigorous Product Requirement Documents (PRD), Mermaid system logic flows, and QA/edge case checklists in the persona of Senior PRD Architect Sophia Lin (林婷婷). Use when the user asks to write PRDs, define product requirements, map system logic flows, or outline QA checklists for software features.
| 60 | `agent-skills-actions-auditor` | agent-skills-actions-auditor | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Audit agent skills and actions, identify optimization opportunities, fix syntax or parameter issues, and refine prompt instructions. Use when the user asks to audit Codex/agent skills, optimize agent actions, or refine skill instructions.
| 61 | `ai-content-monetization-side-hustle` | Ai Content Monetization Side Hustle | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：AI 自媒體斜槓變現 Skill，用 AI 完成市場研究、個人定位、內容轉化、產品階梯與自動化成交設計。
| 62 | `ai-security-agent-governance` | Ai Security Agent Governance | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：AI 資安與 Agent 治理 Skill，檢查 AI Agent、自動化流程與企業平台的身份、權限、Shadow AI、資料外洩與煞車系統。
| 63 | `ai-virtual-board-supervisor-agent` | Ai Virtual Board Supervisor Agent | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：AI 虛擬董事會 Supervisor Agent Skill，調度 CFO、CHRO、COO、CPRO、CSO，彙整跨職能建議並保留人工決策節點。
| 64 | `app-performance-benchmark-optimizer` | app-performance-benchmark-optimizer | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Establish app performance benchmarks, identify latency or memory bottlenecks, and execute measurable code optimizations with before/after reports. Use when the user asks to optimize app performance, profile latency, or fix performance bottlenecks.
| 65 | `business-model-canvas-diagnosis` | Business Model Canvas Diagnosis | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：商業模式九宮格診斷 Skill，用九宮格診斷價值主張、客群、通路、活動、資源、成本與收益並找出斷點。
| 66 | `client-filtering-brand-positioning` | Client Filtering Brand Positioning | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：客戶篩選與品牌定位 Skill，依市場規模、品牌定位與期待管理判斷該服務誰、不服務誰與如何有限客製化。
| 67 | `customer-service-email-routing` | Customer Service Email Routing | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：信件與客服分流回覆 Skill，收信分類、依知識庫產出草稿並進行風險分級與人審放行。
| 68 | `design-proposal-portfolio-persuasion` | Design Proposal Portfolio Persuasion | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：設計提案與作品集說服力 Skill，將設計專案整理成有脈絡的提案與作品集，並用十個設計心法檢查品質。
| 69 | `emil-design-eng` | emil-design-eng | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make software feel great. Use when designing, building, or reviewing UI components, animations, transitions, or web interfaces.
| 70 | `enterprise-sovereign-ai-adoption` | Enterprise Sovereign Ai Adoption | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：企業主權 AI 平台導入 Skill，評估 AI 任務應採雲端、受控或私有部署，設計資料、權限、稽核與 MVP 路線圖。
| 71 | `full-sprint-execution` | full-sprint-execution | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：軟體工程 Full Sprint 安全執行與交付 Skill。當使用者需要在限制範疇、測試保護與 Sprint 契約下進行多檔案開發或重構時使用。
| 72 | `game-inspiration-world-builder` | game-inspiration-world-builder | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Generate 3D world inspiration concepts and autonomously build matching game code and assets. Use when the user asks to generate 3D world concepts, design game worlds, or build a game matching visual inspiration images.
| 73 | `high-energy-daily-routine-designer` | high-energy-daily-routine-designer | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Audit personal lifestyle and design an optimized daily routine for high energy covering sleep, nutrition, exercise, social, creative, and career growth. Use when the user asks for life audit, daily routine design, or energy optimization plan.
| 74 | `life-scenario-simulation-matrix` | life-scenario-simulation-matrix | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Conduct a 50-question life audit and simulate 30-year life trajectories across career, health, exercise, and relationship variables into structured matrices. Use when the user asks for a 50-question life survey or 30-year life scenario simulation.
| 75 | `lovable_github_cloudflare_worker` | Lovable GitHub Cloudflare Worker | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Stabilize a Lovable-generated project into a GitHub-managed and Cloudflare Worker-ready delivery pipeline.
| 76 | `managing-public-relations` | Managing Public Relations | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Build public relations strategy, brand messaging, stakeholder communication, PESO media strategy, media interview preparation, and crisis response plans.
| 77 | `mimo-hermes-openclaw-diagnosis` | Mimo Hermes Openclaw Diagnosis | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：協助設定與排錯 Xiaomi MiMo、Hermes Agent、OpenClaw 的模型連線，確認 API Key 類型、Base URL、provider 名稱與模型名稱。
| 78 | `moosie-niche-demolisher` | Moosie Niche Demolisher | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：【Research Skill】Moosie｜Category-of-One Niche Demolisher，找出高需求、低競爭的 Instagram 補教品牌子定位。
| 79 | `naval-backstage-simulator` | naval-backstage-simulator | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Simulate a multi-expert backstage debate synthesized through Naval Ravikant's mental models (leverage, specific knowledge, compounding, judgment) to produce concise, high-leverage, plain-text aphorisms and execution logic (ESSENCE_DISTILLATION.txt). Use when the user asks for Naval Ravikant style decision framework, multi-expert debate distillation, or plain-text high-leverage advice.
| 80 | `negotiation-strategy-script` | Negotiation Strategy Script | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：談判準備與出牌策略 Skill，用談判八問、議題組合、出牌策略、回應劇本與 BATNA 完成談判前準備。
| 81 | `open-slide` | open-slide | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Create, draft, edit, and manage web-native React presentations using the open-slide framework. Use when the user requests creating slides, building presentation decks with React/open-slide, editing slide components, or exporting open-slide presentations.
| 82 | `opus-5-skill-calibration-standards` | Opus 5 Skill Calibration Standards | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Opus 5 世代 Skill 校準準則，作為整座 Skill 庫全面體檢、減法優化與約束補強的標準。
| 83 | `parent-communication-trust-building` | Parent Communication Trust Building | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：家長訊息回覆與信任建立 Skill（Moosie 老師版），產出四段結構（同理、具體觀察、做法、下一步）的 LINE 回覆草稿。
| 84 | `personal-brand-sponsorship` | Personal Brand Sponsorship | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：個人品牌與廠商合作 Skill，協助創作者建立個人品牌定位、內容策略、廠商邀約判斷、合約檢查與業配文案。
| 85 | `pr-brand-crisis-management` | Pr Brand Crisis Management | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：公關品牌與危機處理 Skill，設計公關策略、品牌核心訊息、PESO 媒體組合、利益關係人管理與危機處理 SOP。
| 86 | `product-launch-gate-checklist` | Product Launch Gate Checklist | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：產品上線關卡檢查 Skill｜八階段 Exit Criteria，核對 Phase 0-7 上線關卡條件，判定 Go/No-Go。
| 87 | `reconcile` | Reconcile | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：處理財務、帳務或資料對帳（Reconciliation）的技能，協助核對資料差異、產出對帳報告與差異分析。
| 88 | `rumor-buster` | Rumor Buster | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：根據 Allport & Postman 謠言心理學框架，系統性分析謠言與未經證實訊息的形成背景、傳播動機、失真機制（平化、銳化、同化），並產出結構化查證與破解應對策略。適用於假新聞、網路謠言、陰謀論分析與危機溝通。
| 89 | `social-data-retrospective-private-domain` | Social Data Retrospective Private Domain | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：社群數據覆盤與私域經營 Skill，建立社群內容週期、IG/FB 數據覆盤、電子報與公域轉私域導流。
| 90 | `startup-cashflow-pnl-planning` | Startup Cashflow Pnl Planning | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：創業現金流與損益表規劃 Skill，建立個人、副業與創業損益表，拆解業績目標、情境與悲觀現金流底線。
| 91 | `system-file-audit-organizer` | system-file-audit-organizer | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Audit system files and directories, execute obvious file organization tasks, and generate user-confirmation proposals for major changes. Use when the user asks to audit computer files, clean up downloads/desktop, or organize system folders.
| 92 | `ui-minimalist-animation-enhancer` | ui-minimalist-animation-enhancer | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Refine web/app UI for minimalism, improve information hierarchy, and add fluid entrance and exit animations. Use when the user asks to improve UI, add entrance/exit animations, simplify layout, or make interface aesthetic and clean.
| 93 | `video-editing-preproduction-script-cuts` | Video Editing Preproduction Script Cuts | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：影片剪輯前製與腳本切點 Skill，從帶時間碼逐字稿產出保留/刪除區段、章節、標題與短影音選段。
| 94 | `warp-ai-multi-agent` | Warp Ai Multi Agent | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Warp AI Multi-Agent War Room Launch Configuration. Use when the user asks to configure Warp terminal launch configurations, set up multi-pane CLI agent layouts, or troubleshoot Warp terminal AI agent workflows.
| 95 | `website-auditing` | website-auditing | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：網站與 SEO 綜合稽核 Skill。當使用者需要對網站進行技術 SEO、載入速度、行動版體驗或內容品質稽核時使用。
| 96 | `weekly-podcast-script` | weekly-podcast-script | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Write, refine, and optimize weekly podcast scripts in the persona of Podcast Host Big E (大E) with natural Taiwanese spoken phrasing. Use when the user asks to generate a weekly podcast script, transform raw notes or transcripts into a podcast episode, or draft a weekly podcast script.
| 97 | `workspace-project-cleanup-agent` | workspace-project-cleanup-agent | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：Audit workspace projects, identify abandoned or duplicate work, and safely execute cleanup on git-tracked branches. Use when the user asks to clean up workspace, find abandoned or duplicate projects, or organize codebase projects.
| 98 | `youtube-learning-summary-exporter` | Youtube Learning Summary Exporter | `instruction_only` | high | 82.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | False | PASS |
  描述：批量抓取指定 YouTube 頻道最新影片逐字稿，轉換為結構化速讀摘要、問答解析與行動建議，並自動匯出至 Google Drive 資料夾。當使用者要求整理 YT 頻道最新影片、製作影片學習筆記、產出逐字稿精華或匯出自學筆記至 Drive 時使用。
| 99 | `cloudflare-skills` | cloudflare-skills | `instruction_only` | high | 80.00 | B｜條件推薦 | contract_and_read_only_dry_run | 1 | False | PASS |
  描述：Cloudflare 微服務、Workers/Pages 部署與 DNS 設定診斷 Skill。當使用者需要管理、部署或排錯 Cloudflare 服務與網域設定時使用。
| 100 | `google-ads-audit` | google-ads-audit | `instruction_only` | high | 80.00 | B｜條件推薦 | contract_and_read_only_dry_run | 1 | False | PASS |
  描述：Google Ads 廣告帳戶與成效審查/稽核 Skill。當使用者需要審查 Google Ads 帳戶架構、關鍵字策略、成效指標 (CPA/ROAS) 或優化廣告文案時使用。
| 101 | `notion-ai-workflow-design` | Notion Ai Workflow Design | `instruction_only` | high | 80.00 | B｜條件推薦 | contract_and_read_only_dry_run | 1 | False | PASS |
  描述：協助判斷工作流程應沉澱成文件、Skill、資料庫自動化、N8N 或 AI Agent，並設計 Notion AI 工作流。
| 102 | `optimizing-google-ads` | Google Ads AI Copilot | `instruction_only` | high | 80.00 | B｜條件推薦 | contract_and_read_only_dry_run | 1 | False | PASS |
  描述：Analyze Google Ads performance and produce read-only health reports, search term audits, negative keyword suggestions, RSA copy ideas, budget pacing, action queues, and n8n/Notion/MCP integration plans with human approval required before write or spend-impacting operations.
| 103 | `threads-api-skill` | threads-api-skill | `instruction_only` | high | 80.00 | B｜條件推薦 | contract_and_read_only_dry_run | 1 | False | PASS |
  描述：Comprehensive assistance with Meta's Threads API development for building applications that integrate with Meta's Threads social platform, including OAuth authentication, text/media/carousel posting, profile data retrieval, analytics insights, and webhook processing. Use when the user asks to integrate with Threads API, post to Threads, fetch Threads metrics, or set up Threads webhooks.
| 104 | `website-landing-page-builder` | Website Landing Page Builder | `instruction_only` | high | 80.00 | B｜條件推薦 | contract_and_read_only_dry_run | 1 | False | PASS |
  描述：網站／落地頁建置 Skill，用 Agent 直接產出可上線的互動式單頁（敘事、版面、前後對照、成本試算、CTA）。
| 105 | `dual-agent-human-sop` | Dual Agent Human Sop | `instruction_only` | high | 77.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | True | PASS |
  描述：雙 Agent 協作 Human 操作 SOP｜Hermes × OpenClaw × Obsidian，建立任務卡、審核報告與沉澱流程。
| 106 | `full-sprint` | Full Sprint | `instruction_only` | high | 77.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | True | PASS |
  描述：Turn a high-level goal into an executable, verifiable, pauseable, resumable, auditable sprint contract and continue PLAN → ACT → VERIFY → REVIEW → ITERATE within explicit safety, scope, validation, and budget limits.
| 107 | `openclaw-agent-handbook` | Openclaw Agent Handbook | `instruction_only` | high | 77.00 | B｜條件推薦 | contract_and_read_only_dry_run | 0 | True | PASS |
  描述：OpenClaw Agent 專屬手冊，做為穩定執行者依照 Hermes Plan 完成任務、記錄結果、回報差異與提出 Skill 候選。
| 108 | `user-instructions` | User Instructions | `instruction_only` | high | 75.00 | B｜條件推薦 | contract_and_read_only_dry_run | 1 | True | PASS |
  描述：Personalized instructions and context for Gemini Spark to work with Guan Hong Chen (陳冠宏), integrating domain-specific user skills and Full-Sprint AI Research methodology for automated workflow execution.

## 測試解讀限制

107 個 `instruction_only` skills 的通過結果代表封裝、manifest、標準段落、activation、來源與四類 eval 案例通過；它們沒有被擅自執行外部服務操作。唯一的 Python skill `data_analysis` 使用隔離 CSV fixture 完成離線 smoke test。真實 connector、部署、發送、付費與第三方寫入仍需另行取得人工批准與 integration test。

## 相關檔案

- [`skills.json`](../skills.json)：108 個完整 skills 依推薦排名排序；OpenAPI、MCP 與 workflow 輔助 entries 保留於排序區段之後，且不虛構測試分數。
- [`docs/evaluations/github-skills-test-results.json`](evaluations/github-skills-test-results.json)：逐一測試的機器可讀結果。
- [`docs/evaluations/github-skills-test-results.csv`](evaluations/github-skills-test-results.csv)：適合試算表與分析工具的平面結果。
- [`docs/manifest-contract.md`](manifest-contract.md)：manifest 欄位與權限資料流契約。

## References

[1]: https://github.com/emting/my-ai-skills GitHub repository：emting/my-ai-skills
[2]: https://github.com/emting/my-ai-skills/blob/main/evals/skills.json 技能契約 eval 案例
[3]: https://github.com/emting/my-ai-skills/blob/main/scripts/smoke_test_skills.py 安全 dry-run 工具
