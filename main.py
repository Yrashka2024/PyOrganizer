import os
import shutil
import tkinter as tk
from tkinter import messagebox

# Категории и расширения
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Archives": [".zip", ".rar", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Others": []
}

# Путь к рабочему столу
TARGET_DIR = os.path.expanduser("~/Desktop")  # Рабочий стол

# Функции создания папок, определения категории и перемещения файлов
def create_folders(base_path):
    for folder in CATEGORIES:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)

def get_category(extension):
    for category, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_folder(path):
    print(f"🔍 Organizing: {path}")
    create_folders(path)
    files_moved = 0

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            _, ext = os.path.splitext(item)
            category = get_category(ext)
            destination = os.path.join(path, category, item)
            shutil.move(item_path, destination)
            print(f"✅ Moved: {item} → {category}/")
            files_moved += 1

    print(f"\n🎉 Done! Total files moved: {files_moved}")
    messagebox.showinfo("Done", f"Total files moved: {files_moved}")

# Главная функция
def select_folder():
    if os.path.exists(TARGET_DIR):
        organize_folder(TARGET_DIR)
    else:
        messagebox.showerror("Error", "Desktop not found! Check the path.")

if __name__ == "__main__":
    select_folder()
