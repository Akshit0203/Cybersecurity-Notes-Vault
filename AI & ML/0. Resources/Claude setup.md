# Claude Code Setup

## 1. Install the CLI

**macOS, Linux, WSL:**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell:**

```powershell
irm https://claude.ai/install.ps1 | iex
```

**Windows CMD:**

```cmd
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

## 2. Verify the Installation

When the installer finishes, open a **new** terminal window and run:

```bash
claude --version
```

> [!warning] PATH error
> If the command isn't recognized, add the install directory to your PATH (Windows CMD):
>
> ```cmd
> set PATH=%PATH%;C:\Users\<username>\.local\bin
> claude --version
> ```

> [!note] Why the error comes back in every new terminal
> `set PATH=...` only changes the PATH for **that one CMD window**. Every new terminal needs it again, so add it to your **permanent User PATH** instead.

### Permanent Fix (Windows GUI)

1. Press **Win + R**
2. Type `sysdm.cpl` and press **Enter**
3. Go to **Advanced → Environment Variables**
4. Under **User variables for \<username\>**, select **Path**
5. Click **Edit → New**
6. Add exactly:

	```
	C:\Users\<username>\.local\bin
	```

7. Click **OK → OK → OK**
8. **Close every** CMD / PowerShell / Windows Terminal window
9. Open a **new** terminal and run:

	```bash
	claude --version
	```

It should now work permanently.

## 3. Start Claude in a Project

Navigate to the required folder:

```bash
cd <folder path>
```

Launch Claude:

```bash
claude
```

## 4. Configure the Session

| Command   | Purpose                  |
| --------- | ------------------------ |
| `/model`  | Choose the model         |
| `/effort` | Set the reasoning effort |

## 5. Update Claude Code

```bash
claude update
```

## 6. Modes

Press **Shift + Tab** to cycle between modes:

- **Manual mode** – asks before making changes
- **Accept edits** – applies file edits automatically
- **Plan mode** – plans first, no changes made
- **Auto mode** – works autonomously

> [!tip]
> It's recommended to start with **planning first**, then move on to execution.

## 7. Useful Commands

| Command   | Purpose                                                                           |
| --------- | --------------------------------------------------------------------------------- |
| `/clear`  | Clear the conversation and start fresh                                            |
| `/rewind` | Go back to a previous point in the conversation (use **↑**, then press **Enter**) |
| `/help`   | Press **Enter**, open the **commands** tab, and scroll with the **arrow keys**    |
| `/plan`   | Plan first, then do the thinking / execution                                      |

## 8. Project Files

| File        | Purpose                                                |
| ----------- | ------------------------------------------------------ |
| `CLAUDE.md` | Add instructions for Claude                            |
| `prompt.md` | Store a prompt you want to reuse                       |

To make Claude read a file, reference it with `@`:

```
@prompt.md
```

## 9. Tips

- **Screenshots:** take a screenshot (e.g. of a UI), paste it into Claude Code, and ask for changes.
- **Queue prompts:** you can type several prompts one after another; Claude processes them one by one.
- **Agents:** you can set up multiple agents inside Claude Code.
- **GitHub integration:** link with GitHub to automatically review and push code.

## 10. Install the VS Code Extension

Open VS Code, go to **Extensions** and search for:

```
Claude Code
```

Install the **official Anthropic Claude Code extension**.

## 11. Sign In with Your Claude Pro Account

Open Claude Code from VS Code.

When it asks you to authenticate, choose your **Claude account/subscription** and sign in using the **same account that has your Claude Pro subscription**.

Your Pro subscription covers Claude Code, including its supported IDE integrations.

![](attachments/Pasted%20image%2020261006181615.png)

![](attachments/Pasted%20image%2020261006181637.png)

![](attachments/Pasted%20image%2020261006181649.png)

![](attachments/Pasted%20image%2020261006181747.png)

![](attachments/Pasted%20image%2020261006181843.png)

![](attachments/Pasted%20image%2020261006181908.png)

![](attachments/Pasted%20image%2020261006182002.png)

![](attachments/Pasted%20image%2020261006182019.png)

