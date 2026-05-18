# Website Custom Optimizer／網站客製優化

## 定位

Website Custom Optimizer 是網站策略顧問、UX/CRO 顧問與內容架構師。它依據網站目標與主要受眾，對官方網站、Landing Page、活動頁、產品頁、服務頁、內部入口網或知識庫進行客製化診斷，並產出可交給設計、工程、SEO、行銷與業務團隊執行的優化方案。

## 檔案結構

- `SKILL.md`：Agent 載入時使用的核心操作指令與觸發條件。
- `REFERENCE.md`：完整技能規格，包含參數、狀態檔、十階段流程、子任務模板、品質驗證規則、進度儀表板、模式設計、領域適配器、上線準備檢核表與錯誤處理。
- `manifest.json`：機器可讀的技能 metadata、輸入輸出、權限與安全規則。

## Metadata

| 欄位 | 內容 |
| --- | --- |
| Name | website-custom-optimizer |
| Version | 1.0.0 |
| Capability | website-custom-optimization |
| Language | 繁體中文為預設，可依使用者需求調整 |
| Primary outputs | 網站診斷報告、頁面架構、文案重寫、SEO 計畫、CRO 建議、技術需求、A/B 測試、上線檢核、執行路線圖 |

## 使用情境

當使用者希望優化網站的清楚度、信任感、轉換率、SEO、UX/UI、行動版體驗、效能、可近用性或上線品質時，啟用此 skill。

適用網站類型包含官方網站、Landing Page、商品頁、服務介紹頁、活動報名頁、課程招生頁、SaaS 產品網站、電商網站、B2B 業務開發網站、個人品牌網站、非營利組織網站、政府服務入口頁、內部入口網、知識庫／FAQ 網站。

典型任務：網站健檢與改版規劃、Landing Page 轉換率優化、首頁架構設計、網站文案重寫、SEO 與內容策略、表單／報名／預約流程改善、手機版體驗優化、上線前檢核、競品網站分析，以及產出給設計師、前端工程師、SEO、行銷與業務的需求文件。

## 核心理念

網站優化不是單點修改，而是讓網站更能完成任務。

```text
目標定義 → 使用者與任務分析 → 頁面盤點 → 問題診斷 → 資訊架構優化 → 文案與內容優化 → UX/UI 與信任元素優化 → SEO / 效能 / 可近用性檢核 → 轉換路徑與 A/B 測試 → 執行路線圖與驗收清單
```

八個原則：目標優先、使用者優先、轉換導向、信任導向、內容可掃讀、行動版優先、技術可落地、持續驗證。

## 預設配置

```yaml
mode: standard
language: Traditional Chinese
website_type: auto_detect
goal: conversion_and_clarity
pages_scope: key_pages
analysis_depth: practical
seo: true
performance: true
accessibility: true
mobile_first: true
conversion_rate_optimization: true
copywriting: true
information_architecture: true
trust_elements: true
ab_testing_plan: true
implementation_roadmap: true
quality_gate: strict
output_directory: website-optimization-output/
```

## 參數

| 參數 | 預設值 | 範圍 | 說明 |
| --- | --- | --- | --- |
| 網站類型 | auto_detect | official / landing / ecommerce / saas / gov / content / custom | 網站或頁面類型 |
| 目標 | conversion_and_clarity | conversion / seo / trust / usability / performance / accessibility / branding | 主要優化目標 |
| 受眾 | auto_detect | 字串 | 主要使用者或客群 |
| 頁面範圍 | key_pages | single_page / key_pages / full_site | 分析範圍 |
| 模式 | standard | quick / standard / full / launch / cro | 分析深度 |
| SEO | true | true / false | 是否產生 SEO 建議 |
| 文案優化 | true | true / false | 是否重寫頁面文案 |
| A/B 測試 | true | true / false | 是否產生測試假設 |

## 核心流程

### Phase 0：目標解析與網站類型判斷

確認網站任務、主要受眾、商業或服務目標與頁面範圍。判斷主要轉換行為，例如填寫表單、預約諮詢、下載資料、撥打電話、加入 LINE、報名活動、購買商品、申請服務、搜尋資訊、完成線上申辦，或閱讀並理解重要公告。

### Phase 1：使用者、任務與轉換路徑分析

回答使用者是誰、為什麼來、想完成什麼任務、最在意什麼、最可能卡在哪裡，以及網站希望使用者下一步做什麼。

```markdown
## 使用者任務分析

| 使用者類型 | 主要意圖 | 關鍵疑慮 | 需要看到的資訊 | 期望行動 |
|---|---|---|---|---|
| 潛在客戶 | 了解服務是否適合 | 價格、效果、可信度 | 方案、案例、流程、保證 | 預約諮詢 |
```

### Phase 2：頁面與資訊架構診斷

檢查首屏是否清楚說明價值、導覽是否符合使用者任務、區塊順序是否合理、重要資訊是否容易找到、CTA 是否清楚且重複出現、是否有足夠信任元素、頁尾是否提供必要聯絡與合法資訊、手機版是否保留核心資訊。

```markdown
## 頁面盤點

| 頁面 | 目標 | 主要問題 | 優先級 | 建議處理 |
|---|---|---|---|---|
| 首頁 | 建立信任並導向諮詢 | 首屏價值不清楚、CTA 不明顯 | 高 | 重寫 Hero、加入主要 CTA |
```

### Phase 3：首頁與關鍵頁面客製化架構

通用首頁架構：Hero 首屏、信任列、痛點區、解決方案、核心優勢、服務／產品／課程內容、流程區、案例／成果、FAQ、CTA 區與頁尾。

Landing Page 架構：Hero、問題共鳴、解決方案、證據、內容細節、反對意見處理、表單或 CTA、最後提醒。

政府或機關網站架構：重要公告與常用服務、民眾任務入口、線上申辦／查詢／下載、服務流程與應備文件、FAQ、聯絡窗口、法規依據、無障礙與多語資訊。

### Phase 4：網站文案與訊息優化

文案要先說使用者價值，再說公司能力。標題具體、副標補足對象／效益／差異、CTA 使用行動語言、每個區塊只傳達一個主要訊息、避免空泛形容詞，改用證據與案例。表單旁需說明填寫後會發生什麼事。

```markdown
## 文案重寫建議

### 原文
{originalCopy}

### 問題
- 不清楚目標受眾
- 沒有具體效益
- CTA 不明確

### 建議改寫
{rewrittenCopy}

### 改寫理由
1. ...
```

### Phase 5：UX/UI、信任元素與轉換率優化

檢查視覺層級、標題與 CTA、區塊間距、掃讀性、圖片是否支援理解、表單長度、錯誤提示、行動版按鈕、導覽與下一步。信任元素可包含客戶見證、成功案例、前後對比、數據成果、認證與獎項、媒體報導、團隊背景、流程透明、價格透明、隱私與安全承諾、FAQ、聯絡資訊與實體地址。

```markdown
## 轉換率優化建議

| 問題 | 影響 | 建議 | 優先級 | 預期效果 |
|---|---|---|---|---|
| CTA 不明顯 | 使用者不知道下一步 | 首屏加入主 CTA 並固定手機底部按鈕 | 高 | 提升點擊率 |
```

### Phase 6：SEO 與內容策略

檢查搜尋意圖、Title、Meta description、唯一 H1、H2/H3 大綱、URL、圖片 alt、FAQ、內部連結、結構化資料、重複內容與 E-E-A-T。

```markdown
## SEO 建議

### 主要關鍵詞
### 搜尋意圖
### 建議 Title
### 建議 Meta Description
### 建議 H1
### 建議 H2 架構
### FAQ 建議
### 內部連結建議
```

### Phase 7：效能、可近用性與技術檢核

效能檢核包含圖片壓縮與尺寸、現代圖片格式、第三方腳本、首屏重量、CSS/JS、快取、字型、lazy loading 與 Core Web Vitals。可近用性檢核包含標題階層、色彩對比、alt、label、鍵盤操作、焦點狀態、錯誤提示、連結文字、不只依賴顏色與動畫控制。

```markdown
## 技術修改清單

| 項目 | 類型 | 說明 | 優先級 | 負責角色 |
|---|---|---|---|---|
| 圖片壓縮 | 效能 | 首頁 Hero 圖片過大，建議壓縮並提供 WebP | 高 | 前端 |
```

### Phase 8：A/B 測試與數據追蹤計畫

```markdown
## A/B 測試計畫

| 測試 ID | 假設 | A 版本 | B 版本 | 指標 | 預期影響 | 優先級 |
|---|---|---|---|---|---|---|
| AB-001 | 更具體的 Hero 標題可提高 CTA 點擊 | 原標題 | 強調成果的新標題 | CTA CTR | 提升 | 高 |
```

建議事件：`hero_cta_click`、`secondary_cta_click`、`form_start`、`form_submit`、`phone_click`、`line_click`、`faq_expand`、`pricing_view`、`case_study_click`。

### Phase 9：優先級排序與執行路線圖

| 優先級 | 條件 | 處理方式 |
| --- | --- | --- |
| P0 | 影響轉換、可用性、合法性或重大錯誤 | 立即修正 |
| P1 | 高影響、中低成本 | 優先排入本週或本次迭代 |
| P2 | 中影響或需較多設計／開發 | 排入近期優化 |
| P3 | 加分項或長期改善 | 納入後續迭代 |

### Phase 10：最終網站優化包

```text
website-optimization-output/
├── 00_website-optimization-summary.md
├── 01_user-journey-and-conversion-path.md
├── 02_page-audit-report.md
├── 03_information-architecture-plan.md
├── 04_copywriting-rewrite.md
├── 05_cro-and-trust-elements.md
├── 06_seo-plan.md
├── 07_performance-accessibility-checklist.md
├── 08_ab-testing-plan.md
├── 09_implementation-roadmap.md
└── 10_launch-readiness-checklist.md
```

## 子任務模板

- 網站整體診斷：摘要、主要目標、使用者任務、主要問題、優先改善建議、預期效果。
- 首頁或 Landing Page 架構設計：頁面目標、受眾、區塊順序、每區文案與內容重點、CTA、信任元素、手機版建議。
- 網站文案重寫：原文問題、建議文案、CTA、FAQ、改寫理由。
- SEO 與內容策略：搜尋意圖、關鍵詞、Title / Description、標題架構、FAQ、內部連結、內容缺口。
- CRO 優化：轉換目標、轉換路徑、阻礙分析、優化建議、A/B 測試、追蹤指標。
- 上線前檢核：內容、連結、表單、SEO、效能、可近用性、隱私、追蹤碼、上線後 7 日追蹤。

## 品質驗證規則

每份輸出都要確認：目標明確、受眾明確、建議可執行、優先級明確、文案真實、CTA 明確、信任元素完整、手機版可用、SEO 完整、可近用性有檢核、技術可交付、不使用暗黑模式。

## 隱私、資安與合規

表單只收必要資料；收集個資要清楚告知用途；不得隱藏取消／退訂／拒絕選項；不得預設勾選非必要同意；不得使用假倒數、假庫存、假評論。涉及兒少、醫療、金融、法律、政府服務、登入、支付或個資流程時，需標記合規、HTTPS、權限控管、錯誤訊息、資料最小化與日誌保護風險。

## 最終回覆格式

```markdown
## ✅ 網站客製優化完成

網站/專案：{websiteOrProject}

### 產出摘要
- 網站類型：{websiteType}
- 優化目標：{goal}
- 檢查頁面：{pagesReviewed}
- 發現問題：{issuesFound}
- 高優先問題：{highPriorityIssues}
- 文案重寫區塊：{copyBlocksRewritten}
- SEO 建議：{seoItems}
- A/B 測試：{abTests}
- 執行任務：{implementationTasks}

### 最重要的 3 個建議
1. ...

### 建議立即處理
1. ...

### 輸出位置
website-optimization-output/
```

## 一句話總結

`website-custom-optimizer` 的核心是：把網站從「看起來有內容」優化成「使用者看得懂、信任、願意行動，團隊也能落地執行」的高效轉換工具。
