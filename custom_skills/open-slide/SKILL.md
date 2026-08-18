---
name: open-slide
description: Create, draft, edit, and manage web-native React presentations using the open-slide framework. Use when the user requests creating slides, building presentation decks with React/open-slide, editing slide components, or exporting open-slide presentations.
---

# Open Slide

Framework and authoring guide for building agent-native React slide decks with open-slide.

## Summary

`open-slide` is an open-source, React-based presentation framework built specifically for AI agents and developer-centric workflows. Presentations in open-slide are written as standard React components rendering on a fixed 1920 × 1080 canvas, with automatic scaling, hot reloading, present mode, and in-browser inspection comments.

## When to Use

Use this skill when:
- Creating a new presentation deck or slide project using `open-slide`
- Writing or editing React slide components under `slides/<deck-id>/index.tsx`
- Structuring slide layouts, typography, color palettes, or animations for 1920 × 1080 slides
- Applying in-browser inspector comments (`@slide-comment`) to slide code
- Exporting open-slide decks to static HTML or PDF format

---

## Core Principles & Canvas Contract

1. **Fixed Canvas Resolution**: Every page renders inside a `1920 × 1080` pixel viewport.
2. **React Page Architecture**: Decks are standard React applications. Slides default-export an array of `Page` components.
3. **No DSL Constraints**: Authors can use standard HTML, CSS, Tailwind CSS, Lucide icons, Framer Motion, and SVGs.
4. **Hot Reload & Presenter Mode**: Includes live preview, speaker notes, preview of upcoming slides, and keyboard navigation.

---

## Workflow Steps

### Step 1: Initialize Deck
To create a new slide workspace:
```bash
npx @open-slide/cli init <deck-name>
cd <deck-name>
pnpm dev
```

### Step 2: Deck Scoping & Structure
Before writing slide code, establish:
- **Topic & Audience**: Target domain and visual tone (e.g., modern tech, minimalist, dark mode, corporate).
- **Page Count & Density**: Total slides (typically 5–15 pages) and text density per slide.
- **Color Palette & Typography**:
  - Primary, background, text, and accent colors
  - Consistent type scale suited for 1920 × 1080 canvas (e.g., Title: 48px–72px, Body: 20px–28px).

### Step 3: Slide Component Authoring
Slide files reside under `slides/<deck-id>/index.tsx`.

```tsx
import React from 'react';

export const Slide1 = () => (
  <div className="w-[1920px] h-[1080px] bg-slate-900 text-white flex flex-col justify-center items-center p-16">
    <h1 className="text-6xl font-bold mb-6 text-blue-400">Open Slide Title</h1>
    <p className="text-2xl text-slate-300 max-w-3xl text-center">
      Agent-native presentation framework built on React.
    </p>
  </div>
);

export const Slide2 = () => (
  <div className="w-[1920px] h-[1080px] bg-slate-900 text-white p-16 flex flex-col justify-between">
    <h2 className="text-4xl font-semibold text-blue-400">Key Features</h2>
    <div className="grid grid-cols-3 gap-8 my-auto">
      <div className="bg-slate-800 p-8 rounded-xl border border-slate-700">
        <h3 className="text-2xl font-bold mb-4">React Native</h3>
        <p className="text-slate-300">Full power of React and Tailwind CSS.</p>
      </div>
      <div className="bg-slate-800 p-8 rounded-xl border border-slate-700">
        <h3 className="text-2xl font-bold mb-4">Agent Driven</h3>
        <p className="text-slate-300">Designed for natural language generation.</p>
      </div>
      <div className="bg-slate-800 p-8 rounded-xl border border-slate-700">
        <h3 className="text-2xl font-bold mb-4">Inspector & Export</h3>
        <p className="text-slate-300">In-browser comments & instant PDF export.</p>
      </div>
    </div>
  </div>
);

export default [Slide1, Slide2];
```

### Step 4: In-Browser Comments & Edits
Use the dev server inspector to leave `@slide-comment` markers on elements, then update slide components accordingly:
- Read comment markers in `slides/<deck-id>/index.tsx`.
- Apply requested changes (e.g., adjust font size, change color, update layout).
- Remove completed comment markers.

### Step 5: Exporting & Publishing
Build and export presentations:
- **Static Build**: `pnpm build`
- **PDF Export**: Export present mode views via static site or Playwright screenshot script.

---

## Best Practices & Gotchas

- **Always maintain 1920 × 1080 proportions**: Use explicit width (`1920px`) and height (`1080px`) or full-container flex/grid bounds to prevent content clipping.
- **Readable Type Contrast**: Ensure text contrast ratios meet accessibility standards on dark or light backgrounds.
- **Modular Component Design**: Break complex slide diagrams or charts into reusable React components.
- **Avoid Content Overflow**: Keep text concise per slide to maintain visual balance on large screens.

## 標準執行契約

### 觸發與輸入

使用者明確要求「open-slide」的核心任務，或輸入與本技能描述高度相符時才啟用。先確認目標、受眾、上下文、資料來源、授權、限制條件與希望的輸出格式；未提供的資訊不得自行補成事實。

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
- 涉及外部資料時記錄來源、擷取時間與查證限制；將可觀察事實、推論與建議分開呈現。
- 本技能只提供分析、草稿與驗證建議；涉及高影響決策或外部操作時，必須由適當的人員在執行前覆核。

- 不得用於未授權存取、憑證收集、冒充他人、垃圾訊息、操縱或規避平台政策。
- 不得把未經授權的第三方內容、個資或機密資料重新發布到公開服務。

## 停止條件

若使用授權、資料來源、範圍、關鍵數字、身份或外部操作權限無法確認，立即停止高影響部分並回報缺口。若發現來源互相矛盾、任務目標漂移、敏感資料暴露、輸出無法驗證或操作不可恢復，保留已完成的安全分析，暫停後續動作並要求人工判斷。

## 關聯技能

本技能與 `presentation-structure-visual-script`、`presentation-yaml-design-architect` 有功能相近或可互補的技能；選擇時以使用者明確需求、資料來源與權限邊界為準，不要平行重複執行相同的高影響操作。

## 來源追蹤

此技能由 `docs/sources/skills_export_20260818.zip` 內的 `open-slide/SKILL.md` 正規化而來，來源項目 SHA-256 為 `46bd95857016624d92cdd46524be8ba6652504cfdc78675f9249c12465354e1a`，原始行號範圍為 1–108。原始附件已保存於 repository 的 `docs/sources/`，並補上輸入、輸出、權限、安全、人工核准與停止契約。
