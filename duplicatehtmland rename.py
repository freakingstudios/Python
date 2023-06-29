import shutil
import os

def duplicate_and_rename_html(original_file, new_names, original_dir, destination_dir):
    for name in new_names:
        new_file = os.path.join(destination_dir, f"{name}.html")
        shutil.copyfile(original_file, new_file)

# Example usage
original_file = r'C:\Users\jeremiahkalaiselvan\Documents\Projects\JobFinderPlus\Website\tcsprocess.html'
new_names = ['infosysprocess', 'wiproprocess', 'accentureprocess', 'zohoprocess']
original_dir = r'C:\Users\jeremiahkalaiselvan\Documents\Projects\JobFinderPlus\Website'
destination_dir = r'C:\Users\jeremiahkalaiselvan\Documents\Projects\JobFinderPlus\Website'

duplicate_and_rename_html(original_file, new_names, original_dir, destination_dir)
