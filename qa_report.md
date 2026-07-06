# QA Report — Darya.ai Platform Prototype
**Date:** 2026-07-02  
**Screens analyzed:** 7 (re-captured via Playwright/Chromium at 1440px wide)  
**Note:** The original shots/configurator|register|payment|launch|console|api.png files in /shots/ are all corrupted — each is a 404 error page rendered as PNG. All analysis below is based on fresh screenshots taken from the HTML source files.

---

## 1. index.html — Landing Page

**Expected:** Hero, live GPU price cards, 3 tariff cards, TCO calculator

### Issues Found

**I-1 · Price cards: missing 4th card content / inconsistent card heights**
The 4th price card ("Трафик egress") has a very different visual weight. Its large "$0" in green/teal is a distinct accent color — but the label text "Без платы за исходящий" wraps inside a small badge that is very close to the card's bottom edge. The badge text is cramped with barely any padding at the bottom. Potential clipping on smaller viewports.

**I-2 · "Трафик egress" badge: low-contrast text**
The green badge inside the 4th price card uses a dark green background with what appears to be a slightly lighter green text ("Без платы за исходящий"). At this size the contrast is borderline — the text is significantly smaller than the other cards' badges and harder to read than "В наличии".

**I-3 · TCO calculator: layout break — two-column split is asymmetric**
The calculator section splits into a left column (sliders) and a right column (price result). The right column floats with a right-aligned card, but the left side's sliders extend edge-to-edge of their column while the right card appears visually heavier. The section label "КАЛЬКУЛЯТОР СТОИМОСТИ" is very small (uppercase tracking, ~10px equivalent) — barely readable against the dark background.

**I-4 · TCO calculator: large blank white space below sliders**
There is a significant empty area at the bottom of the calculator section (below the "Часов в месяц: 720" slider and before the footer). The right column's "Продолжить настройку" button is not vertically centered with the sliders — the entire right card floats to the top, leaving empty space in the lower right of the section. This looks broken.

**I-5 · "Три модели потребления" section: radio button circles visible but unstyled**
The three tariff cards each have a visible radio-button circle in the top-right corner. The unselected ones (On-Demand, Offtake) show bare gray outline circles. These look like unstyled native `<input type="radio">` elements — inconsistent with the design system.

**I-6 · Hero section: missing GPU live-price cards section header**
The 4-card price strip (H200 $5.00, Reserved $4.20, Offtake $3.50, Egress $0) has no heading or label — it appears right below the CTA buttons with no visual separator or context label. A user who scrolls past the hero would not immediately understand what these 4 cards represent.

**I-7 · Stats bar: spacing inconsistency**
The 4-stat bar ("8× H200 / 1128 ГБ / 3.2 Тбит/с / 100% ГЭС") uses non-uniform internal spacing. The stat values use a larger bold font with the units in smaller text, but the gap between the number and unit seems to collapse in the "8× H200" cell compared to the others (looks like "8×" and "H200" have an extra space while the other cells have tighter joins).

**I-8 · Footer: left and right content nearly touching viewport edges**
The footer "ООО «Дарёи санаи марказ» · Душанбе, Таджикистан" on the left and "Устойчивая AI-инфраструктура на «зелёной» гидроэнергии" on the right appear to have very little left/right page margin — they appear to reach very close to (or exactly to) the viewport edge, which is less than the recommended minimum margin.

---

## 2. configurator.html — GPU Configurator

**Expected:** Stepper, GPU picker cards, config dropdowns, sticky cost summary sidebar

### Issues Found

**C-1 · Cost summary sidebar: number spacing broken in "В месяц" line**
The value "$24 192" in the sidebar "В месяц (720 ч)" row has a non-breaking space used as a thousands separator, but it renders as a visible gap wider than expected — "$24 192" looks like two separate numbers at a glance. This is repeated on the index page too. All large monetary values using this pattern should use a narrower thin space or the standard locale format.

**C-2 · Cost summary sidebar: "Продолжить → Регистрация" button — arrow glyph**
The button reads "Продолжить → Регистрация" using a plain ASCII arrow (→). This is stylistically inconsistent with the rest of the UI which uses icon components elsewhere. The arrow also visually breaks the button text flow awkwardly.

**C-3 · Section 4 "Регион и сеть": public IP placeholder text too small**
The "Публичный IP / порты" field has placeholder text "22 (SSH), 8888 (Jupyter), 443" that is noticeably smaller or lighter than the label above it — may be a font-size discrepancy between the input placeholder and the label.

**C-4 · Section 5 "Образ ОС": card grid alignment**
The 4 image template cards (PyTorch 2.4, TensorFlow, vLLM/инференс, Ubuntu 22.04) are in a 4-column row. The "vLLM / инференс" card has a slash with spaces around it ("vLLM / инференс") which breaks the card title into two visual words — inconsistent with "PyTorch 2.4" and "TensorFlow" formatting. Also "LLM serving" subtitle is in English while others are in Russian or have no subtitle.

**C-5 · Stepper: step connector lines barely visible**
The dashed/dotted lines connecting step circles in the stepper ("Тариф ··· Конфигурация ··· Регистрация …") are very low contrast against the dark background. They read more like missing content than intentional connectors.

**C-6 · Page cuts off without bottom padding**
The page ends at section 6 "Имя и параметры инстанса" with the SSH key dropdown partially visible — the page either lacks a bottom CTA or the scroll ends without adequate bottom padding/margin, giving an abrupt cutoff feel.

**C-7 · H100 card "Ограничено" badge: orange badge insufficient contrast**
The orange "Ограничено" badge on the H100 GPU card uses an orange background with white text — this is fine — but the badge font is very small (approximately 10px equivalent) making it hard to read, especially given the font weight appears to be regular, not bold.

---

## 3. register.html — Registration

**Expected:** Stepper, account form, account-type cards, org verification form, order summary sidebar

### Issues Found

**R-1 · Order summary sidebar: "$33.60" — no thousands separator consistency issue (minor)**
Minor: "$33.60" is rendered correctly. However the "В час" label and value have inconsistent vertical rhythm compared to the items above — there is a larger visual gap before this line creating an uneven summary layout.

**R-2 · Section B "Тип аккаунта": radio button on "Частное лицо" card is unstyled native circle**
Same issue as the tariff cards on index.html — the radio input on the left card (Частное лицо) is a visible native gray circle outline in the top-right corner of the card, while the "Организация" card shows a filled blue checkmark. This inconsistency between selected and unselected states is fine for state, but the unstyled native radio circle on the unselected card looks broken compared to the custom checkmark.

**R-3 · Section C "Верификация организации": form label "ИНН / налоговый номер" truncation risk**
The "ИНН / налоговый номер" label is long and placed above a half-width field. On narrower viewports it may wrap awkwardly, though at 1440px it appears fine.

**R-4 · Section C: file upload zone has no visible border/box — blends with card background**
The document upload area ("Перетащите или выберите файлы") has a very subtle dashed border that almost disappears against the dark card background. The upload zone is indistinguishable from empty space unless the user looks carefully.

**R-5 · Section D "Быстрая настройка": spinner/arrow icon color**
The third item "Следующий шаг: добавить способ оплаты" uses a "→" arrow in what appears to be a muted blue-gray, which is noticeably dimmer than the green checkmarks above it. The inconsistency in icon style (checkmark vs arrow) is intentional (in-progress state) but the color contrast of that arrow icon against the card background is low.

**R-6 · "Пропустить →" button in header: mismatch with design system**
The top-right "Пропустить →" button has a visible border/outline style on a dark background — this is fine — but the border color is very faint (barely distinguishable from the background), making the button look ghosted or disabled rather than interactive.

**R-7 · Overall: no visible bottom margin before page end**
The page ends at section D with very little space below the last list item before the page terminates. No footer is present (unlike index.html), which is intentional for wizard flows, but the lack of bottom padding (~0px apparent) makes the bottom feel cut off.

---

## 4. payment.html — Payment

**Expected:** Stepper, 3-way payment toggle, balance top-up form with amount cards, summary sidebar

### Issues Found

**P-1 · Page title says "Два способа оплаты" but toggle shows 3 options**
The heading reads "Два способа оплаты" (Two payment methods) but the toggle immediately below offers three options: "Баланс Darya.ai", "Банковский эквайринг", "Счёт для организации". This is a content error — the heading is factually wrong and contradicts the UI.

**P-2 · Summary sidebar: "$24  192" — double-space / wide thousands separator**
Same issue as configurator: "Оценка/мес (720 ч) $24  192" renders with an excessively wide gap between "24" and "192". Looks like a rendering artifact or incorrect use of `&nbsp;` as thousands separator.

**P-3 · Amount selection cards: inconsistent spacing between radio circle and amount label**
The four amount cards ($50, $500, $2 000, $10 000) each have a radio circle on the right side. The radio circles appear to be native unstyled inputs (same issue as on index/register), visible as bare gray outlines on unselected cards.

**P-4 · "$2 000" and "$10 000" — space-separated thousands look like two words**
The amounts "$2 000" and "$10 000" use a space as the thousands separator, which causes the number to visually appear as two tokens. A non-breaking thin-space or locale-appropriate format (e.g. "$2,000") would be less ambiguous.

**P-5 · Card input fields: "Срок / CVC" label combines two fields in one label**
The card expiry and CVC share a single label "Срок / CVC" but are a single input field. This is a UX issue — the user sees one input but the label implies two fields. Either split into two inputs or use a combined placeholder.

**P-6 · "Лимит расходов" section: "$80/ч" input field — the "/ч" suffix is inside the input**
The spending limit field shows "$80/ч" as the current value. The "/ч" unit suffix appearing inside the text input field rather than as an external unit label is problematic — a user editing the field may accidentally delete the "/ч" suffix, and it's unclear whether the field accepts just the number or the full string.

**P-7 · Summary sidebar: "Egress $0" — "$0" is in green but other values are white**
"Egress $0.00" uses a green color for the value, which is appropriate as a highlight, but it creates visual inconsistency with "$33.60/ч", "$24 192", and "Баланс" which are all white/neutral. A neutral zero-value display would be more consistent.

**P-8 · Stepper: Step 4 "Оплата" circle has a different visual weight**
The active step circle for "Оплата" uses a filled blue circle with white "4", while the completed steps show blue circles with checkmarks. These look similar enough to potentially confuse which step is current vs completed at small sizes.

---

## 5. launch.html — Launch / Instance Running

**Expected:** Console with sidebar, running instance status stepper, SSH/API access cards with code blocks, live monitoring sidebar

### Issues Found

**L-1 · Sidebar navigation: no visual divider between "РЕСУРСЫ", "РАЗРАБОТКА", "АККАУНТ" sections**
The sidebar groups ("РЕСУРСЫ", "РАЗРАБОТКА", "АККАУНТ") are separated only by the section label text in small caps. There is no horizontal rule or spacing between the last item of one group and the label of the next — "Мониторинг" and "+ Новый инстанс" flow directly into "РАЗРАБОТКА" with only the label differentiating them. The gap is insufficient (visually ~4–6px equivalent).

**L-2 · Sidebar: "АККАУНТ" group items — "Биллинг · Баланс" uses a dot separator inside a nav link**
"Биллинг · Баланс" uses a middle dot as a separator within a single navigation item. This looks like two items forced into one link, which is ambiguous — does clicking it go to Billing, Balance, or both?

**L-3 · Main content area: no top-left page margin**
The main content area starts with "ШАГ 5 · ЗАПУСК И ДОСТУП" label flush against the content edge with only ~20px from the sidebar border. On the right side, the monitoring sidebar extends all the way to the viewport right edge with similarly minimal margin. The page feels cramped horizontally.

**L-4 · Status stepper: "Running" step — checkmark icon is a hollow circle instead of filled**
The final "Running" step in the instance status stepper uses a hollow checkmark circle (✓ inside a thin ring) rather than a solid filled circle like the previous three steps. This visual inconsistency makes "Running" appear less "complete" than the preceding steps.

**L-5 · SSH code block: code touches block edges**
The SSH command block ("ssh root@dyu1.darya.ai -p 22001 -i ~/.ssh/id_ed25519") has the text appearing very close to the left edge of the code block container — the left padding appears to be ~8px or less, which is tight for a code block. There is no copy button visible for the SSH command, which is expected UX for such a block.

**L-6 · API access card: code block line wrapping**
The `curl` command in the REST API code block wraps correctly using backslashes (`\`), but the third line `-d '{"gpu":"H200","count":8,"image":"pytorch-2.4","region":"tj-dyu-1"}'` is very long and appears to be close to overflowing the code block width. At exactly 1440px it fits, but at smaller viewports it will overflow.

**L-7 · "Доступ к инстансу" card: three action buttons crowded**
The three buttons "Открыть JupyterLab", "Open in VS Code", "Endpoint инференса" are displayed in a horizontal row. "Open in VS Code" mixes English ("Open in VS Code") while the other two are Russian. Inconsistent language. The button row also has no bottom margin before the card edge.

**L-8 · Monitoring sidebar: "Осталось на баланса" — grammatical error**
The sidebar label reads "Осталось на баланса" which is grammatically incorrect in Russian. It should be "Осталось на балансе" (locative case). This is a text content bug.

**L-9 · Monitoring sidebar: progress bars for GPU load and VRAM are nearly full but identical in color**
Both "Загрузка GPU 94%" and "Память VRAM 128/141 ГБ" progress bars use the same electric blue color at near-full fill. At a glance they are indistinguishable from each other. A subtle color distinction (e.g., warning amber for VRAM at 91% capacity) would aid quick reading.

---

## 6. console.html — Console Overview

**Expected:** Console with sidebar, 4 KPI cards, instances table, usage chart SVG, billing card

### Issues Found

**K-1 · Sidebar: same issues as launch.html**
"Биллинг · Баланс" dot-separator nav item (see L-2), section labels with insufficient gap (see L-1). Identical sidebar component — bugs carry over.

**K-2 · KPI cards: "$412" (Расход сегодня) — no thousands formatting**
The value "$412" is fine, but the note below it "Reserved $4.20/ч" is dark-muted text on a dark card background — the contrast is borderline. Similarly "из 16 в резерве" below "12" in the GPU card is very low contrast muted gray text.

**K-3 · Instances table: "ДЕЙСТВИЯ" column — "Старт" button on stopped instance uses same style as "Открыть"**
The "Старт" button for the stopped "darya-sd-test" instance and the "Открыть" buttons for running instances use the same outlined gray button style. There is no visual differentiation between a primary action ("Start a stopped instance") and a secondary action ("Open running instance"). A stopped instance's "Старт" should be more prominent.

**K-4 · Instances table: column header "$/Ч" — inconsistent capitalization**
Column headers are "ИМЯ", "GPU", "РЕГИОН", "СТАТУС", "ВРЕМЯ", "$/Ч", "ДЕЙСТВИЯ" — all caps except the mixed "$/Ч" where the "Ч" is uppercase Cyrillic and "$/" is symbol. This is a minor but noticeable consistency issue. The "ДЕЙСТВИЯ" header appears to be right-aligned over left-aligned button content.

**K-5 · Billing card: "$11  240" and "$23  900" — same double-space thousands issue**
"Расход за месяц $11 240" and "Прогноз до конца мес. $23 900" use the same too-wide space separator. Consistent with the global formatting bug but worth flagging explicitly here as well.

**K-6 · Usage chart: Y-axis labels missing**
The "Загрузка GPU · 24 часа" chart SVG has X-axis time labels (00:00, 06:00, 12:00, 18:00, сейчас) but no Y-axis labels. The chart has no percentage scale, making it impossible to read actual GPU load values from the chart. The chart title says "GPU загрузка" but the Y-axis context is absent.

**K-7 · Billing card and chart: bottom alignment mismatch**
The billing card on the right ends significantly higher than the bottom of the chart on the left — the two-column bottom section is uneven. The billing card is shorter, leaving blank dark space below the card buttons ("Пополнить", "Счёт PDF") before the row ends.

**K-8 · "Мониторинг" nav item is active (highlighted) but we are on the Console/Overview page**
The sidebar shows "Мониторинг" highlighted in blue as the active nav item, but the page heading says "Консоль / Обзор". The active nav state is incorrect — it should be highlighting the "Инстансы" or a dedicated "Обзор" item.

---

## 7. api.html — API Keys & Access

**Expected:** Console with sidebar, API keys table, CLI/Terraform code blocks, API logs table, capabilities sidebar

### Issues Found

**A-1 · Sidebar: same issues as launch/console (L-1, L-2)**
Section gap and "Биллинг · Баланс" dot-separator issues.

**A-2 · "Быстрый старт" section label and "Terraform" label: inconsistent styling**
"CLI — установка и запуск" is a muted subtitle under "Быстрый старт", rendered in small gray text. "Terraform" appears directly below the CLI code block as a standalone label — same text size and weight as "Быстрый старт" heading, which is confusing. "Terraform" should be a sub-heading visually distinct from "Быстрый старт", or both CLI and Terraform should be sub-sections under it.

**A-3 · CLI code block: line `--image pytorch-2.4 --region tj-dyu-1` is the longest line and wraps**
At 1440px the CLI block fits, but the last line (`--image pytorch-2.4 --region tj-dyu-1`) runs very close to the right edge of the code block. On standard 1280px displays this will overflow or cause horizontal scroll inside the code block without `overflow-x: auto`.

**A-4 · Terraform code block: inconsistent column alignment of `=` signs**
The Terraform block aligns the `=` signs:
```
gpu    = "H200"
count  = 8
image  = "pytorch-2.4"
region = "tj-dyu-1"
```
The spacing before `=` uses varying numbers of spaces, which looks intentional for alignment. However "count = 8" has no quotes while the others have string values — this is correct HCL syntax, but visually the mixed quoted/unquoted values draw the eye and may look like an error to non-Terraform users.

**A-5 · API log table: "ЭНДПОИНТ" column — values not aligned with header**
The "ЭНДПОИНТ" column header appears center-left aligned, while the values "/v1/instances", "/v1/billing/balance" are left-aligned. The column has noticeably more space than needed — the "КОД" column to its right (with short "201"/"200" values and colored badges) is narrow, creating a very unbalanced table with ЭНДПОИНТ taking ~40% of the table width.

**A-6 · Capabilities sidebar: "Webhooks (события биллинга / инстансов)" — wraps awkwardly**
This sidebar item wraps mid-word onto a second line, with "(событий биллинга / инстансов)" on the second line. The parenthetical wraps at an unnatural point, making the item feel truncated. The sidebar is wide enough that slightly smaller font or adjusted padding would prevent the wrap.

**A-7 · "Приватная сеть" sidebar section: description text is very small and low contrast**
The description "VPN SonicWall · InfiniBand NDR между GPU · изолированные VLAN на клиента." uses a very small font (~11px equivalent) in muted gray on dark background — likely fails WCAG AA contrast minimum. This text appears to be purely decorative at this size.

**A-8 · API keys table: "ИСПОЛЬЗОВАН" column — "2 мин назад" and "1 ч назад" are left-aligned but column header appears to extend further right**
The "ИСПОЛЬЗОВАН" header is the widest column header text, but the values underneath ("2 мин назад", "1 ч назад") are short and left-aligned, leaving a large gap between the value and the action column. A right-align on this column would be more readable.

---

## Cross-Screen / Global Issues

**G-1 · Thousands separator: "$24 192", "$11 240", "$23 900" — wide space rendering**
Appears on index (TCO), configurator (sidebar), console (billing), payment (summary). All large monetary values use a plain space or `&nbsp;` as a thousands separator. This renders as a visually wide gap that makes numbers look broken. Should use a narrow no-break space (U+202F) or locale formatting.

**G-2 · Sidebar "Биллинг · Баланс" navigation item — appears on launch, console, api screens**
This item uses a middle dot to combine two navigation destinations into one link. Ambiguous interaction target. Should either be two separate items or a single item with a clear label.

**G-3 · Native radio/checkbox inputs visible on multiple screens**
On index.html (tariff cards), register.html (account type), and payment.html (amount cards), unstyled native radio button circles are visible in card corners. These are not custom-styled and break the design system consistency.

**G-4 · "Open in VS Code" — English string in Russian UI (launch.html)**
One button on the launch screen uses English. All other action text is Russian. Should be "Открыть в VS Code" or "Открыть в Visual Studio Code".

**G-5 · Original screenshots in /shots/ directory (configurator, register, payment, launch, console, api) are all corrupted — each is a 30,718-byte PNG of a "404 The requested path could not be found" white error page. Only index.png was captured correctly. All 6 files need to be regenerated.**
