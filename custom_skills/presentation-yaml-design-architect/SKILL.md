---
name: presentation-yaml-design-architect
description: Transform presentation topics or draft text into a structured presentation design blueprint in YAML format (PRESENTATION_DESIGN.yaml) specifying global design specs, color schemes, layout rules, page-by-page visual descriptions, and content generation prompts. Use when the user asks to generate presentation design blueprints, YAML slide architectures, or structured presentation visual specs.
---

# Presentation YAML Design Architect

Transforms presentation topics or raw text into a structured, executable presentation design blueprint in YAML format (`PRESENTATION_DESIGN.yaml`).

## When to Use

Use this skill when the user asks to:
- Create a presentation design specification or blueprint in YAML format
- Define global slide design specs (color palette, typography, grid rules, atmosphere)
- Plan page-by-page layout styles, visual descriptions, and content generation prompts for slides

## Workflow

1. **Atmosphere & Tone**: Analyze the topic/content to determine the core atmosphere adjectives and theme.
2. **Global Design Specifications**: Define specific Hex color codes (background, text, accent, secondary), typography recommendations (heading, body, data), and layout/grid rules.
3. **Slide Breakdown & Narrative Flow**: Organize the slide sequence logically (cover, introduction, core concepts, data visualization, conclusion).
4. **Visual Mapping & Prompt Generation**: For each slide (`p1`, `p2`, ...), detail the `type`, `layout_style`, `visual_description`, and content/`generation_prompt`.
5. **YAML Export**: Produce strict, valid YAML code matching the exact schema.

## YAML Output Schema (`PRESENTATION_DESIGN.yaml`)

```yaml
global_design:
  atmosphere: "[3 key adjectives, e.g., Futuristic, Clean, Authoritative]"
  color_scheme:
    background: "[Hex, e.g., #0F172A]"
    text: "[Hex, e.g., #F8FAFC]"
    accent: "[Hex, e.g., #38BDF8]"
    secondary: "[Hex, e.g., #64748B]"
  typography:
    heading: "[Font recommendation, e.g., Inter Bold / Noto Sans TC Bold]"
    body: "[Font recommendation, e.g., Inter Regular / Noto Sans TC Regular]"
    data: "[Font recommendation, e.g., JetBrains Mono]"
  layout_rules:
    navigation: "[Navigation placement, e.g., Top-right progress bar]"
    image_style: ["[Image treatment]", "[Chart style]"]
    layout_design: ["[Grid system]", "[Alignment rules]"]
    decorative_elements: "[Description of accents/decorations]"

slides:
  p1:
    type: "[Slide type, e.g., Cover]"
    layout_style: "[Layout name, e.g., Centered Hero]"
    visual_description: "[Detailed visual composition and graphic elements]"
    content:
      title: "[Title]"
      subtitle: "[Subtitle / Description]"
  p2:
    type: "[Slide type, e.g., Concept Breakdown]"
    layout_style: "[Layout name, e.g., Split 2-Column]"
    visual_description: "[Detailed visual composition and graphic elements]"
    content:
      title: "[Title]"
      generation_prompt: "[Detailed content generation prompt]"
  # Extend p3, p4, etc., as needed
```

## Scope & Boundaries

- **In Scope**: Generating complete YAML blueprints, defining Hex colors, font categories, visual composition descriptions, and content generation prompts.
- **Out of Scope**: Generating actual image binary files, generating full presentation scripts, or exporting directly to PPTX/Keynote binary formats.

## Gotchas

- Strictly preserve the YAML keys (`global_design`, `atmosphere`, `color_scheme`, `typography`, `layout_rules`, `slides`).
- Provide concrete Hex color codes rather than vague color names.

## 標準執行契約

### 觸發與輸入

使用者明確要求「presentation-yaml-design-architect」的核心任務，或輸入與本技能描述高度相符時才啟用。先確認目標、受眾、上下文、資料來源、授權、限制條件與希望的輸出格式；未提供的資訊不得自行補成事實。

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

目前風險等級：**low**。預設可先產出分析或草稿，但仍不得代替使用者做外部高影響決策。本匯入版本為 `instruction_only`，不代表已授權任何外部連接或寫入適配器。

- 先確認任務目標、輸入來源、使用授權、範圍與輸出格式；缺少關鍵資訊時先列出假設並提出最少必要問題。
- 不得捏造事實、數據、案例、評價、客戶反饋、媒體報導、認證或研究來源；無法驗證的內容必須標示為假設或待驗證。
- 只使用使用者提供或明確授權的內容；不得繞過登入、CAPTCHA、付費牆、存取控制或第三方服務限制。
- 外部服務一律採唯讀或草稿模式；發送、發佈、建立、更新、刪除、部署、交易、預算變更與權限變更前必須取得明確人工批准。

- 不得用於未授權存取、憑證收集、冒充他人、垃圾訊息、操縱或規避平台政策。
- 不得把未經授權的第三方內容、個資或機密資料重新發布到公開服務。

## 停止條件

若使用授權、資料來源、範圍、關鍵數字、身份或外部操作權限無法確認，立即停止高影響部分並回報缺口。若發現來源互相矛盾、任務目標漂移、敏感資料暴露、輸出無法驗證或操作不可恢復，保留已完成的安全分析，暫停後續動作並要求人工判斷。

## 關聯技能

本技能與 無 有功能相近或可互補的技能；選擇時以使用者明確需求、資料來源與權限邊界為準，不要平行重複執行相同的高影響操作。

## 來源追蹤

此技能由 `docs/sources/skills_export_20260818.zip` 內的 `presentation-yaml-design-architect/SKILL.md` 正規化而來，來源項目 SHA-256 為 `89a4c5e77ac3e8a4ed42412e6805678320f6e40136ff0d95076d18ba027f9785`，原始行號範圍為 1–70。原始附件已保存於 repository 的 `docs/sources/`，並補上輸入、輸出、權限、安全、人工核准與停止契約。
