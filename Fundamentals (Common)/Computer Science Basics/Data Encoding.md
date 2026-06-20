# Data Encoding

> How computers map numbers to characters — from ASCII to Unicode.

---

## Why Encoding Exists

- Computers store everything as binary (0s and 1s)
- To display text, we need an agreed **mapping** between numbers and characters
- That agreed mapping is called an **encoding**
- Without a shared encoding, the same bits get interpreted as different characters → **gibberish**

> **Representation** = data lives as bits in memory. **Encoding** = the specific mapping that gives those bits meaning (e.g., `65` → `A`).

---

## ASCII

**American Standard Code for Information Interchange** — created in 1963.

- Uses **7 bits** → `0–127` (128 characters)
- Covers: English letters, digits, punctuation, and control characters
- Each character gets a unique number (its **code point**)

### Key Ranges

| Range   | Characters    | Decimal  | Hex         |
| ------- | ------------- | -------- | ----------- |
| Digits  | `0`–`9`       | 48–57    | `30`–`39`   |
| Upper   | `A`–`Z`       | 65–90    | `41`–`5A`   |
| Lower   | `a`–`z`       | 97–122   | `61`–`7A`   |
| Space   | ` `           | 32       | `20`        |

### Anchor Values (Memorize These)

| Char | Decimal |
| ---- | ------- |
| `0`  | 48      |
| `A`  | 65      |
| `a`  | 97      |

- Letters and digits are **sequential** — knowing one gives you the rest (`B` = 66, `C` = 67, …)
- Difference between uppercase and lowercase = **32** (`A` = 65, `a` = 97)

### Example: "TryHackMe" in ASCII

| Char | `T` | `r`  | `y`  | `H` | `a`  | `c`  | `k`  | `M` | `e`  |
| ---- | --- | ---- | ---- | --- | ---- | ---- | ---- | --- | ---- |
| Hex  | 54  | 72   | 79   | 48  | 61   | 63   | 6B   | 4D  | 65   |

Stored on disk (binary):
```
01010100 01110010 01111001 01001000 01100001 01100011 01101011 01001101 01100101
```

Hex view: `54 72 79 48 61 63 6b 4d 65`

> When your editor opens this file, it reads the bytes and maps them back to characters using ASCII. That's encoding in action.

### ASCII Limitations

- Only supports **English** — cannot represent Hindi, Chinese, Arabic, emojis, etc.
- 128 characters is far too few for the world's writing systems
- ASCII is **frozen** — it has not been updated since its creation

---

## Extended ASCII

- Uses **8 bits** → `0–255` (256 characters)
- First 128 values = **same as ASCII** (backward compatible)
- Extra 128 values = additional European characters

### The Problem: Competing Standards

Multiple **ISO-8859** standards were created, each covering different language groups:

| Standard          | Covers                        | Example Characters   |
| ----------------- | ----------------------------- | -------------------- |
| **ISO-8859-1** (Latin-1) | Western European (German, French, Spanish, Nordic) | `ß`, `ü`, `é`, `ñ` |
| **ISO-8859-2** (Latin-2) | Central/Eastern European (Polish, Czech, Hungarian) | `ł`, `č`, `ř`, `ő` |

- Same byte value → **different character** depending on which standard is used
- A file saved as ISO-8859-1 and opened as ISO-8859-2 will show wrong characters
- This fragmentation is why Extended ASCII was ultimately insufficient

---

## Unicode

The **universal character set** — one standard to cover all writing systems.

- Assigns a unique **code point** to every character in every language
- Format: `U+XXXX` (e.g., `U+0041` = `A`, `U+1F600` = 😀)
- Currently defines **150,000+** characters across 160+ scripts
- **Includes ASCII** — the first 128 Unicode code points are identical to ASCII

> Unicode is **not** an encoding itself — it's a character catalog. The actual encoding (how code points become bytes) is handled by **UTF** formats.

---

## UTF Encodings

UTF = **Unicode Transformation Format** — the way Unicode code points are stored as bytes.

### UTF-8 (Most Common)

- **Variable length**: 1 to 4 bytes per character
- **Backward compatible with ASCII** — ASCII characters use exactly 1 byte with the same values
- **Dominant on the web** — used by ~98% of websites

| Character Type      | Bytes Used | Example              |
| ------------------- | ---------- | -------------------- |
| ASCII (English)     | 1 byte     | `A` → `41`           |
| European accented   | 2 bytes    | `é` → `C3 A9`        |
| Asian scripts       | 3 bytes    | `中` → `E4 B8 AD`    |
| Emojis              | 4 bytes    | `😀` → `F0 9F 98 80` |

How it's declared on the web:
```html
<meta charset="UTF-8">
```

### UTF-16

- **Variable length**: 2 or 4 bytes per character
- Most common characters use **2 bytes**
- Used internally by **Windows** and **Java**
- **Not** backward compatible with ASCII

### UTF-32

- **Fixed length**: always **4 bytes** per character
- Simplest to process (constant width) but wastes the most space
- Rarely used for storage or transmission

### Comparison

| Feature             | UTF-8        | UTF-16       | UTF-32       |
| ------------------- | ------------ | ------------ | ------------ |
| Bytes per character  | 1–4          | 2–4          | 4 (fixed)    |
| ASCII compatible     | ✅ Yes       | ❌ No        | ❌ No        |
| Space-efficient for English | ✅ Best | ❌ Wasteful  | ❌ Most wasteful |
| Space-efficient for Asian   | ❌ 3 bytes | ✅ 2 bytes  | ❌ 4 bytes   |
| Web standard         | ✅ Dominant  | ❌ Rare      | ❌ Rare      |
| Used by              | Web, Linux, modern apps | Windows, Java | Internal processing |

### Why UTF-8 Won

1. **Backward compatible** with ASCII — old systems still work
2. **Space-efficient** for English/Latin text (most of the web)
3. **No byte-order issues** (unlike UTF-16/32 which need BOM markers)
4. **Self-synchronizing** — can detect character boundaries from any position

---

## Mojibake (Garbled Text)

When text is decoded with the **wrong encoding**, characters appear as gibberish — this is called **mojibake**.

**Common causes:**
- File saved in one encoding, opened with another
- Web page missing or incorrect `charset` declaration
- Copy-paste between systems with different default encodings

**Example:** A file saved as ISO-8859-1 containing `café` might display as `cafÃ©` when opened as UTF-8.

> If you ever see `Ã©`, `Ã¶`, `Â£` — that's usually UTF-8 bytes being misread as Latin-1.

---

## Quick Reference

| Concept                     | Value          |
| --------------------------- | -------------- |
| ASCII range                 | 0–127 (7 bits) |
| Extended ASCII range        | 0–255 (8 bits) |
| `A` in ASCII                | 65 / `0x41`    |
| `a` in ASCII                | 97 / `0x61`    |
| `0` in ASCII                | 48 / `0x30`    |
| Upper ↔ Lower difference    | 32             |
| UTF-8 bytes for ASCII chars | 1              |
| UTF-8 bytes for emojis      | 4              |

---

## The Scale Problem

English needs only **52** letter characters (upper + lower). Other languages need far more:

| Language | Characters Needed | Standard          |
| -------- | ----------------- | ----------------- |
| Arabic   | 250+              | Ligatures + diacritics |
| Japanese | 6,879             | JIS X 0208        |
| Chinese  | 87,887+           | GB 18030-2022     |

Extended ASCII's 256 slots and fragmented regional standards couldn't handle this → need a **universal** system.

> Encoding mismatch example: `Ø` saved in ISO-8859-1 appears as `Ř` when opened in ISO-8859-2 — same byte, different mapping.

---

## Unicode (Deep Dive)

- **Universal character set** — one code point per character, across all languages
- Format: `U+XXXX` (hex code point)
- Latest version: **Unicode 17.0** — ~157,000 characters, ~4,000 emoji sequences
- First 128 code points = **identical to ASCII**
- Sender and receiver both use Unicode → no encoding mismatch

| Code Point  | Character | Script            |
| ----------- | --------- | ----------------- |
| `U+0041`    | A         | Latin             |
| `U+03A9`    | Ω         | Greek             |
| `U+3042`    | あ        | Japanese Hiragana |
| `U+9F8D`    | 龍        | Chinese (dragon)  |
| `U+062A`    | ت         | Arabic (taa)      |
| `U+30C4`    | ツ        | Japanese (tsu)    |
| `U+265E`    | ♞         | Chess black knight |
| `U+1F60A`   | 😊        | Emoji             |

> Unicode is the **character catalog**. UTF encodings define how those code points become actual bytes.

---

## UTF Encodings (Deep Dive)

### UTF-8

- **Variable length**: 1–4 bytes per character
- ASCII range (`U+0000`–`U+007F`) → **1 byte**, identical to ASCII
- European/Arabic (`U+0080`–`U+07FF`) → **2 bytes** (e.g., `Ω`)
- Asian scripts (`U+0800`–`U+FFFF`) → **3 bytes**
- Emoji/rare scripts (`U+10000`+) → **4 bytes** (e.g., 🔥 `U+1F525`)

### UTF-16

- **Variable length**: 2 or 4 bytes per character
- Most common characters (Latin, Cyrillic, Chinese Hanzi) → **2 bytes**
- Emoji and rare scripts → **4 bytes** (surrogate pair: two 16-bit units)
- Example: `A` = `U+0041` (2 bytes), 🔥 = `U+D83D U+DD25` (4 bytes)
- Used internally by **Windows** and **Java**

---

## How Emoji Rendering Works

The emoji code point (e.g., `U+1F60A`) is **not** an image — it's just a number. The actual graphic comes from the **rendering pipeline**:

```
Code point → OS lookup → Emoji font → GPU renders graphic
```

1. Computer reads the code point (`U+1F60A`)
2. OS looks it up in the system's **emoji font**
3. Font returns a **vector/bitmap graphic** for that code point
4. GPU renders it on screen


### Emoji Fonts by Platform

| Platform | Emoji Font          |
| -------- | ------------------- |
| Apple    | Apple Color Emoji   |
| Android  | Noto Color Emoji    |
| Windows  | Segoe UI Emoji      |

### Why Emojis Look Different Across Devices

- The **Unicode Consortium** defines the code point and a **text description** (e.g., `U+1F60A` = "smiling face with smiling eyes")
- Each company (Apple, Google, Microsoft) **designs their own artwork** for that description
- Same code point → different visual design

> Emoji are not stored as images. The number is a lookup key — the font provides the drawing.
