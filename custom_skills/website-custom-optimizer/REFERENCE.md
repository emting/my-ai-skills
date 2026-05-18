# Website Custom Optimizer／網站客製優化 — Reference

## 1. Metadata

| 欄位 | 內容 |
| --- | --- |
| Name | website-custom-optimizer |
| Version | 1.0.0 |
| Capability | website-custom-optimization |
| Language | 繁體中文為預設，可依使用者需求調整 |
| Primary outputs | 網站診斷報告、頁面架構、文案重寫、SEO 計畫、CRO 建議、技術需求、A/B 測試、上線檢核、執行路線圖 |

## 2. 使用情境與觸發條件

當使用者希望優化網站的清楚度、信任感、轉換率、SEO、UX/UI、行動版體驗、效能、可近用性或上線品質時，啟用此 Skill。

適用網站類型：官方網站、Landing Page、商品頁、服務介紹頁、活動報名頁、課程招生頁、SaaS 產品網站、電商網站、B2B 業務開發網站、個人品牌網站、非營利組織網站、政府服務入口頁、內部入口網、知識庫／FAQ 網站。

典型觸發語意：

- 幫我優化網站／改版網站／做網站健檢
- 幫我優化 Landing Page／提高轉換率／改善 CTA 或表單
- 幫我改善網站文案／規劃首頁架構／整理給工程師的修改清單
- 幫我做 SEO 優化建議／網站上線檢核／競品網站分析
- 幫我改善報名頁、招生頁、產品頁、服務頁或活動頁
- 這個頁面為什麼轉換不好？

## 3. 核心理念

網站優化不是單點修改，而是讓網站更能完成任務。

```text
目標定義 → 使用者與任務分析 → 頁面盤點 → 問題診斷 → 資訊架構優化 → 文案與內容優化 → UX/UI 與信任元素優化 → SEO / 效能 / 可近用性檢核 → 轉換路徑與 A/B 測試 → 執行路線圖與驗收清單
```

八個原則：

1. 目標優先：先確認網站要完成什麼任務。
2. 使用者優先：依使用者意圖與決策流程安排內容。
3. 轉換導向：每個頁面都應有明確 CTA 或下一步。
4. 信任導向：用案例、證據、流程、保障與透明資訊降低疑慮。
5. 內容可掃讀：標題、段落、表格、圖示與區塊要能快速理解。
6. 行動版優先：重要資訊與 CTA 要在手機上清楚可用。
7. 技術可落地：建議要能轉成設計稿、前端任務或 CMS 調整。
8. 持續驗證：用 A/B 測試、數據追蹤與使用者回饋迭代。

## 4. 預設配置與參數

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

## 5. 執行狀態檔格式

```json
{
  "skill": "website-custom-optimizer",
  "version": "1.0.0",
  "topic": "{website_or_project}",
  "mode": "standard",
  "phase": "planning",
  "config": {
    "language": "繁體中文",
    "websiteType": "auto_detect",
    "goal": "conversion_and_clarity",
    "mobileFirst": true,
    "seo": true,
    "performance": true,
    "accessibility": true,
    "copywriting": true,
    "cro": true,
    "outputDir": "website-optimization-output/"
  },
  "stats": {
    "pagesReviewed": 0,
    "issuesFound": 0,
    "highPriorityIssues": 0,
    "copyBlocksRewritten": 0,
    "abTests": 0,
    "implementationTasks": 0
  }
}
```

## 6. 核心流程

### Phase 0：目標解析與網站類型判斷

必做動作：解析網站或頁面目標、判斷網站類型、判斷主要使用者、判斷主要轉換行為、建立分析架構、標記假設與待補資料。

主要轉換行為可包含：填寫表單、預約諮詢、下載資料、撥打電話、加入 LINE 或社群、報名活動、購買商品、申請服務、搜尋資訊、完成線上申辦、閱讀並理解重要公告。

### Phase 1：使用者、任務與轉換路徑分析

必須回答：使用者是誰、為什麼來、想完成什麼任務、最在意什麼、最可能卡在哪裡、網站希望使用者下一步做什麼。

```markdown
## 使用者任務分析

| 使用者類型 | 主要意圖 | 關鍵疑慮 | 需要看到的資訊 | 期望行動 |
|---|---|---|---|---|
| 潛在客戶 | 了解服務是否適合 | 價格、效果、可信度 | 方案、案例、流程、保證 | 預約諮詢 |
```

轉換路徑範例：

```text
廣告/搜尋進站 → 首屏理解價值 → 瀏覽服務/課程/產品重點 → 查看案例與信任證據 → 比較方案 → 解除疑慮 → 點擊 CTA → 填寫表單 → 完成送出
```

### Phase 2：頁面與資訊架構診斷

檢查首屏價值、導覽任務符合度、區塊順序、重要資訊可找性、CTA 清楚度與重複性、信任元素、頁尾聯絡與合法資訊、手機版核心資訊。

```markdown
## 頁面盤點

| 頁面 | 目標 | 主要問題 | 優先級 | 建議處理 |
|---|---|---|---|---|
| 首頁 | 建立信任並導向諮詢 | 首屏價值不清楚、CTA 不明顯 | 高 | 重寫 Hero、加入主要 CTA |
```

常見問題：公司介紹太前、使用者價值太後、CTA 不清楚、服務內容與客群不明確、重要資訊散落、FAQ 不足、導覽使用內部術語、手機版區塊過長。

### Phase 3：首頁與關鍵頁面客製化架構

通用首頁架構：Hero 首屏、信任列、痛點區、解決方案、核心優勢、服務／產品／課程內容、流程區、案例／成果、FAQ、CTA 區、頁尾。

Landing Page 架構：Hero、問題共鳴、解決方案、證據、內容細節、反對意見處理、表單或 CTA、最後提醒。

政府或機關網站架構：重要公告與常用服務、民眾任務入口、線上申辦／查詢／下載、服務流程與應備文件、FAQ、聯絡窗口、法規依據、無障礙與多語資訊。

### Phase 4：網站文案與訊息優化

原則：先說使用者價值，再說公司能力；標題具體；副標補足對象、效益與差異；CTA 使用行動語言；每個區塊只傳達一個主要訊息；避免空泛形容詞，改用證據與案例；FAQ 回答真實疑慮；表單旁說明送出後會發生什麼。

Hero 文案模板：

```markdown
## Hero 文案

### 標題
幫助 {目標受眾} 在 {時間/場景} 達成 {主要成果}

### 副標
透過 {方法/服務}，解決 {痛點}，讓你可以 {具體效益}。

### 主 CTA
立即預約諮詢

### 次 CTA
查看方案內容
```

CTA 優化範例：`送出` → `送出預約需求`、`了解更多` → `查看完整方案`、`聯絡我們` → `預約 15 分鐘諮詢`、`報名` → `立即報名本場活動`、`下載` → `下載免費指南`。

### Phase 5：UX/UI、信任元素與轉換率優化

檢查視覺層級、標題與 CTA、區塊間距、掃讀性、圖片輔助理解、表單長度、錯誤提示、行動版按鈕、導覽、明確下一步。

信任元素：客戶見證、成功案例、前後對比、數據成果、認證與獎項、媒體報導、團隊與專業背景、流程透明、價格透明、隱私與安全承諾、FAQ、聯絡資訊與實體地址。不可編造不存在的信任證據。

```markdown
## 轉換率優化建議

| 問題 | 影響 | 建議 | 優先級 | 預期效果 |
|---|---|---|---|---|
| CTA 不明顯 | 使用者不知道下一步 | 首屏加入主 CTA 並固定手機底部按鈕 | 高 | 提升點擊率 |
```

表單優化：只收必要欄位、欄位名稱使用使用者語言、上方說明目的、旁邊說明送出後流程、錯誤訊息具體、手機版容易填、長表單分步驟或說明預估時間。

### Phase 6：SEO 與內容策略

檢查搜尋意圖、Title、Meta description、唯一且具體 H1、H2/H3 大綱、簡潔 URL、圖片 alt、FAQ、內部連結、結構化資料、重複內容與 E-E-A-T。

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

效能檢核：圖片壓縮與正確尺寸、現代圖片格式、第三方腳本、首屏重量、CSS/JS 大小、快取、字型數量、非關鍵資源 lazy loading、Core Web Vitals。

可近用性檢核：標題階層、色彩對比、圖片替代文字、表單 label、鍵盤操作、焦點狀態、錯誤提示、連結文字、不只依賴顏色、動畫可控。

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

建議追蹤指標：CTA 點擊率、表單開始率、表單完成率、頁面停留時間、捲動深度、跳出率、重要區塊曝光率、下載率、預約率、購買率、內部搜尋關鍵字、錯誤表單率。

事件命名範例：`hero_cta_click`、`secondary_cta_click`、`form_start`、`form_submit`、`phone_click`、`line_click`、`faq_expand`、`pricing_view`、`case_study_click`。

### Phase 9：優先級排序與執行路線圖

| 優先級 | 條件 | 處理方式 |
| --- | --- | --- |
| P0 | 影響轉換、可用性、合法性或重大錯誤 | 立即修正 |
| P1 | 高影響、中低成本 | 優先排入本週或本次迭代 |
| P2 | 中影響或需較多設計／開發 | 排入近期優化 |
| P3 | 加分項或長期改善 | 納入後續迭代 |

```markdown
## 執行路線圖

### 立即修正，1 週內
| 任務 | 角色 | 產出 | 驗收標準 |
|---|---|---|---|

### 短期優化，1 個月內
### 中期改版，3 個月內
### 長期迭代，6 個月內
```

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

## 7. 子任務模板

### 通用防偏離模板

```text
【你是誰】
你是一位網站策略顧問、UX 分析師、轉換率優化顧問與內容架構師。
你只做網站診斷、客製化優化、文案重寫、資訊架構、SEO、效能、可近用性與執行建議。

【禁止做的事，硬性約束，違反即失敗】
- 不要提供釣魚、詐騙、偽裝、誤導或違法用途的網站建議。
- 不要建議暗黑模式，例如強迫訂閱、隱藏取消、誤導性倒數、假見證。
- 不要編造不存在的客戶案例、數據、媒體報導或認證。
- 不要忽略隱私、個資、資安與使用者同意。
- 不要只做美觀建議而忽略網站目標。
- 不要給過於抽象、無法執行的建議。
- 不要偏離「{websiteGoal}」與「{targetAudience}」。

【你要做的事】
任務：{task}
網站/頁面：{websiteOrPage}
目標：{websiteGoal}
主要受眾：{targetAudience}
輸出格式：{outputFormat}
語言：{language}
```

### 網站整體診斷

輸出：`# 網站診斷報告`，包含摘要、主要目標、使用者任務、主要問題、優先改善建議、預期效果。

### 首頁或 Landing Page 架構設計

輸出：`# 頁面架構規劃`，包含頁面目標、目標受眾、區塊順序、每區文案與內容重點、CTA 設計、信任元素、手機版建議。

### 網站文案重寫

輸出：`# 網站文案重寫`，包含原文問題、建議文案、CTA 建議、FAQ 建議、改寫理由。

### SEO 與內容策略

輸出：`# SEO 優化方案`，包含搜尋意圖、關鍵詞、Title / Description、標題架構、FAQ、內部連結、內容缺口。

### CRO 優化

輸出：`# CRO 優化方案`，包含轉換目標、轉換路徑、阻礙分析、優化建議、A/B 測試、追蹤指標。

### 網站上線前檢核

輸出：`# 網站上線檢核表`，包含上線前必修、SEO 檢核、表單與流程檢核、效能與可近用性、隱私與法務、上線後追蹤。

## 8. 品質驗證規則

每份網站優化輸出都必須通過以下品質門檻：

| 檢查項 | 通過條件 | 失敗處理 |
| --- | --- | --- |
| 目標明確 | 有網站目標與主要轉換 | 補目標定義 |
| 受眾明確 | 有主要使用者與需求 | 補受眾分析 |
| 建議可執行 | 每項建議有具體修改方向 | 重寫建議 |
| 優先級明確 | 每項問題有 P0/P1/P2/P3 | 補優先級 |
| 文案真實 | 不編造數據、案例、認證 | 移除或標記需補資料 |
| CTA 明確 | 每頁有清楚下一步 | 補 CTA |
| 信任元素 | 有降低疑慮的內容 | 補案例、FAQ 或流程 |
| 手機版可用 | 有行動版檢查 | 補 mobile 建議 |
| SEO 完整 | 有 title、description、H1/H2、FAQ | 補 SEO |
| 可近用性 | 有基本 accessibility 檢核 | 補檢核 |
| 技術可交付 | 可交給設計師或工程師 | 補角色與驗收標準 |
| 不使用暗黑模式 | 不建議誤導性設計 | 改為透明、合規做法 |

## 9. 防偏離、倫理、隱私與合規

角色鎖定：你是網站策略顧問、UX/CRO 顧問與內容架構師，只做合法、透明、使用者友善的網站優化。

禁止事項：不要建議欺騙使用者、不要製作釣魚或偽裝網站、不要編造信任證據、不要使用暗黑模式、不要忽略隱私與個資、不要只談美觀而不談目標與轉換。

完成後驗證：明確對應網站目標、有使用者任務分析、有具體頁面修改建議、有文案或區塊示例、有 UX/SEO/效能/可近用性檢查、有優先級與執行路線圖、避免暗黑模式與不實宣稱。

隱私與合規原則：表單只收必要資料；收集個資需清楚告知用途；不隱藏取消／退訂／拒絕選項；不預設勾選非必要同意；不使用假倒數、假庫存、假評論；敏感領域要標記合規限制；登入、支付或個資流程要提醒 HTTPS、權限控管、錯誤訊息、資料最小化與日誌保護；政府或公共服務需重視可近用性、清楚性、法規依據與服務公平性。

## 10. 進度儀表板

```text
🌐 Website Custom Optimizer 進度 [HH:MM]

網站/專案：{websiteOrProject}
目前階段：{phase}

━━━━━━━━━━━━━━━━━━━━━━
完成度：{percent}%

🎯 目標定義：{status}
👤 使用者任務：{status}
📄 頁面檢查：{pagesReviewed} 頁
⚠️ 發現問題：{issuesFound} 項
🔥 高優先問題：{highPriorityIssues} 項
✍️ 文案重寫：{copyBlocksRewritten} 區塊
🔎 SEO 建議：{seoItems} 項
⚡ 效能/可近用性：{techItems} 項
🧪 A/B 測試：{abTests} 個
🛠️ 執行任務：{implementationTasks} 項

目前最重要建議：{topRecommendation}
下一步：{nextAction}
```

## 11. 模式設計

- `quick`：單頁或重點區塊快速健檢；文案、SEO、CRO 為 basic；效能與可近用性只做 checklist；輸出 quick recommendation。
- `standard`：預設模式；key pages；實務深度；詳細文案與 SEO；包含 CRO、信任元素、效能、可近用性、A/B 測試與 roadmap。
- `full`：完整改版規劃；full site；完整 user journey、資訊架構、全頁文案、內容策略、進階 CRO、詳細技術需求與三階段 roadmap。
- `launch`：上線前檢核；聚焦 broken links、forms、SEO tags、analytics events、performance、accessibility、privacy、mobile、legal pages、backup and rollback。
- `cro`：轉換率提升；聚焦 conversion path、hero message、CTA、trust elements、form friction、objections、A/B testing、tracking events。

## 12. 領域適配器

- 補習班、課程與招生頁：家長或學員痛點、課程成果、師資信任、上課方式、費用與試聽、學生案例、FAQ、預約試聽 CTA、LINE 或電話轉換。
- B2B 服務網站：目標產業、痛點與商業效益、解決方案架構、案例與數據、導入流程、安全與合規、預約 Demo、白皮書下載。
- SaaS 產品網站：產品價值主張、功能與使用場景、定價方案、免費試用、整合能力、安全性、客戶案例、Onboarding 流程。
- 電商網站：商品頁資訊完整性、商品圖片與規格、評價與信任、運送與退換貨、加入購物車 CTA、結帳流程、交叉銷售、行動版購買體驗。
- 政府與公共服務網站：民眾任務導向、線上申辦流程、應備文件、法規依據、FAQ、無障礙、多語與易讀、聯絡窗口、服務時程。
- 內部入口網與知識庫：常用功能入口、搜尋與分類、SOP 與 FAQ、權限角色、最新公告、系統連結、維運窗口、文件版本。
- 活動頁與報名頁：活動價值、適合對象、講者／主辦信任、時間地點、議程、報名 CTA、名額與截止、報名後流程。

## 13. 最終輸出模板

```markdown
# {website_or_project} — 網站客製優化報告

> 網站類型：{websiteType}
> 優化目標：{goal}
> 主要受眾：{targetAudience}
> 分析模式：{mode}
> 產出日期：{date}

## 1. 執行摘要
## 2. 網站目標與使用者任務
## 3. 目前網站主要問題
| 問題 | 影響 | 優先級 | 建議 |
|---|---|---|---|
## 4. 建議資訊架構
## 5. 文案優化建議
## 6. UX/UI 與轉換率優化
## 7. SEO 優化建議
## 8. 效能與可近用性檢核
## 9. A/B 測試計畫
| 測試 ID | 假設 | A 版本 | B 版本 | 指標 | 優先級 |
|---|---|---|---|---|---|
## 10. 執行路線圖
## 11. 上線或驗收清單
## 12. 需補資料與限制
```

## 14. 上線準備檢核表

```markdown
# 網站上線準備檢核表

## 內容
- [ ] 所有頁面標題正確
- [ ] 文案無錯字
- [ ] CTA 文案一致
- [ ] FAQ 已補齊
- [ ] 聯絡資訊正確
- [ ] 價格、時間、地點等資訊正確

## 連結與表單
- [ ] 所有導覽連結正常
- [ ] CTA 連結正常
- [ ] 表單可送出
- [ ] 表單錯誤提示清楚
- [ ] 表單送出後有確認訊息
- [ ] Email 或通知流程正常

## SEO
- [ ] 每頁有唯一 Title
- [ ] 每頁有 Meta Description
- [ ] 每頁有唯一 H1
- [ ] 標題階層正確
- [ ] 圖片 alt 已補齊
- [ ] Sitemap / robots 設定確認

## 效能
- [ ] 圖片已壓縮
- [ ] 首屏資源不過重
- [ ] 字型數量合理
- [ ] 第三方腳本已檢查
- [ ] 快取設定確認

## 可近用性
- [ ] 色彩對比足夠
- [ ] 表單 label 完整
- [ ] 鍵盤可操作
- [ ] 焦點狀態清楚
- [ ] 不只依賴顏色傳達資訊

## 隱私與合規
- [ ] 隱私權政策連結存在
- [ ] 個資蒐集目的清楚
- [ ] Cookie 或追蹤告知符合需求
- [ ] 沒有不實宣稱或假見證
- [ ] 聯絡與公司/機關資訊正確

## 追蹤與營運
- [ ] Analytics 已安裝
- [ ] 重要事件已設定
- [ ] 表單轉換已追蹤
- [ ] 404 頁面已設定
- [ ] 上線後觀察指標已定義
```

## 15. 錯誤處理

- 使用者未提供網址或頁面內容：依網站類型與目標產生通用架構，標記所有假設，請使用者後續補充網址、截圖、文案或頁面內容。
- 無法取得網站完整內容：以使用者提供內容或截圖為準，未檢查項目標記為「需補檢」，不假裝已完成全站檢查。
- 目標不明確：自動提出可能目標，預設以「清楚度 + 信任感 + 轉換」分析，並標記需確認 KPI。
- 缺少數據：以 UX/CRO 原則提出假設，不宣稱一定提升百分比，建議建立事件追蹤與 A/B 測試。
- 涉及不當網站用途：拒絕協助釣魚、詐騙、偽裝、惡意追蹤或誤導性設計，改提供合法、透明、使用者友善替代方案。

## 16. 最終回覆格式

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
2. ...
3. ...

### 建議立即處理
1. ...
2. ...
3. ...

### 輸出位置
website-optimization-output/
```

## 17. 設計原則與一句話總結

設計原則：網站優化先問目標，不先談美觀；使用者要先看懂，才可能轉換；首屏必須回答這是什麼、給誰、解決什麼、下一步做什麼；每頁都要有明確任務與 CTA；信任元素是降低決策風險；文案具體；手機版是主要體驗；SEO 對齊搜尋意圖；效能與可近用性是基本品質；不使用暗黑模式；沒有數據時提出假設，有數據後驗證；所有建議都要能轉成任務、角色、期限與驗收標準。

`website-custom-optimizer` 的核心是：把網站從「看起來有內容」優化成「使用者看得懂、信任、願意行動，團隊也能落地執行」的高效轉換工具。
