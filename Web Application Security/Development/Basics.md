# Web Development Basics

> Core concepts of how the web works — before writing any code.

---

## The Web Technology Stack

### Frontend (what the user sees)

| Technology     | Role                | Example                                    |
| -------------- | ------------------- | ------------------------------------------ |
| **HTML**       | Structure / content | Headings, paragraphs, buttons, forms       |
| **CSS**        | Styling / layout    | Colors, fonts, spacing, responsive design  |
| **JavaScript** | Interactivity       | Button clicks, form validation, animations |

CSS frameworks: **Bootstrap**, **Tailwind CSS**  
JS frameworks: **React**, **Vue**, **Angular**

### Backend (what runs on the server)

| Technology    | Role                    | Example                            |
| ------------- | ----------------------- | ---------------------------------- |
| **Node.js**   | JS runtime for servers  | Express.js web server              |
| **Python**    | General-purpose backend | Django, Flask                      |
| **Databases** | Store and retrieve data | SQL (MySQL, PostgreSQL), MongoDB   |

> Full stack = frontend + backend + database.

---

## HTTP (How Client and Server Communicate)

**HyperText Transfer Protocol** — the language browsers and servers speak.

### HTTP Methods

| Method     | Purpose                | Example                         |
| ---------- | ---------------------- | ------------------------------- |
| **GET**    | Retrieve data          | Load a webpage, fetch user list |
| **POST**   | Send/create data       | Submit a form, create an account |
| **PUT**    | Update existing data   | Edit a profile                  |
| **DELETE** | Remove data            | Delete a post                   |

### HTTP Status Codes

| Code | Meaning               | When You See It                    |
| ---- | --------------------- | ---------------------------------- |
| 200  | OK                    | Page loaded successfully           |
| 301  | Moved Permanently     | URL redirect                       |
| 403  | Forbidden             | No permission to access            |
| 404  | Not Found             | Page doesn't exist                 |
| 500  | Internal Server Error | Server crashed / bug               |

### HTTP vs HTTPS

- **HTTP** — data sent in plain text (anyone can read it)
- **HTTPS** — data is **encrypted** using TLS/SSL (secure)
- The `S` = **Secure** — always look for the 🔒 in the address bar

---

## Web Standards Bodies

Standards ensure the same code works the same way across all browsers.

### The Major Organizations

| Organization           | Full Name                               | Defines                               |
| ---------------------- | --------------------------------------- | ------------------------------------- |
| **W3C**                | World Wide Web Consortium               | HTML, CSS, accessibility (WCAG), SVG  |
| **WHATWG**             | Web Hypertext Application Technology Working Group | Living HTML standard (actively updated) |
| **ECMA International** | European Computer Manufacturers Association | JavaScript language spec (ECMAScript) |
| **IETF**               | Internet Engineering Task Force         | HTTP, TLS/SSL, DNS, TCP/IP protocols  |
| **IANA**               | Internet Assigned Numbers Authority     | Domain names, IP addresses, port numbers |

### W3C vs WHATWG

- **W3C** originally maintained the HTML spec with **versioned releases** (HTML4, XHTML, HTML5)
- **WHATWG** (founded by Apple, Mozilla, Opera in 2004) disagreed with W3C's direction and created a **"living standard"** — continuously updated, no version numbers
- In 2019, W3C and WHATWG agreed: **WHATWG's living standard is the official HTML spec**
- W3C now focuses on **CSS, accessibility (WCAG), and web APIs**

### How a Web Feature Becomes a Standard

A new feature (e.g., CSS Grid, `fetch()` API) doesn't appear overnight:

| Stage        | What Happens                                              |
| ------------ | --------------------------------------------------------- |
| **Proposal** | Someone submits an idea (often a browser vendor)          |
| **Draft**    | Spec is written, reviewed, and debated                    |
| **Implementation** | Browser vendors build experimental support (behind flags) |
| **Testing**  | Web developers test and provide feedback                  |
| **Standard** | Officially adopted — all browsers should implement it     |

> This process can take **years**. CSS Grid was proposed in 2011 and widely supported by 2017.

### Who Has the Real Power?

These bodies **don't control** the web — they define **guidelines everyone agrees to follow**.

The actual power is shared:

| Entity                | Role                                               |
| --------------------- | -------------------------------------------------- |
| **Standards bodies**  | Write the rules                                    |
| **Browser vendors**   | Choose to implement them (Google, Apple, Mozilla, Microsoft) |
| **Developers**        | Build with them, report bugs, influence direction  |

- Browser vendors **choose** to follow standards so websites work everywhere
- If any browser broke standards → websites break → users leave → market share lost
- Even Google (with ~65% browser market share) **must follow standards** — otherwise the open web breaks

### What Standards Define (Examples)

| Standard    | Rule                                              |
| ----------- | ------------------------------------------------- |
| HTML        | `<h1>` must render as a large heading             |
| HTML        | `<input type="password">` must hide characters    |
| CSS         | `color: red` must show red text everywhere        |
| JavaScript  | `2 + 2` must equal `4` in every engine            |
| Browser API | `fetch()` must handle network requests            |
| Security    | Same-Origin Policy prevents cross-site data theft |

### What Happens Without Standards (Real Examples)

- **Internet Explorer era (2000s)** — IE ignored many standards, used its own proprietary features → developers had to write separate code for IE vs other browsers → massive pain
- **Vendor prefixes** — before a CSS feature is standardized, browsers use prefixes like `-webkit-`, `-moz-` → code like `-webkit-border-radius` only works in Chrome/Safari
- **Encoding chaos** — before Unicode became standard, different encodings (ISO-8859-1 vs Windows-1252) caused garbled text across systems

> "Standards exist because everyone benefits from compatibility."

---

## Developer Tools (DevTools)

Every modern browser has built-in developer tools (`F12` or `Ctrl+Shift+I`):

| Tab          | What It Does                                  |
| ------------ | --------------------------------------------- |
| **Elements** | Inspect and edit HTML/CSS live                 |
| **Console**  | Run JavaScript, see errors and logs            |
| **Network**  | See all HTTP requests (URLs, status codes, timing) |
| **Sources**  | View and debug JavaScript files                |
| **Application** | Inspect cookies, local storage, sessions    |

> DevTools is your most important debugging tool — learn it early.
