import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

class SortyApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Sorty - Archive Photos and Videos')

        # Create a button to select the SD card folder
        self.select_button = tk.Button(root, text='Select SD Card Folder', command=self.select_folder)
        self.select_button.pack(pady=20)

        # Create a label to show selected folder
        self.folder_label = tk.Label(root, text='No folder selected')
        self.folder_label.pack(pady=10)

        # Archive button
        self.archive_button = tk.Button(root, text='Archive Files', command=self.archive_files)
        self.archive_button.pack(pady=20)

    def select_folder(self):
        self.folder_selected = filedialog.askdirectory()
        if self.folder_selected:
            self.folder_label.config(text=self.folder_selected)

    def archive_files(self):
        if not hasattr(self, 'folder_selected') or not self.folder_selected:
            messagebox.showerror('Error', 'Please select a folder first.')
            return

        archive_folder = os.path.join(self.folder_selected, 'Archived')
        os.makedirs(archive_folder, exist_ok=True)

        # Example of archiving photos and videos
        for filename in os.listdir(self.folder_selected):
            if filename.endswith(('.jpg', '.png', '.mp4', '.avi')):
                file_path = os.path.join(self.folder_selected, filename)
                shutil.move(file_path, archive_folder)

        messagebox.showinfo('Success', 'Files have been archived.')

if __name__ == '__main__':
    root = tk.Tk()
    app = SortyApp(root)
    root.mainloop()