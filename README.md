---

# 📁 ASCII Project Structure Builder

*A tiny Python utility that converts an LLM-generated ASCII folder tree into real folders and files.*

This script takes a visual ASCII project tree — the kind large language models often output — and automatically creates the actual directory and file structure on disk.

Useful for quickly scaffolding new projects, prototyping ideas, or turning AI-generated structures into real codebases without manually clicking around.

---

## 🚀 Features

* **Parses common ASCII/Unicode tree outputs**
  Supports characters like `│`, `├`, `└`, `─`, and typical indentation.

* **Automatically creates directories and files**
  Files are detected when a name contains a dot (`index.js`, `README.md`, etc.).

* **Flexible depth detection**
  Uses a heuristic based on indentation width rather than strict character matching.

* **No dependencies**
  Pure Python — works out of the box.

---

## 📦 Example Input

Paste something like this:

```
dnd-survivors-frontend/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── ClassSelection.js
│   │   ├── Enemy.js
│   │   └── Player.js
│   ├── hooks/
│   │   └── usePlayerInput.js
│   ├── App.js
│   ├── index.css
│   └── index.js
└── package.json
```

The script will recreate this exact structure on disk.

---

## 🛠️ How It Works

The script:

1. Reads your multiline ASCII tree.
2. Determines the root folder name.
3. Walks each line, computing depth based on indentation and box-drawing characters.
4. Creates directories or empty files accordingly.

The core logic is in:

```python
create_project_structure(structure_text: str)
```

Just pass in any tree text and run it.

---

## 📥 Installation

Clone this repo or download/copy paste the .py file and you’re good to go:

No external packages required.

---

## ▶️ Usage

1. Open `create_structure.py`.
2. Paste your project tree into the `project_hierarchy` variable.
3. Run:

```bash
python create_structure.py
```

You'll see output like:

```
Creating root directory: dnd-survivors-frontend
Creating directory: ...
Creating file: ...
```

When it completes:

```
✅ Project structure created successfully!
```

---

## 🧩 Tips

* Works best with standard “tree”-style LLM outputs (ChatGPT, Claude, etc.).
* Make sure the root directory line ends with a `/`.
* If a file doesn't have an extension (e.g., `LICENSE`), the script will treat it as a directory — you can adjust the heuristic if needed.

---

## 📝 License

MIT — free to use, modify, and enjoy.

---

