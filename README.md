# 🚀 Smart File Organizer Agent v2.0

An intelligent file automation system that automatically organizes downloaded files into structured folders in real-time.

---

## ✨ Version 2.0 Improvements

- 🔥 Fixed Chrome download temporary file issue (`.crdownload`, `.com.google.Chrome.*`)
- ⏳ Added file stability detection before processing
- 🧹 Improved watchdog event handling reliability
- ⚡ Safer real-time file classification
- 📁 Auto-organizes files into categories:
  - Documents
  - Images
  - Archives
  - Others

---

## 🧠 How It Works

1. Watches download folder in real-time
2. Detects new file creation
3. Filters temporary/incomplete downloads
4. Waits until file is fully downloaded
5. Classifies file type
6. Moves file into correct folder

---

## ⚙️ Tech Stack

- Python
- Watchdog
- OS Module
- Custom File Classifier

---

## 🚀 Run Project

```bash
python main.py