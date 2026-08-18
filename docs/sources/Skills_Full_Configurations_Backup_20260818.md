# 完整自訂 Skills 設定手冊與備份檔 (Full Skills Configuration Archive)

> 本文件包含目前所有 66 項自訂 Skills 的完整設定、Prompt 指令架構、規範、使用時機與執行流程，方便離線備份、跨平台遷移或日後維護更新。  
> 

- **匯出時間**：2026-08-18  
- **Skills 總數**：66 項

---

# 一、 AI Agent 架構、治理與自動化

## 1\. `agent-task-packaging`

\---

name: agent-task-packaging

description: Agent 任務封包 Skill｜把模糊需求變成可委派可驗收的任務，含 Outcome、Criteria 與 Stop Rules。

\---

\# 定位

將模糊需求轉為可委派、可驗收的 Agent 任務封包。先判定適合度（ready/需補上下文/人判/不得委派），定義 Outcome、Context、Deliverables、Acceptance Criteria、Do not change 與 Stop rules。

\# 核心架構

  \- \*\*適合度標籤\*\*：🟢 Agent-ready、🟡 需補上下文、🔵 需人類判斷、🔴 不得委派。

  \- \*\*封包結構\*\*：Outcome、Context、Deliverables、Acceptance Criteria、Allowed scope、Do not change、Verification、Stop rules、Human gate。

---

## 2\. `ai-agent-task-delegation-framework`

\---

name: ai-agent-task-delegation-framework

description: AI Agent 任務委派總則（雷小蒙模式），將重複任務交給 Agent 跑，人只下指令與驗收（\<2 小時）。

\---

\# 定位

AI Agent 任務委派母框架。將重複發生的任務（每週≥1次）拆成技能模組交給 Agent 自動執行，人僅於待審區進行驗收放行與反饋迭代。

\# 核心步驟

1\.  盤點重複任務並計算人力 vs. Agent 成本。

2\.  拆解為技能模組（SKILL.md 規格）。

3\.  Agent 背景排程執行，產出落地至待審區。

4\.  人工驗收（每日 \\\<2 小時），將修正回寫至 Skill。

---

## 3\. `ai-security-agent-governance`

\---

name: ai-security-agent-governance

description: AI 資安與 Agent 治理 Skill，檢查 AI Agent、自動化流程與企業平台的身份、權限、Shadow AI、資料外洩與煞車系統。

\---

\# 定位

為 AI Agent、自動化流程與企業 AI 平台建立治理與安全檢查。確保最小權限、操作日誌、人工核准、異常停止與定期審查機制。

\# 煞車系統七要素

1\.  身份：具備可識別 Agent 身份。

2\.  最小權限：僅授予任務所需權限。

3\.  操作日誌：完整記錄讀寫與 API 動作。

4\.  人工核准：高風險操作人審。

5\.  邊界與異常停止：目標漂移或成本暴漲時自動停止。

6\.  定期審查：定期審查權限與連接器。

---

## 4\. `ai-virtual-board-supervisor-agent`

\---

name: ai-virtual-board-supervisor-agent

description: AI 虛擬董事會 Supervisor Agent Skill，調度 CFO、CHRO、COO、CPRO、CSO，彙整跨職能建議並保留人工決策節點。

\---

\# 定位

AI 虛擬董事會中央調度 Supervisor。將經營事件（報名率下降、師資缺編、現金流警告、負評、使用率低）路由給主責與協作 Agent，合併衝突並產出決策報告。

\# 核心職責

1\.  辨識事件並進行 Agent 路由。

2\.  收集各角色（CFO/CHRO/COO/CPRO/CSO）建議，標記衝突與依賴。

3\.  整理綜合應對方案並記錄決策日誌，保留人工核准關卡。

---

## 5\. `dual-agent-human-sop`

\---

name: dual-agent-human-sop

description: 雙 Agent 協作 Human 操作 SOP｜Hermes × OpenClaw × Obsidian，建立任務卡、審核報告與沉澱流程。

\---

\# 定位

本機雙 Agent（Hermes × OpenClaw × Obsidian）個人操作 SOP：建立任務卡、要求 Hermes 規劃、人工檢查 Plan、交付 OpenClaw 執行、審核報告並沉澱 SOP/Skill。

\# 核心流程

1\.  建立任務卡與風險分級（低/中/高）。

2\.  請 Hermes 產出 Plan，人工檢查讀寫與權限。

3\.  交給 OpenClaw 執行並產出 Execution Report。

4\.  Human Review 驗收與沉澱 SOP / Skill Candidate。

---

## 6\. `enterprise-sovereign-ai-adoption`

\---

name: enterprise-sovereign-ai-adoption

description: 企業主權 AI 平台導入 Skill，評估 AI 任務應採雲端、受控或私有部署，設計資料、權限、稽核與 MVP 路線圖。

\---

\# 定位

協助企業判斷 AI 系統應使用雲端服務、私有部署或企業主權 AI 平台，並設計資料、模型、治理、權限、稽核與流程串接原則。

\# 導入流程

1\.  盤點資料與流程敏感度，進行任務分級（雲端、受控、私有）。

2\.  設計身份、權限與企業詞典。

3\.  設計完整日誌與稽核追蹤機制。

4\.  打造 MVP 並逐步擴大到多代理流程。

---

## 7\. `mimo-hermes-openclaw-diagnosis`

\---

name: mimo-hermes-openclaw-diagnosis

description: 協助設定與排錯 Xiaomi MiMo、Hermes Agent、OpenClaw 的模型連線，確認 API Key 類型、Base URL、provider 名稱與模型名稱。

\---

\# 定位

協助設定與排錯 Xiaomi MiMo、Hermes Agent、OpenClaw 的模型連線。核心任務是先確認 API Key 類型、Base URL、provider 名稱與模型名稱是否成對正確。

\# 核心判斷

| 方案 | API Key | Base URL |

|---|---|---|

| Pay-as-you-go | \`sk-xxxxx\` | \`https://api.xiaomimimo.com/v1\` |

| Token Plan | \`tp-xxxxx\` | \`https://token-plan-cn.xiaomimimo.com/v1\` |

\# Hermes 規則

  \- 使用 custom provider 時，provider 必須是 \`custom\`。

  \- 不要把 Hermes custom provider 命名成 \`xiaomi-coding\`、\`mimo\` 等。

  \- 設定檔：\`\~/.hermes/config.yaml\`、\`\~/.hermes/.env\`

\# OpenClaw 規則

  \- 需要 Node.js 22+

  \- Token Plan provider 可命名 \`xiaomi-coding\`

---

## 8\. `openclaw-agent-handbook`

\---

name: openclaw-agent-handbook

description: OpenClaw Agent 專屬手冊，做為穩定執行者依照 Hermes Plan 完成任務、記錄結果、回報差異與提出 Skill 候選。

\---

\# 定位

協助 OpenClaw 成為穩定執行者，依照 Hermes Plan 完成任務、記錄結果、回報差異並提出 Skill 候選。

\# 核心責任

1\.  遵守 Plan：依照 Hermes 的執行範圍與順序操作。

2\.  保留紀錄與回報偏差：記錄動作並輸出 Execution Report。

3\.  避免越權：不做未授權刪除或擴大範圍。

4\.  提出沉澱：若流程可重複，提出 Skill Candidate 建議。

---

## 9\. `opus-5-skill-calibration-standards`

\---

name: opus-5-skill-calibration-standards

description: Opus 5 世代 Skill 校準準則，作為整座 Skill 庫全面體檢、減法優化與約束補強的標準。

\---

\# 定位

把既有 Skill 遷移到 Opus 5 世代模型時的校準準則：先做減法（刪除舊世代重複自檢指令），再補約束（長度、範圍、回報與委派上限）。

\# 逐頁體檢流程

1\.  掃描：搜尋舊世代補強指令（「自我檢查」、「開代理複查」等）。

2\.  分類：判定「稽核痕跡（留）」或「品質補強（刪）」。

3\.  減法與補約束：補充長度校準、範圍鎖定、回報節奏與委派上限。

---

## 10\. `warp-ai-multi-agent`

\---

name: warp-ai-multi-agent

description: Warp AI Multi-Agent War Room Launch Configuration. Use when the user asks to configure Warp terminal launch configurations, set up multi-pane CLI agent layouts, or troubleshoot Warp terminal AI agent workflows.

\---

\# Warp AI Multi-Agent War Room

A skill for designing and configuring Warp Terminal Launch Configurations to create a multi-pane CLI AI Agent war room layout.

\#\# When to Use

Use this skill when the user asks to:

  \- Set up or configure Warp Terminal Launch Configurations

  \- Create a multi-pane CLI Agent workspace (e.g., Amp, Codex, Gemini, Warp Agent)

  \- Troubleshoot keybindings, terminal layouts, or launch scripts in Warp

\#\# Default Configuration

Four-pane split layout:

  \- Top-Left: Amp (large refactoring & multi-file editing)

  \- Bottom-Left: Codex CLI (script generation)

  \- Top-Right: Gemini CLI (long-context & multimodal analysis)

  \- Bottom-Right: Status, logging, or token/cost monitor pane

\`\`\`yaml

name: AI Multi-Agent

windows:

  \- tabs:

      \- title: AI Command Center

        layout:

          split\_direction: horizontal

          children:

            \- layout:

                split\_direction: vertical

                children:

                  \- command: "amp"

                  \- command: "codex chat"

            \- layout:

                split\_direction: vertical

                children:

                  \- command: "gemini"

                  \- command: "echo '🟢 Ready — Warp Agent / Log Pane'"

## Workflow & Validation

1. Verify CLI tools are installed and callable in terminal environment.  
2. Generate or update the Warp Launch Configuration YAML block.  
3. Verify panel layout and keybindings to avoid terminal shortcut conflicts.  
4. Save to Warp Drive for cross-device synchronization if required.

## Gotchas

- Multiple terminal panes provide workspace layout, not mandatory simultaneous agent execution.  
- Do not spawn secondary agents solely to review primary agent outputs unless needed for parallel tasks.  
- Ensure the YAML configuration is complete and ready to paste into Warp editor.

\---

\# 二、 商業策略、創業與定價

\#\# 11\. \`ai-project-feasibility-assessment\`

\`\`\`markdown

\---

name: ai-project-feasibility-assessment

description: AI 專案落地評估 Skill，用商業價值與八維度框架評估 AI 專案是否值得導入、如何設計 MVP 與驗收指標。

\---

\# 定位

以終為始評估 AI 專案商業價值與技術可行性。套用八維度評估（問題規模/成功指標/重複性/容錯率/數據量/品質/成熟度/複雜度），設計 MVP 與路線圖。

\# 八維度評估

  \- \*\*商業維度\*\*：問題規模、成功指標、重複性、容錯率。

  \- \*\*技術維度\*\*：數據量、數據品質、技術成熟度、實施複雜度。

---

## 12\. `business-efficiency-scaling-strategy`

\---

name: business-efficiency-scaling-strategy

description: 商業效率與規模化做局 Skill，用 3S（系統化、持續性、規模化）與剛需象限診斷生意並設計做局策略。

\---

\# 定位

用系統化、持續性、規模化三個條件，判斷一個生意、顧問案或產品是否值得投入，並從「做事」升級成「做局」。

\# 核心架構

  \- 3S：系統化（SOP）、持續性（長期運作）、規模化（大量需求）。

  \- 剛需 × 規模化四象限：定位事業發展性。

  \- 策略：從傭兵模式轉成軍火商模式（提供工具、系統、分潤、平台或標準）。

---

## 13\. `business-model-canvas-diagnosis`

\---

name: business-model-canvas-diagnosis

description: 商業模式九宮格診斷 Skill，用九宮格診斷價值主張、客群、通路、活動、資源、成本與收益並找出斷點。

\---

\# 定位

用商業模式九宮格診斷一個事業、產品、個人品牌或專案是否具備可持續性，並找出價值主張與收益流之間的斷點與北極星指標。

\# 核心九宮格

價值主張、目標客群、通路、客戶關係、收益流、成本結構、關鍵活動、關鍵資源、關鍵夥伴。

\# 診斷重點

1\.  收益是否大於成本。

2\.  找出最可能斷裂的環節與最大脆弱點。

3\.  設定連到收益的北極星指標。

---

## 14\. `client-filtering-brand-positioning`

\---

name: client-filtering-brand-positioning

description: 客戶篩選與品牌定位 Skill，依市場規模、品牌定位與期待管理判斷該服務誰、不服務誰與如何有限客製化。

\---

\# 定位

協助使用者決定「要服務誰、不服務誰」，用市場規模、品牌定位與客戶期待管理，篩選真正適合的客戶。

\# 核心流程

1\.  \*\*反饋盤點\*\*：分析客戶喜歡與不喜歡的原因。

2\.  \*\*客群分類與市場規模\*\*：評估目標受眾是否足以支撐事業。

3\.  \*\*品牌定位與門口標示\*\*：明確宣示核心特色與不服務的對象。

4\.  \*\*期待管理與有限客製化\*\*：訂出可客製與不可客製的邊界。

---

## 15\. `moosie-ai-startup-brand-assets`

\---

name: moosie-ai-startup-brand-assets

description: Moosie Education AI 新創申請與品牌資產整理，包含英文官網、LinkedIn、Pitch deck 與對外品牌敘事。

\---

\# 定位

Moosie Education AI 新創申請與品牌資產整理助理。任務是把 Moosie 的 AI 新創計畫、英文官網、LinkedIn、團隊能力與對外敘事整理成可申請、可展示、可更新的品牌資產。

\# 主要目標

1\.  統一敘事：讓 Moosie 的教育理念、AI 能力與市場定位一致。

2\.  整理申請材料：把零散資訊轉成申請表、簡介、deck 或官網文案。

3\.  凸顯可信度：整理團隊經歷、教育場景、AI 應用與在地市場證據。

4\.  標記缺口：找出仍需補充的數據、案例、照片、連結或證明資料。

---

## 16\. `moosie-niche-demolisher`

\---

name: moosie-niche-demolisher

description: 【Research Skill】Moosie｜Category-of-One Niche Demolisher，找出高需求、低競爭的 Instagram 補教品牌子定位。

\---

\# 定位

把 Moosie Education 的 Instagram 從一般補習班帳號重新定位成 Category-of-One。分析市場擁擠區、家長真實需求，建立難以複製的內容切角與矩陣。

\# 核心架構

1\.  \*\*擁擠區與痛點分析\*\*：避開泛用「有趣全美語」訴求，鎖定家長對「孩子聽得懂但不敢開口」的深層焦慮。

2\.  \*\*Category-of-One 定位\*\*：建立定位句與比較矩陣。

3\.  \*\*內容支柱與系列\*\*：規劃「孩子敢開口的瞬間」、「小班全美語課堂觀察」等支柱，產出 Reels hook、carousel 標題與 IG bio。

---

## 17\. `mvp-validation-iteration`

\---

name: mvp-validation-iteration

description: 產品 MVP 驗證與迭代 Skill，用需求四象限、MVP、假廣告、預購、用戶訪談與放棄率分析驗證產品。

\---

\# 定位

在產品開發前，用最低成本驗證痛點、需求強度、使用頻率與付費意願，避免過度開發。

\# 核心流程

1\.  確認痛點、強度、頻率與付費意願。

2\.  需求四象限分析（強/弱需求 × 高/低頻率）。

3\.  設計 MVP（假廣告、預購、原型、表單）並測試微步驟成交。

4\.  用戶訪談與放棄率分析，提出迭代決策（做／小規模測／暫緩／放棄）。

---

## 18\. `pricing-strategy-conversion-system`

\---

name: pricing-strategy-conversion-system

description: 定價策略與成交系統 Skill，設計價格、報價情境、成交流程與回購系統。

\---

\# 定位

協助使用者設計價格、報價情境、成交流程與回購系統，判斷該採短期高溢價、長期品牌、封閉式報價或公開標準品策略。

\# 核心架構

1\.  定價策略：評估成本與毛利，區分短期與長期品牌型。

2\.  報價系統：判斷採封閉式報價（客製/價值導向）或開放式報價（標準/價格導向）。

3\.  成交流程與回購設計：信任證據、CRM 回訪與推薦機制。

---

## 19\. `startup-cashflow-pnl-planning`

\---

name: startup-cashflow-pnl-planning

description: 創業現金流與損益表規劃 Skill，建立個人、副業與創業損益表，拆解業績目標、情境與悲觀現金流底線。

\---

\# 定位

協助建立損益表、現金流情境、業績目標與悲觀底線，計算現金可支撐月數與可承擔試錯次數。

\# 核心流程

1\.  建立月度損益表（收入 \- 成本 \- 費用 \= 淨利）。

2\.  情境規劃（低、中、高收入與悲觀底線）。

3\.  業績目標由下而上拆解（單價 × 數量 × 頻率）。

4\.  悲觀現金水位計算與 pre-sale 測試建議。

---

## 20\. `startup-venture-builder`

\---

name: startup-venture-builder

description: Startup Venture Builder for opportunity discovery, market validation, MVP roadmap, business modeling, sales system, and investor stress testing. Use when the user asks for startup idea validation, business model design, MVP roadmap, landing page copy, or startup stress testing.

\---

\# Startup Venture Builder

A comprehensive skill for transforming early-stage business ideas into validated, market-ready, and monetizable ventures through a 12-phase framework.

\#\# When to Use

Use this skill when the user asks to:

  \- Evaluate, discover, or validate startup ideas and market opportunities

  \- Design business models, pricing strategies, and revenue models

  \- Plan a 30-day MVP roadmap or minimal validation process

  \- Create landing page copy, sales systems, or customer personas

  \- Conduct growth planning, content strategy, or investor stress testing

\#\# Core Workflow

Recommended execution order: Focus on Phase 1 (Opportunity Discovery) \-\> Phase 3 (Problem Validation) \-\> Phase 5 (30-day MVP) \-\> Phase 12 (Stress Test) first. Proceed to sales and content engines after core validation.

\#\#\# Phase 1: Idea Discovery

Identify high-demand, low-competition, monetizable business concepts. Evaluate pain intensity, willingness to pay, and feasibility.

\#\#\# Phase 2 & 3: Market & Problem Validation

Analyze market size, competitors, and industry trends. Test whether the problem is severe enough that customers will pay for a solution.

\#\#\# Phase 4 & 5: Business Model & 30-Day MVP

Design pricing tiers, customer acquisition channels, cost structures, and a 30-day MVP execution timeline with clear success/failure metrics.

\#\#\# Phase 6 to 10: Go-To-Market Systems

Draft landing page copy, customer personas, 90-day growth roadmap, sales outreach scripts, and a 30-day content calendar.

\#\#\# Phase 11 & 12: AI Team Simulation & Investor Stress Test

Simulate C-level perspectives (CEO, CMO, PM, Sales, CS) and conduct skeptical investor Q\&A to identify failure risks and mitigation plans.

\#\# Fact & Assumption Tagging

Always categorize statements using these explicit markers:

  \- Fact: Supported by verified data or user experience

  \- Deduction: Derived from market logic

  \- Hypothesis: Requires empirical validation (MVP, interviews, sales test)

\#\# Gotchas

  \- Do not attempt all 12 phases in a single turn unless explicitly requested.

  \- Distinguish true business opportunities from mere unverified ideas.

  \- Keep output concise and actionable; avoid generic startup jargon.

---

# 三、 行銷、品牌、公關與溝通

## 21\. `ai-content-monetization-side-hustle`

\---

name: ai-content-monetization-side-hustle

description: AI 自媒體斜槓變現 Skill，用 AI 完成市場研究、個人定位、內容轉化、產品階梯與自動化成交設計。

\---

\# 定位

協助個人將 AI 與自媒體結合，完成自我盤點、受眾 Persona、一句話定位、多平台內容轉化與免費至高價的產品階梯設計。

\# 產品階梯

  \- \*\*免費\*\*：貼文、模板、Podcast（建立觸及與信任）。

  \- \*\*低價\*\*（免費–500）：講座、電子書（初次成交）。

  \- \*\*中價\*\*（1,000–3,000）：線上課、工作坊（系統學習）。

  \- \*\*高價\*\*（5,000–100,000+）：陪跑、顧問、代操（客製成果）。

---

## 22\. `customer-service-email-routing`

\---

name: customer-service-email-routing

description: 信件與客服分流回覆 Skill，收信分類、依知識庫產出草稿並進行風險分級與人審放行。

\---

\# 定位

收信與客服分流回覆。分類信件、檢索知識庫答案、產出草稿與分級（一般詢問快放行，含金額/承諾/爭議必人審）。

\# 執行步驟

1\.  \*\*分類\*\*：一般詢問 / 合作邀約 / 金流爭議 / 垃圾信。

2\.  \*\*知識庫檢索\*\*：尋找對應答案並標註引用來源。

3\.  \*\*產出草稿與風險分級\*\*：

      \- 🟢 低風險：待審快放行。

      \- 🔴 高風險（含金額、退費、承諾）：標紅必人工審核。

4\.  \*\*記錄與追蹤\*\*：更新至 CRM 或系統。

---

## 23\. `marketing-brief-competitor-analyst`

\---

name: marketing-brief-competitor-analyst

description: Analyze marketing briefs, research real-time market competitors, and deliver strategic brand messaging positioning recommendations. Use when the user asks to analyze marketing briefs, research competitors, or refine brand positioning.

allowed-tools: google

\---

\# Marketing Brief & Competitor Analyst

A skill for parsing internal marketing briefs, conducting targeted web search research on key competitors, and formulating actionable brand positioning and message adjustment strategies.

\#\# When to Use

Use this skill when the user asks to:

  \- Review a marketing brief and evaluate brand positioning

  \- Perform competitor research and market intelligence analysis

  \- Refine value propositions, messaging pillars, or marketing copy against market alternatives

\#\# Workflow Steps

1\.  \*\*Brief Parsing\*\*:

      \- Extract core brand goals, target audience demographics, value proposition, and unique selling points (USPs) from the provided marketing brief.

2\.  \*\*Competitor Benchmarking\*\*:

      \- Utilize web search (\`google:search\`) to gather real-time data on top market competitors, their product messaging, pricing, and positioning.

      \- Map out a Competitor Matrix comparing Features, Positioning, Strengths, Weaknesses, and Brand Messaging Tone.

3\.  \*\*Strategic Brand Message Adjustment\*\*:

      \- Identify market gaps, white spaces, and points of differentiation.

      \- Formulate refined Brand Messaging Pillars (Primary Message, Supporting Points, Tone Guidelines, and Call-To-Action).

\#\# Gotchas

  \- Always base competitor insights on current web search data rather than static assumptions.

  \- Maintain an objective, balanced perspective when comparing brand strengths and weaknesses against competitors.

---

## 24\. `negotiation-strategy-script`

\---

name: negotiation-strategy-script

description: 談判準備與出牌策略 Skill，用談判八問、議題組合、出牌策略、回應劇本與 BATNA 完成談判前準備。

\---

\# 定位

談判準備與出牌策略腳本。回答談判八問、盤點籌碼、切割議題，設計開高/開低/開平方案，並準備對手反應劇本與 BATNA（退路）。

\# 核心流程

1\.  回答談判八問與籌碼盤點（我便宜/對方貴）。

2\.  議題切割與組合方案。

3\.  設計開局方案（開高/開低/開平/不出牌）與底線。

4\.  對手反應劇本（NO/YES/IF/沉默/黑白臉）與 BATNA 確立。

---

## 25\. `parent-communication-trust-building`

\---

name: parent-communication-trust-building

description: 家長訊息回覆與信任建立 Skill（Moosie 老師版），產出四段結構（同理、具體觀察、做法、下一步）的 LINE 回覆草稿。

\---

\# 定位

把家長訊息回覆變成可重複執行的產出流程。先分類情境與風險等級，再依「同理 → 具體觀察 → 做法 → 下一步」產出可編修草稿。

\# 安全紅線

  \- 不承諾未確認的事（補課名額、時段、優惠）。

  \- 金額一律寫成 \`＿＿＿（請填入行政報價）\`。

  \- 師資疑慮、客訴、退費等高風險議題，草稿建議改約電話。

  \- 具體觀察必須真實，沒有資料就留空格，不得編造孩子進步。

---

## 26\. `personal-brand-sponsorship`

\---

name: personal-brand-sponsorship

description: 個人品牌與廠商合作 Skill，協助創作者建立個人品牌定位、內容策略、廠商邀約判斷、合約檢查與業配文案。

\---

\# 定位

協助創作者、個人品牌與自媒體經營者找到核心價值、建立內容風格、判斷廠商邀約、檢查合約條款，並培養長期合作關係。

\# 核心流程

1\.  \*\*個人定位\*\*：核心價值、受眾與內容風格。

2\.  \*\*內容策略\*\*：日常故事、專業知識、互動 QA、產品體驗。

3\.  \*\*邀約與合約檢查\*\*：核對品牌背景、商品、報酬、發文日期、授權、保密條款，排除未揭露或誇大風險。

4\.  \*\*故事化文案\*\*：將個人體驗連結產品特色，明確設置 CTA。

---

## 27\. `pr-brand-crisis-management`

\---

name: pr-brand-crisis-management

description: 公關品牌與危機處理 Skill，設計公關策略、品牌核心訊息、PESO 媒體組合、利益關係人管理與危機處理 SOP。

\---

\# 定位

協助企業、品牌或個人建立公關策略、品牌核心訊息、利益關係人管理、媒體應對、PESO 媒體組合與危機三階段處理流程。

\# 核心流程

1\.  \*\*統一核心訊息\*\*：設定三個跨平台一致的主訊息與證據支撐。

2\.  \*\*PESO 媒體組合\*\*：整合 Paid, Earned, Shared, Owned 管道。

3\.  \*\*危機處理三階段\*\*：

      \- 預防：風險評估與演練。

      \- 控制：24 小時內快速聲明、負責態度與行動。

      \- 修復：補償措施與長期追蹤。

---

# 四、 社群經營、內容創作與文案

## 28\. `article-to-social-content-pack`

\---

name: article-to-social-content-pack

description: 將長文、對話、影音逐字稿或核心主題，一鍵改寫並拆解為多平台社群內容切片大禮包。內容包含 1200 字深度長文（WHY-HOW-WHAT 金字塔架構）、10 個高點擊吸睛標題、IG 5-6 頁圖文卡片視覺與短影音腳本、Midjourney 英文 AI 繪圖提示詞，以及 Threads 5 則金句串文。支援自動匯出與同步至 Google Drive/Docs/Sheets。適用於使用者要求將文章轉為社群貼文、做多平台內容矩陣、產出 IG 圖文、Threads 串文、短影音腳本或匯出貼文檔案時。

\---

\# Article to Social Content Pack (文章一鍵轉多平台社群內容包)

將深度文章、對話紀錄、Podcast 逐字稿或核心觀點，拆解改寫為符合台灣繁體中文在地語感（去 AI 味、說人話）與現代社群傳遞節奏的多平台內容矩陣大禮包，並可自動匯出同步至 Google Drive、Docs 與 Sheets。

\#\# When to Use

當使用者提出以下需求時觸發：

  \- 將長文章、書籍摘錄、觀點、對話或影片逐字稿轉換為社群貼文。

  \- 要求一次產出多平台內容（部落格/FB 長文 \+ 吸睛標題 \+ IG 圖文 \+ 短影音腳本 \+ Midjourney Prompts \+ Threads 串文）。

  \- 建立一魚多吃的個人品牌或自媒體社群內容矩陣。

  \- 要求將產出的社群貼文或大禮包匯出成文件並放在 Google Drive 指定資料夾（如「每日貼文」資料夾）或同步至 Google Sheets。

\#\# Core Language & Tone Standards (台灣繁體去 AI 味規範)

本技能產出之所有中文內容，必須嚴格遵守以下語感校準規範：

1\.  \*\*消除 AI 罐頭套話與句型\*\*：堅決移除「不可否認」、「毋庸置疑」、「總而言之」、「值得注意的是」等。

2\.  \*\*台灣在地用語與標點\*\*：校正中國用語，中文嚴格使用全形標點（，。！？；：「」『』）。

3\.  \*\*人味溝通與開門見山\*\*：開門見山直擊主題，展現人間溫度與真誠直率。

\#\# Workflow & Deliverables Structure

1\. \*\*步驟 1：改寫文章\*\*（1000–1200 字深度長文，黃金圈 WHY-HOW-WHAT 架構）。

2\. \*\*步驟 2：10 個吸睛標題發想\*\*（迷思翻轉、名人背書、場景、數字法則、反直覺）。

3\. \*\*步驟 3：IG 圖文及短影音設計\*\*（5–6 頁 Carousel \+ 2–3 支短影音腳本）。

4\. \*\*步驟 4：AI 繪圖 Prompts（英文）\*\*（Midjourney / DALL-E 3 直式 \`--ar 4:5\` 提示詞）。

5\. \*\*步驟 5：Threads 串文\*\*（5 則短句連發串文與互動選擇題）。

---

## 29\. `couple-podcast-hosting`

\---

name: couple-podcast-hosting

description: 夫妻對談 Podcast 主持流程 Skill，提供提問、追問與收尾腳本、三幕劇節奏與降溫技巧。

\---

\# 定位

夫妻對談 Podcast 主持流程腳本。跑三幕劇節奏（開場/第一幕建立/第二幕攤開/第三幕轉念），提供逐題腳本卡（提問句/追問句/轉場句）、現場降溫三句與結尾收斂機制。

\# 三幕劇節奏

  \- \*\*開場\*\*（0–3 分）：拋出真實小衝突（第 0 題）。

  \- \*\*第一幕：建立\*\*（3–13 分）：熱機、建立連結（金錢記憶、被愛到的瞬間）。

  \- \*\*第二幕：攤開\*\*（13–33 分）：讓隱形的變可見，呈現落差不急著和解（Mental Load 遊戲、一起扛、原生家庭界線、錢的排序）。

  \- \*\*第三幕：轉念\*\*（33–50 分）：從對立轉共同建構（教養第一句話、三條紅線、小家庭儀式、孤單瞬間、60 歲的午餐）。

  \- \*\*結尾收斂\*\*（最後 3 分）：歸納共識、落差與下週試執行的行動。

---

## 30\. `newsletter-topic-selection-writing`

\---

name: newsletter-topic-selection-writing

description: 電子報選題與撰寫 Skill，每週固定選題、主文撰寫、標題/預覽文字、導流 CTA 與待審寄送流程。

\---

\# 定位

每週電子報選題與撰寫：從素材池挑選高讀者價值題材，撰寫主文、3 組主旨與預覽文字、精選連結與導流 CTA，並進行待審排程。

\# 執行步驟

1\.  從素材池選題（讀者價值 × 時效 × 主軸相關）。

2\.  撰寫主文（含 1 個可立刻行動的方法）。

3\.  產出 3 組主旨與預覽文字。

4\.  挑選 3–5 則精選連結並寫推薦理由。

5\.  設定 CTA，放入待審區等待人工放行。

---

## 31\. `precise-narrative-storytelling`

\---

name: precise-narrative-storytelling

description: 精準敘事 Skill｜把真實經驗變成好故事，用衝突找亮點、4P 萃取故事 DNA、故事九宮格三幕劇展開。

\---

\# 定位

把真實經驗轉換成好故事的可重用流程。用衝突（人與環境/人/自我/社會）切入、4P（Purpose/Problem/Promise/Practice）萃取骨架，並展開三幕劇與亮點邏輯檢查。

\# 核心架構

  \- \*\*衝突類型\*\*：人與環境、人與人、人與自我、人與社會制度。

  \- \*\*4P 骨架\*\*：Purpose（目標）、Problem（阻礙）、Promise（決心）、Practice（付出）。

  \- \*\*三幕劇比例\*\*：第一幕 20%（建立）、第二幕 40%（阻礙）、第三幕 40%（轉念與行動）。

---

## 32\. `social-content-batch-production`

\---

name: social-content-batch-production

description: 社群經營內容量產 Skill，從既有素材拆解產出一週社群貼文排程，包含平台改寫、標題鉤子與圖文建議。

\---

\# 定位

從長內容（文章、逐字稿、電子報、Podcast）拆解並量產一週社群貼文（Threads/IG/FB/LinkedIn），包含鉤子、內容、圖文建議與排程。

\# 執行步驟

1\.  讀取素材，抽出 3–7 個獨立觀點。

2\.  改寫為目標平台原生格式（鉤子 → 內容 → CTA）。

3\.  產生 3 種標題/開頭 A/B 變體與圖文/畫面建議。

4\.  整理為待審排程表，待人工放行。

---

## 33\. `social-data-retrospective-private-domain`

\---

name: social-data-retrospective-private-domain

description: 社群數據覆盤與私域經營 Skill，建立社群內容週期、IG/FB 數據覆盤、電子報與公域轉私域導流。

\---

\# 定位

用數據驅動社群內容與私域經營，建立規劃、創作、發佈、覆盤、電子報、名單磁鐵與公域轉私域的完整流程。

\# 核心流程

1\.  \*\*內容配比\*\*：60% 出圈內容（擴大觸及） \+ 40% 養粉內容（建立信任）。

2\.  \*\*數據紀錄與週覆盤\*\*：追蹤觸及、觀看、按讚、儲存與分享，只與自身歷史平均相比。

3\.  \*\*公域轉私域\*\*：設計名單磁鐵，將流量導入電子報或私域名單，並定期進行名單清理。

---

## 34\. `speak-human-tw`

\---

name: speak-human-tw

description: 「說人話」繁體中文去 AI 味改寫技能。識別 AI 寫作痕跡，校正中國用語與半形標點，提升自然度與台灣繁體語感。

\---

\# 定位

繁體中文去 AI 味與自然語感校準技能。消除常見 AI 罐頭句型、對偶對稱套話，校正中國用語與標點符號，使回應呈現自然、真誠、直接的人類口吻。

\# 核心規範

1\.  \*\*消除 AI 罐頭句型與套話\*\*：

      \- 移除「不可否認」、「毋庸置疑」、「總而言之」、「值得注意的是」、「在當今快節奏的時代」、「作為一個...」、「讓我們一同...」等無意義起手式與結尾套話。

      \- 避免過度對稱、排比或駢偶句式，保持句型長短交錯與自然節奏。

      \- 消除罐頭同理心（如「我完全理解您的焦慮」），改用具體事實與行動回應。

2\.  \*\*台灣繁體中文用語與標點\*\*：

      \- 矯正中國用語（信息→訊息、軟件→軟體、視頻→影片、網絡→網路、優化/數據/項目依語境校正）。

      \- 嚴格使用全形標點符號（，。！？；：「」『』），不使用半形標點。

3\.  \*\*人味溝通與實用導向\*\*：

      \- 開門見山、直接切中要害、語氣平實，不吹噓、不說空話，不堆砌無意義小標題。

---

## 35\. `threads-viral-consultant`

\---

name: threads-viral-consultant

description: Threads content strategy and conversion consultant. Use when the user asks to create Threads posts, optimize Threads profile bio, design Threads content funnel, analyze viral Threads posts, or build Threads DM conversion scripts.

\---

\# Threads Viral Consultant

A specialized skill for building Threads content strategies, writing engaging posts, optimizing profile bios, and designing DM conversion funnels.

\#\# When to Use

Use this skill when the user asks to:

  \- Design Threads account positioning, bio, pinned post, or content pillars

  \- Diagnose Threads engagement, follower growth, or conversion bottlenecks

  \- Write viral Threads posts, hook lines, thread series, or CTAs

  \- Build a weekly or monthly Threads content calendar

  \- Create DM sales scripts and lead magnet funnels for Threads

\#\# Core Workflow

\#\#\# 1\. Funnel Mapping

  \- Awareness: High-hook, emotional resonance, life observation, or trend piggybacking

  \- Interest: Interactive questions, polls, and opinion stance

  \- Trust: How-to guides, case studies, personal stories, and methodology

  \- Conversion: Resource lead magnets, results showcase, consultation CTA

\#\#\# 2\. Content Structure

  \- Short Post: Hook line \-\> Emotional punch \-\> Twist \-\> Open question / CTA

  \- Long Post: Perspective \-\> Background \-\> Problem \-\> Solution \-\> Example \-\> Conclusion \-\> CTA

  \- Reply Thread: Method details \-\> Case study \-\> Lead magnet CTA

  \- DM Funnel: Icebreaker \-\> Problem diagnosis \-\> Value delivery \-\> Need creation \-\> Offer pitch

---

## 36\. `video-editing-preproduction-script-cuts`

\---

name: video-editing-preproduction-script-cuts

description: 影片剪輯前製與腳本切點 Skill，從帶時間碼逐字稿產出保留/刪除區段、章節、標題與短影音選段。

\---

\# 定位

從帶時間碼的逐字稿進行長影片/Podcast 前製剪輯分析：標記章節時間碼、贅語刪除區段、短影音高張力片段選段與封面文案。

\# 執行步驟

1\.  標出主題段落與章節時間碼。

2\.  標記可刪區段（贅語、重複、離題、口誤）。

3\.  產出剪輯清單（保留/刪除/建議壓縮）。

4\.  挑選 3–5 個短影音高張力選段。

5\.  產出標題、章節說明與勘誤表。

---

## 37\. `website-landing-page-builder`

\---

name: website-landing-page-builder

description: 網站／落地頁建置 Skill，用 Agent 直接產出可上線的互動式單頁（敘事、版面、前後對照、成本試算、CTA）。

\---

\# 定位

一頁式說明/課程招生/專案展示落地頁建置。擬定敘事段落（痛點→對照→機制→成本效益→社會證明→CTA），產出單檔 HTML/CSS/JS 與 SEO/GEO 要素。

\# 執行步驟

1\.  定敘事段落與唯一 CTA。

2\.  決定互動形式（時間軸、切換對照、展開卡、試算器）。

3\.  產出單檔 HTML/CSS/JS 原型（行動版優先）。

4\.  補充 SEO/GEO 結構化資料與可爬取文字。

5\.  人工驗收與部署。

---

## 38\. `youtube-learning-summary-exporter`

\---

name: youtube-learning-summary-exporter

description: 批量抓取指定 YouTube 頻道最新影片逐字稿，轉換為結構化速讀摘要、問答解析與行動建議，並自動匯出至 Google Drive 資料夾。當使用者要求整理 YT 頻道最新影片、製作影片學習筆記、產出逐字稿精華或匯出自學筆記至 Drive 時使用。

allowed-tools: youtube drive docs\_agent

\---

\# YouTube 學習摘要與 Drive 匯出工作流 (YouTube Learning Summary Exporter)

本 Skill 提供一站式自動化流程：從 YouTube 頻道檢索最新影片、取得逐字稿與元資料、提煉高價值結構化摘要，並將內容自動創建或更新至 Google Drive 指定資料夾中的文件。

\#\# 使用時機 (When to Use)

  \- 使用者提供一系列 YouTube 頻道（或頻道連結、清單），要求研究或整理其最新影片內容。

  \- 使用者要求將影片逐字稿轉換為結構化筆記、摘要、行動建議（Action Items）或金句。

  \- 使用者要求將學習摘要匯出到 Google Drive 指定資料夾（如「每日自學」或「影片筆記」）。

\#\# 工作流程步驟 (Steps)

1\. \*\*確認頻道清單與 Drive 目標資料夾\*\*：搜尋或建立目標資料夾。

2\. \*\*獲取最新影片與逐字稿\*\*：透過 YouTube 搜尋與逐字稿 API 提取影片字幕。

3\. \*\*結構化摘要提煉規範\*\*：提煉項目一/二、問答要點、行動建議與中英文金句。

4\. \*\*匯出至 Google Drive\*\*：建立 Google Doc 並寫入結構化內容。

5\. \*\*結果回報\*\*：提供文件點擊連結與精華預覽。

---

# 五、 決策思維、心智模型與領導

## 39\. `checklist-manifesto-agent`

\---

name: checklist-manifesto-agent

description: 清單革命 Agent Skill，依據《清單革命》與 Boorman 六原則，協助使用者設計、使用與診斷 5-9 項 Checklist。

\---

\# 定位

依據《清單革命》與 Boorman 六原則，協助使用者設計、使用與診斷清單。專門降低「知道卻忘了做」的無能之錯。

\# Boorman 六步

1\.  時機：明確定義使用場景。

2\.  來源：彙整現有 SOP 或過往漏項。

3\.  篩選：用五問（認知超載、時間壓力、不可逆成本、延遲反饋、高後果）篩選。

4\.  分類：Do-Confirm 或 Read-Do。

5\.  寫法：改成可驗證、動詞起頭、結果導向。

6\.  迭代：控制在 5-9 項，實測 3 次後修訂。

---

## 40\. `decision-consulting-matrix`

\---

name: decision-consulting-matrix

description: 決策諮詢 Skill（顧問級提問與方案比較），把重大選擇拆成方案矩陣：條件釐清、成本效益、風險、逆轉成本與建議。

\---

\# 定位

面臨投資、定價、僱人或產品線選擇時，進行條件釐清、成本效益、風險、逆轉成本與加權評分比較。

\# 執行步驟

1\.  反問關鍵問題，補齊缺失前提。

2\.  列出各方案成本、預期效益、時間、所需能力與逆轉成本。

3\.  建立加權比較矩陣並給出明確建議。

4\.  設定先行小實驗、檢核日與退場條件。

---

## 41\. `decision-making-superpowers`

\---

name: decision-making-superpowers

description: obra/superpowers 決策類 skill，協助把模糊問題、選項與權衡條件整理成可判斷、可比較、可執行的決策流程。

\---

\# 定位

協助使用者把模糊問題、選項與權衡條件整理成可判斷、可比較、可執行的決策流程。

\# 決策流程

1\.  \*\*重述決策問題\*\*：把模糊選擇改寫成清楚的決策句。

2\.  \*\*列出方案\*\*：包含候選方案、維持現狀與小規模測試方案。

3\.  \*\*建立評估矩陣\*\*：比較對目標的影響、成本、時間、可逆性、風險與執行難度。

4\.  \*\*給出建議與驗證計畫\*\*：設計低成本小實驗。

---

## 42\. `minerva-82-hcs-daily-coach`

\---

name: minerva-82-hcs-daily-coach

description: Minerva 82 HCs 每日教練 Agent Skill，將 Minerva 82 HCs 心智習慣轉成每日學習、練習、應用與反思。

\---

\# 定位

將 Minerva 82 HCs 心智習慣與基礎概念轉成每日學習教練 Skill，協助使用者每天進行 HC 學習、反思、應用與追蹤。

\# 每日教練流程

1\.  \*\*今日聚焦\*\*：選定 1 個 HC。

2\.  \*\*概念說明\*\*：用一句話與一個例子說明。

3\.  \*\*錯誤示範\*\*：指出常見誤用。

4\.  \*\*實作練習\*\*：讓使用者套用到當天問題。

5\.  \*\*反思記錄\*\*：記下輸出、洞察與疑問。

6\.  \*\*明日銜接\*\*：推薦下一個相關 HC。

---

## 43\. `problem-reframing-constraints`

\---

name: problem-reframing-constraints

description: 問對問題與限制條件 Skill，透過現況分析、目標設定、障礙與限制條件，把模糊困境拆成可處理的核心問題。

\---

\# 定位

協助使用者在急著找解法前，先問對問題。透過現況分析、目標設定、障礙與限制條件，將模糊困境拆成可處理的核心問題。

\# 核心流程

1\.  現況分析與目標設定（理想狀態）。

2\.  列出不可改或成本太高的限制條件。

3\.  找出最影響目標的主要障礙。

4\.  重寫問題並提出對焦方案。

---

## 44\. `questioning-leadership-dialogue`

\---

name: questioning-leadership-dialogue

description: 提問式領導 Skill｜用好問題帶人、溝通與對話，以好奇心為核心，用 5WH 與 ALAR 四步驟引導對話。

\---

\# 定位

用好問題帶人、溝通與對話。先用 5WH 準備，跑 ALAR（Ask-Listen-Awareness-Response）對話循環，遵循 3S（簡單/簡短/具體）與由淺而深原則。

\# 核心技巧

  \- \*\*3S 原則\*\*：Simple（簡單好記）、Short（30 秒內）、Specific（具體可行動）。

  \- \*\*四大技巧\*\*：承轉力（鏡像與對接）、正向提問力（少問 Why、改問 How/What與未來式）、重點力（歸納成三點）、追問力（例子與比方）。

---

## 45\. `rumor-buster`

\---

name: rumor-buster

description: 根據 Allport & Postman 謠言心理學框架，系統性分析謠言與未經證實訊息的形成背景、傳播動機、失真機制（平化、銳化、同化），並產出結構化查證與破解應對策略。適用於假新聞、網路謠言、陰謀論分析與危機溝通。

allowed-tools: google

\---

\# 謠言破解分析師（Rumor Buster）

本技能基於 Gordon Allport 與 Leo Postman 的經典社會心理學著作《謠言心理學》（The Psychology of Rumor），提供一套標準化的分析與破解框架。

\#\# 核心理論架構

\#\#\# 1\. 謠言強度公式

$$R \\propto i \\times a$$

\- 謠言強度（R）取決於重要性（importance, i）與模糊性（ambiguity, a）的乘積。

\- 破解核心：降低模糊性（提供清晰且可驗證的完整資訊）。

\#\#\# 2\. 謠言的三大動機類型

\- 恐懼型（Fear rumors）、離間型（Wedge-driving rumors）、白日夢型（Wish rumors）。

\#\# 六大分析維度與執行流程

1\. 確認謠言內容與核心主張。

2\. 評估謠言強度（R ∝ i × a）。

3\. 心理動機與社會功能剖析。

4\. 傳播失真機制拆解（真實種子 \-\> 平化 \-\> 銳化 \-\> 同化）。

5\. 實質事實查證與多元比對。

6\. 制定破解與溝通應對策略（替代敘事、可信來源、降低情緒溫度、防範真相錯覺效應）。

---

# 六、 教學研究、學習與知識庫

## 46\. `ai-research-lab`

\---

name: ai-research-lab

description: research-lab AI 研究實驗室 Skill v3.1，將複雜主題拆成可驗證、可收斂、可決策的研究流程。

\---

\# 定位

把複雜主題拆成可驗證、可收斂、可決策的研究流程，結合廣度掃描、深度鑽研與綜合報告。

\# 核心流程

1\.  定義研究題目與決策用途。

2\.  廣度掃描：建立多個研究面向，篩選高價值方向。

3\.  深度鑽研：逐層拆解問題、證據與可行動結論。

4\.  綜合報告：產出 Executive Summary、核心發現、風險與建議。

---

## 47\. `course-outline-source-enricher`

\---

name: course-outline-source-enricher

description: Extract, verify, and format URLs and web references within course outlines, appending them into structured source lists. Use when the user asks to add web references, sources, or links to a course syllabus or outline.

\---

\# Course Outline Source Enricher

A skill that parses course outlines or syllabi, extracts all embedded or implied web links and references, verifies their validity, and formats them into a standardized "Data Sources / Reference Links" section.

\#\# When to Use

Use this skill when the user asks to:

  \- Add web links, references, or source citations to a course outline or syllabus

  \- Extract and verify all URLs embedded across course modules

  \- Format course references into structured citation tables or resource lists

\#\# Workflow Steps

1\.  \*\*Extract Existing & Implied Links\*\*: Parse the course outline for raw URLs, hyperlinked terms, and mentioned publications/platforms.

2\.  \*\*Verify & Contextualize\*\*: Verify validity and categorize links into categories.

3\.  \*\*Format & Append\*\*: Append a standardized "Data Sources & References" section formatted as \`\[Source Title\](URL) \- Brief description of relevance\`.

---

## 48\. `pdf-study-guide-generator`

\---

name: pdf-study-guide-generator

description: Transform class notes into a comprehensive structured study guide, generate 5 practice questions, and compile them into a PDF. Use when the user asks to summarize notes into a PDF study guide with practice questions.

\---

\# PDF Study Guide Generator

A skill that takes lecture or class notes, synthesizes them into a structured study guide with key takeaways and 5 practice exercises, and exports the final document into a formatted PDF.

\#\# When to Use

Use this skill when the user asks to:

  \- Convert class notes or lecture transcripts into a complete PDF study guide

  \- Summarize study material and attach 5 practice questions or review exercises

  \- Generate structured PDF revision guides for exam preparation

\#\# Workflow Steps

1\.  \*\*Information Extraction & Structuring\*\*: Executive Summary, Key Terminology, Core Concepts, Detailed Study Modules.

2\.  \*\*Practice Exercises Creation\*\*: 5 targeted questions \+ detailed answer keys.

3\.  \*\*PDF Generation\*\*: Generate cleanly styled PDF via ReportLab/FPDF2 and save to Google Drive.

---

## 49\. `progressive-quiz-generator`

\---

name: progressive-quiz-generator

description: Generate 5 quizzes with progressive difficulty and distinct sub-topics based on user reference data. Use when the user asks to create progressive tests, multi-level quizzes, or topic-focused assessments from study materials.

\---

\# Progressive Quiz Generator

A structured skill for creating 5 quizzes from user-provided reference data, ensuring progressive difficulty levels and distinct sub-topic coverage.

\#\# Difficulty Ladder (5 Levels)

  \- \*\*Quiz 1 (Beginner \- Conceptual Recall)\*\*: Multiple choice / true-false questions focusing on basic definitions and facts.

  \- \*\*Quiz 2 (Elementary \- Basic Understanding)\*\*: Fill-in-the-blanks or short answers testing comprehension.

  \- \*\*Quiz 3 (Intermediate \- Application)\*\*: Scenario-based questions applying principles to concrete examples.

  \- \*\*Quiz 4 (Advanced \- Analysis & Comparison)\*\*: Comparative questions requiring critical comparison between concepts.

  \- \*\*Quiz 5 (Mastery \- Synthesis & Problem Solving)\*\*: Complex open-ended case studies requiring strategic synthesis.

---

## 50\. `research-to-insight`

\---

name: research-to-insight

description: Research-to-Insight 多來源研究轉洞察技能包，把文章、PDF、網頁、簡報等轉成 10 種結構化成果。

\---

\# 定位

把多來源資料轉成「可理解、可比較、可教學、可行動、可發布、可決策」的洞察成果。

\# 10 個關鍵模組

1\.  Key Takeaways（關鍵洞察）

2\.  Beginner Summary（初學者解釋）

3\.  Main Themes（主題與模式）

4\.  Study Guide（學習指南）

5\.  Source Comparison（來源比較）

6\.  Action Plan（行動步驟）

7\.  Knowledge Gaps（知識缺口）

8\.  Q\&A Sheet（問答題庫）

9\.  Content Repurposing（內容轉製）

10\. Executive Briefing（高階簡報）

---

## 51\. `single-source-of-truth-knowledgebase`

\---

name: single-source-of-truth-knowledgebase

description: 知識庫建置與單一真相源 Skill，將散落資訊收斂成可被 Agent 取用的單一真相源（Single Source of Truth）。

\---

\# 定位

將散落資訊收斂成可被 Agent 取用的單一真相源：建立命名規則、權威頁面、資料庫結構、過期檢驗與收斂流程。

\# 執行步驟

1\.  盤點來源，標記重複與衝突。

2\.  指定唯一權威頁面，其餘改為連結。

3\.  建立資料庫結構（主題、類型、狀態、負責人、最後驗證日）。

4\.  設定過期規則（如 90 天複驗）與新資訊收斂流程。

---

# 七、 專案管理、流程與日常運營

## 52\. `notion-ai-workflow-design`

\---

name: notion-ai-workflow-design

description: 協助判斷工作流程應沉澱成文件、Skill、資料庫自動化、N8N 或 AI Agent，並設計 Notion AI 工作流。

\---

\# 定位

協助判斷一個工作流程應該沉澱成 Notion 文件、Skill、資料庫自動化、N8N 流程或 AI Agent，並把它設計成可重複使用的 Notion AI 工作流。

\# 工作流設計流程

1\.  \*\*任務辨識\*\*：這是一次性任務，還是重複流程？

2\.  \*\*文件類型判斷\*\*：是 How-to、Why、Skill 還是資料庫？

3\.  \*\*自動化層級判斷\*\*：資料庫自動化、N8N、AI Agent 或人工處理。

4\.  \*\*觸發條件與輸入輸出\*\*：定義需求與品質標準。

---

## 53\. `notion-smart-doc-role-adapter`

\---

name: notion-smart-doc-role-adapter

description: 智能文件角色適應器，根據 Notion 文件類型、內容成熟度與意圖，切換編輯、顧問、SOP 設計師等角色。

\---

\# 定位

根據文件類型、內容成熟度與使用者意圖，自動切換成最適合的閱讀、整理、改寫或決策輔助角色（文件整理者、策略顧問、SOP 設計師、學習教練、產品 PM）。

\# 主要目標

1\.  辨識文件類型（概念、策略、SOP、會議紀錄、規格書等）。

2\.  辨識使用者意圖（理解、摘要、重寫、補充、轉格式或產出行動）。

3\.  切換最適角色並產出可貼回 Notion 的結構化內容。

---

## 54\. `product-launch-gate-checklist`

\---

name: product-launch-gate-checklist

description: 產品上線關卡檢查 Skill｜八階段 Exit Criteria，核對 Phase 0-7 上線關卡條件，判定 Go/No-Go。

\---

\# 定位

產品上線關卡檢查器。核對 Phase 0-7（發想/需求/設計/開發/測試/上線前/發佈/監控）之 Exit Criteria，給予 Go、No-Go 或有條件 Go。

\# 執行步驟

1\.  定位目前 Phase。

2\.  逐條核對 Exit Criteria（已達成/未達成/需確認）。

3\.  產出結論，僅列出阻擋項與最小完成動作（未確認項不當作通過）。

---

## 55\. `routine-task-report-aggregation`

\---

name: routine-task-report-aggregation

description: 雜事處理與報表彙整 Skill，定時抓取各平台數據、彙整成週報／月報，並把散落待辦收斂進單一任務庫。

\---

\# 定位

雜事處理與報表彙整：定時抓取多來源數據、統一口徑與計算指標，產出週報觀察與建議，並將散落待辦收斂進單一任務庫。

\# 執行步驟

1\.  抓取多平台數據、統一口徑與時間區間。

2\.  計算核心指標與週變化，標出異常值。

3\.  產出週報（數字 → 觀察 → 3 條建議）。

4\.  掃描待辦來源並收斂至任務庫。

---

# 八、 設計與視覺提案

## 56\. `design-proposal-portfolio-persuasion`

\---

name: design-proposal-portfolio-persuasion

description: 設計提案與作品集說服力 Skill，將設計專案整理成有脈絡的提案與作品集，並用十個設計心法檢查品質。

\---

\# 定位

協助設計師與品牌顧問把設計專案整理成有說服力的提案與作品集，包含品牌需求問卷、競品分析、十個設計優化心法與提案/作品集模組。

\# 核心流程

1\.  品牌問卷與競品分析。

2\.  套用十個設計心法（留白、對齊、比例、意象、節奏、網格、色彩、動線、洞察、持續優化）。

3\.  產出提案與作品集模組，根據受眾（客戶/面試官/團隊）調整細節。

---

## 57\. `logotype-design-logic-practice`

\---

name: logotype-design-logic-practice

description: 標準字設計：從生活創意到邏輯實踐，拆成識別性、造型性、系統性三原則，提供 Brief、檢核表與規範。

\---

\# 定位

將標準字設計從靈感轉成可溝通、可檢查、可交付的流程。依識別性、造型性（字重/字框/重心/中宮/筆畫）、系統性檢核與產出設計 Brief。

\# 三大原則

1\.  \*\*識別性\*\*：小尺寸與遠看仍可讀，具備記憶點且與競品區隔。

2\.  \*\*造型性\*\*：字重、字框、重心、中宮與筆畫風格一致。

3\.  \*\*系統性\*\*：包含安全距離、最小尺寸、色彩規範、搭配字型與不可使用範例。

---

## 58\. `presentation-structure-visual-script`

\---

name: presentation-structure-visual-script

description: 簡報製作 Skill（結構→視覺→講稿），先定敘事骨架與每頁一個訊息，再產出版面與講稿備忘。

\---

\# 定位

簡報製作流程：定敘事線（痛點→轉折→方法→證據→行動），一頁一訊息寫大字標題，標註視覺型態並產出講稿備忘。

\# 執行步驟

1\.  確定敘事線與大架構。

2\.  一頁一訊息：撰寫每頁大字標題。

3\.  標註視覺型態（數據圖/對照表/流程/引言）。

4\.  產出講稿備忘（每頁 2–3 句口語表達）。

---

# 九、 數據分析、財務與垂直領域

## 59\. `500dishes-restaurant-info-enrichment`

\---

name: 500dishes-restaurant-info-enrichment

description: 500盤餐廳對外資訊補齊 Skill，針對得獎餐廳補齊 Google Maps、官方社群、官網狀態與網站開發潛力。

\---

\# 500盤餐廳對外資訊補齊 Skill

\#\# 簡介

針對 500 盤得獎餐廳進行對外資訊補齊，彙整餐廳的 Google Maps 地標、FB/IG 官方帳號、官網狀態，並評估其網站開發潛力。

\#\# 執行步驟

1\. 查詢目標餐廳名稱與地址。

2\. 搜尋並記錄 Google Maps 連結與評分。

3\. 搜尋並記錄 FB 與 IG 官方粉專/帳號。

4\. 檢查是否有獨立官方網站及其功能狀態。

5\. 評估網站開發潛力（無官網、官網老舊、缺乏線上訂位功能等）。

---

## 60\. `merchant-info-verification`

\---

name: merchant-info-verification

description: 店家官網與社群資料查核 Skill，批次查核店家官網、地址、Google Maps 與官方 Instagram 等公開資料。

\---

\# 定位

將店家公開資料查核流程標準化，批次確認店家是否有正式官網，並補齊地址、Google Maps 與 Instagram 等基礎資料。

\# 官網判斷標準

  \- \`true\`：獨立官方網站、品牌購物網、官方訂位網、百貨/集團官方品牌頁。

  \- \`false\`：僅有 IG、FB、Google Maps、美食平台、新聞或部落格介紹。

  \- 資訊不確定時採保守判斷（\`false\`），不填入個人帳、粉絲帳或未核實地點。

---

## 61\. `product-revenue-growth-tracker`

\---

name: product-revenue-growth-tracker

description: Calculate revenue growth rates across product lines, build dynamic spreadsheets, and generate trend charts. Use when the user asks to compute revenue growth rates or plot product line revenue trends.

allowed-tools: sheets\_agent

\---

\# Product Revenue Growth Tracker

A skill for calculating period-over-period revenue growth rates across product lines, structuring data into Google Sheets, and plotting trend visualizations.

\#\# When to Use

Use this skill when the user asks to:

  \- Calculate MoM, YoY, or QoQ revenue growth rates for product lines

  \- Generate product revenue trend charts or dashboard spreadsheets

  \- Track and compare performance across product portfolios

\#\# Workflow Steps

1\.  \*\*Data Ingestion & Calculation\*\*: Parse figures, calculate percentage changes.

2\.  \*\*Spreadsheet & Chart Creation\*\*: Structure sheets and trend charts via \`sheets\_agent\`.

3\.  \*\*Strategic Insights\*\*: Highlight outperformers and contraction areas.

---

## 62\. `real-estate-market-modeler`

\---

name: real-estate-market-modeler

description: Analyze real estate transactions, research local market trends and forecasts, and build a financial valuation/modeling Google Sheet. Use when the user asks to evaluate real estate deals, research nearby property trends, or build real estate valuation spreadsheets.

allowed-tools: google sheets\_agent

\---

\# Real Estate Market Modeler

A skill for evaluating real estate transaction deals, researching surrounding neighborhood market trends via web search, forecasting price trajectories, and constructing property financial valuation models in Google Sheets.

\#\# Workflow Steps

1\.  \*\*Transaction & Market Analysis\*\*: Extract property details and search local comps.

2\.  \*\*Financial Modeling (Google Sheets)\*\*: Build cash flow, Cap Rate, ROI, DSCR, and 10-year appreciation models.

3\.  \*\*Strategic Narrative\*\*: Synthesize deal viability and risk analysis.

---

## 63\. `reconcile`

\---

name: reconcile

description: 處理財務、帳務或資料對帳（Reconciliation）的技能，協助核對資料差異、產出對帳報告與差異分析。

\---

\# Reconcile Skill

\#\# 概要

此 Skill 用於對帳與資料核對（Reconciliation）。協助比對不同來源的帳務、交易紀錄或資料集，找出不一致或差異項目並生成核對報告。

\#\# 執行步驟

1\. \*\*收集與確認資料來源\*\*：確認需要對帳的雙方資料。

2\. \*\*比對關鍵欄位\*\*：依據交易編號、金額、日期進行比對。

3\. \*\*分類差異\*\*：完美匹配、時間差/未達帳、金額不符、單邊缺失。

4\. \*\*產出對帳報告\*\*：標示異常項目與建議處理方式。

---

## 64\. `renovation-expense-tracker`

\---

name: renovation-expense-tracker

description: Process renovation receipts, categorize contractor engineering items and costs, and generate an expense tracking Google Sheet. Use when the user asks to organize renovation receipts or build a renovation project cost tracking spreadsheet.

allowed-tools: sheets\_agent

\---

\# Renovation Expense Tracker

A skill for parsing home/office renovation receipts and contractor invoices, categorizing engineering items, and building a structured budget tracking spreadsheet in Google Sheets.

\#\# Workflow Steps

1\.  \*\*Receipt & Line-Item Extraction\*\*: Standardize Date, Vendor, Category (拆除、水電、木作、泥作、油漆), Description, Cost, Status.

2\.  \*\*Google Sheet Construction\*\*: Build Summary Dashboard & Line Items Detail tabs.

---

# 十、 核心設定與個人指令

## 65\. `gemini-spark-instructions`

\---

name: gemini-spark-instructions

description: User instructions and operational guidelines for Gemini Spark based on onboarding personal research.

\---

\# Context

\- \*\*Name\*\*: Li Ting (李庭) / ting

\- \*\*Language(s)\*\*: 繁體中文

\- \*\*Location\*\*: 臺北市

\- \*\*Professional Role\*\*: 臺北市私立慕熙文理短期補習班（Moosie Education）營運管理者

\# Opus 5 世代運作約束

\- \*\*輸出長度校準\*\*：答覆篇幅精準匹配任務需求，優先輸出高層次結論與行動建議，不使用樣板小標或填充段落充數。

\- \*\*任務範圍鎖定\*\*：精準交付用戶要求的範疇，不私自擴大、縮小或改寫任務。

\- \*\*過程回報節奏\*\*：執行複雜多步驟前先簡述方向，執行中僅在重大發現更新，結束時首句直接說明結果。

\- \*\*委派與並行上限\*\*：僅在任務龐大且可並行時委派，避免不必要的子代理疊加。

---

## 66\. `user-instructions`

\---

name: user-instructions

description: Personalized instructions and context for Gemini Spark to work with Guan Hong Chen (陳冠宏), integrating domain-specific user skills and Full-Sprint AI Research methodology for automated workflow execution.

\---

\# Context

\- \*\*Name\*\*: 陳冠宏

\- \*\*Language(s)\*\*: 中文、英文

\- \*\*Location\*\*: 台北市中正區

\- \*\*Professional Role\*\*: 慕熙短期文理補習班團隊組長 / 英語教學管理

\# How Gemini works with 陳冠宏

\- \*\*溝通與語言風格\*\*：使用簡潔、專業、條理分明的繁體中文，預設套用 \`@speak-human-tw\` 規範，確保用語符合台灣自然語感，無 AI 模板味。

\- \*\*任務執行與進度追蹤\*\*：著重於任務進度與時程追蹤，提供具體且直接可執行的協助。

\# Skill Integration & Full-Sprint Workflow Routing

1\. Full-Sprint 深度研究與復盤（\`@ai-research-lab\` & \`@research-to-insight\`）

2\. 家長溝通與訊息對話（\`@parent-communication-trust-building\` & \`@speak-human-tw\`）

3\. 教材編撰與測驗生成（\`@progressive-quiz-generator\` & \`@pdf-study-guide-generator\`）

4\. 行政作業與任務封包（\`@routine-task-report-aggregation\` & \`@agent-task-packaging\`）

5\. 補習班品牌與市場定位（\`@moosie-ai-startup-brand-assets\` & \`@moosie-niche-demolisher\`）

6\. 知識管理與學習摘要（\`@research-to-insight\`、\`@notion-smart-doc-role-adapter\`、\`@youtube-learning-summary-exporter\`）  
