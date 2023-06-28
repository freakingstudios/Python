import os
import webbrowser


def run_html_files(folder_path):
    # Get the list of files in the folder
    file_list = os.listdir(folder_path)

    # Iterate over each file
    for file_name in file_list:
        # Check if the file is an HTML file
        if file_name.endswith('.html'):
            # Construct the full path to the HTML file
            file_path = os.path.join(folder_path, file_name)

            # Open the HTML file in a web browser
            webbrowser.open(file_path, new=2)  # 'new=2' opens in a new tab if possible


# Provide the folder path where the HTML files are located
folder_path = r'C:\Users\jeremiahkalaiselvan\Documents\Projects\JobFinderPlus\Website'

# Run the HTML files
run_html_files(folder_path)
