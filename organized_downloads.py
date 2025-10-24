import os
import shutil
from pathlib import Path

def get_downloads_path():
    """Get the path to the user's Downloads folder."""
    return str(Path.home() / 'Downloads')

def create_directories(downloads_path):
    """Create directories for different file types if they don't exist."""
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
        'Audio': ['.mp3', '.wav', '.ogg', '.m4a', '.flac'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv'],
        'Executables': ['.exe', '.msi', '.dmg', '.pkg', '.deb', '.app'],
        'Code': ['.py', '.js', '.html', '.css', '.java', '.c', '.cpp', '.h', '.json', '.xml'],
        'Spreadsheets': ['.csv', '.xls', '.xlsx', '.ods'],
        'Presentations': ['.ppt', '.pptx', '.odp'],
    }
    
    # Create directories
    for folder in categories.keys():
        os.makedirs(os.path.join(downloads_path, folder), exist_ok=True)
    
    return categories

def organize_downloads():
    """Organize files in the Downloads folder into appropriate subdirectories."""
    downloads_path = get_downloads_path()
    categories = create_directories(downloads_path)
    
    # Get all files in Downloads
    for filename in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, filename)
        
        # Skip directories and hidden files
        if os.path.isdir(file_path) or filename.startswith('.'):
            continue
            
        # Get file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        
        # Find the right category
        moved = False
        for category, extensions in categories.items():
            if ext in extensions:
                dest = os.path.join(downloads_path, category, filename)
                try:
                    shutil.move(file_path, dest)
                    print(f"Moved: {filename} -> {category}/")
                    moved = True
                    break
                except Exception as e:
                    print(f"Error moving {filename}: {e}")
        
        # If file type doesn't match any category, move to 'Other'
        if not moved and ext != '':
            other_dir = os.path.join(downloads_path, 'Other')
            os.makedirs(other_dir, exist_ok=True)
            try:
                shutil.move(file_path, os.path.join(other_dir, filename))
                print(f"Moved: {filename} -> Other/")
            except Exception as e:
                print(f"Error moving {filename} to Other: {e}")

if __name__ == "__main__":
    print("Starting to organize your Downloads folder...")
    organize_downloads()
    print("Organization complete!")
