# Data Representation

> How computers represent numbers and colors.

---

## Why Number Systems Exist

- Humans use **decimal (base 10)** — likely because we have 10 fingers
- Computers only understand **binary (base 2)** — hardware has two states:
  - High/Low voltage (transistors)
  - North/South polarity (hard drives)
  - Light presence/absence (fiber optics)
- **Octal & Hex** exist as human-readable shortcuts for binary

| System      | Base | Digits  | Used For                        |
| ----------- | ---- | ------- | ------------------------------- |
| Decimal     | 10   | `0`–`9` | Daily life                      |
| Binary      | 2    | `0`–`1` | CPU, memory, hardware           |
| Octal       | 8    | `0`–`7` | Linux permissions (`chmod 755`) |
| Hexadecimal | 16   | `0`–`F` | Colors, memory addresses        |

> **"Base"** = how many digits a system uses. After the last digit, you carry over (e.g., base 10: after `9` → `10`).

### What If We Used a Different Base?

Nothing physical would change — only how humans write numbers. It's like switching languages, not reality.

| Base   | Daily Life Impact                                    | Example: decimal `255` |
| ------ | ---------------------------------------------------- | ---------------------- |
| Binary | Everything becomes very long, impractical for humans | `11111111`             |
| Octal  | Slightly different counting, still manageable        | `377`                  |
| Hex    | Shorter numbers, but requires memorizing A–F         | `FF`                   |

- **Binary world** — age `21` becomes `10101`, phone numbers are absurdly long
- **Octal world** — already used in Linux permissions (`chmod 777`)
- **Hex world** — actually quite efficient, just needs A–F memorization
- **Decimal won** — best balance for humans (10 fingers → base 10)

> Number systems are just representation tools. Same value, different form. The world wouldn't change — only how we write and think about numbers.

---

## Bits & Bytes

- **Bit** — smallest unit, either `0` or `1`
- **Byte (Octet)** — group of 8 bits
- Each added bit **doubles** the possibilities: `2ⁿ`

| Bits | Values |
| ---- | ------ |
| 1    | 2      |
| 2    | 4      |
| 3    | 8      |
| 4    | 16     |
| 5    | 32     |
| 6    | 64     |
| 7    | 128    |
| 8    | 256    |

> **Why doubling?** Each bit is an independent ON/OFF switch. Adding one switch doubles all prior combinations.

---

## How Positional Number Systems Work

Every number system works the same way — each position = `baseⁿ`

**Decimal example:** `345` = `3×10² + 4×10¹ + 5×10⁰` = `300 + 40 + 5`

**Binary example:** `1011` = `1×2³ + 0×2² + 1×2¹ + 1×2⁰` = `8 + 0 + 2 + 1` = `11`

---

## Conversions

### Binary → Decimal

Write place values, keep only where bit = `1`, add them up.

```
Place values:  128  64  32  16  8  4  2  1
```

| Binary     | Calculation      | Decimal |
| ---------- | ---------------- | ------- |
| `1011`     | 8 + 2 + 1        | 11      |
| `1001`     | 8 + 1            | 9       |
| `1100`     | 8 + 4            | 12      |
| `1111`     | 8 + 4 + 2 + 1    | 15      |
| `10100011` | 128 + 32 + 2 + 1 | 163     |

---

### Decimal → Binary

**Method 1 — Divide by 2**, read remainders bottom to top:

| Step   | Quotient | Remainder |
| ------ | -------- | --------- |
| 13 ÷ 2 | 6        | 1         |
| 6 ÷ 2  | 3        | 0         |
| 3 ÷ 2  | 1        | 1         |
| 1 ÷ 2  | 0        | 1         |

→ Read bottom to top: `1101`

**Method 2 — Break into powers of 2** (faster with practice):

`13 = 8 + 4 + 1` → place `1` at positions 8, 4, 1 → `1101`

---

### Binary ↔ Octal

Group binary in **3 bits** (right to left), convert each group.

| Binary → Octal  | Octal → Binary                           |
| --------------- | ---------------------------------------- |
| `110 101` → `65` | `6` → `110`, `5` → `101` → `110101` |

| Octal | Binary |
| ----- | ------ |
| `0`   | `000`  |
| `1`   | `001`  |
| `2`   | `010`  |
| `3`   | `011`  |
| `4`   | `100`  |
| `5`   | `101`  |
| `6`   | `110`  |
| `7`   | `111`  |

---

### Binary ↔ Hexadecimal

Group binary in **4 bits** (right to left), convert each group.

| Binary → Hex       | Hex → Binary                               |
| ------------------ | ------------------------------------------ |
| `1010 1111` → `AF` | `A` → `1010`, `F` → `1111` → `10101111` |

| Hex | Binary | Hex | Binary |
| --- | ------ | --- | ------ |
| `0` | `0000` | `8` | `1000` |
| `1` | `0001` | `9` | `1001` |
| `2` | `0010` | `A` | `1010` |
| `3` | `0011` | `B` | `1011` |
| `4` | `0100` | `C` | `1100` |
| `5` | `0101` | `D` | `1101` |
| `6` | `0110` | `E` | `1110` |
| `7` | `0111` | `F` | `1111` |

---

### Hex → Decimal

Same positional approach, using powers of 16.

| Hex    | Calculation                       | Decimal |
| ------ | --------------------------------- | ------- |
| `AB`   | `10×16 + 11×1`                    | 171     |
| `A3`   | `10×16 + 3×1`                     | 163     |
| `9BDF` | `9×4096 + 11×256 + 13×16 + 15×1` | 39,903  |

### Octal → Decimal

| Octal | Calculation        | Decimal |
| ----- | ------------------ | ------- |
| `357` | `3×64 + 5×8 + 7×1` | 239     |

---

## RGB Color Model

- Colors = combination of **Red, Green, and Blue** light
- Each channel can be **on (1)** or **off (0)**

### 3-Bit Color (8 Colors)

`2 × 2 × 2 = 8` possible colors

| Binary | Meaning      | Color   |
| ------ | ------------ | ------- |
| `000`  | All off      | Black   |
| `001`  | Blue only    | Blue    |
| `010`  | Green only   | Green   |
| `100`  | Red only     | Red     |
| `011`  | Green + Blue | Cyan    |
| `101`  | Red + Blue   | Magenta |
| `110`  | Red + Green  | Yellow  |
| `111`  | All on       | White   |

### 24-Bit Color (16 Million Colors)

- **8 bits (1 byte)** per channel → 256 intensity levels (0–255)
- `256 × 256 × 256` = **16,777,216** colors
- One color = **3 bytes (24 bits)**

> **Why multiply?** For every red value, you can combine ALL green values × ALL blue values. Combinations explode.

### Color Format: `#RRGGBB`

Each byte → 2 hex digits → total 6 hex digits per color

| Format  | Value                        |
| ------- | ---------------------------- |
| Binary  | `10100011 11101010 00101010` |
| Hex     | `#A3EA2A`                    |
| Decimal | `(163, 234, 42)`             |
| Color   | Green                        |

Common RGB values:

| RGB              | Color |
| ---------------- | ----- |
| `(0, 0, 0)`      | Black |
| `(255, 0, 0)`    | Red   |
| `(0, 255, 0)`    | Green |
| `(0, 0, 255)`    | Blue  |
| `(255, 255, 255)` | White |

---

## Linux Permissions (Octal in Practice)

Permissions have 3 groups: **User**, **Group**, **Others**

Each group has 3 bits: `r` (read), `w` (write), `x` (execute)

| Permission | Binary | Octal Value |
| ---------- | ------ | ----------- |
| `rwx`      | `111`  | 7           |
| `rw-`      | `110`  | 6           |
| `r-x`      | `101`  | 5           |
| `r--`      | `100`  | 4           |
| `---`      | `000`  | 0           |

`chmod 755` → User: `rwx`, Group: `r-x`, Others: `r-x`

> Octal fits perfectly here because each permission group = exactly 3 bits.

---

## Quick Reference

| Concept                | Value       |
| ---------------------- | ----------- |
| Bits per color channel | 8           |
| Bytes per color        | 3 (24 bits) |
| Total colors (24-bit)  | 16,777,216  |
| Hex digits per byte    | 2           |
| Hex digits per color   | 6           |
| `#FFFFFF` in decimal   | 16,777,215  |
| `0xAB` in decimal      | 171         |