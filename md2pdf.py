import glob
import subprocess
import os
import argparse

def main(md_file_name=None):
    """
    Converts Markdown files to PDF using Pandoc.

    Args:
        md_file_name (str): The name of the Markdown file to convert. 
        If None, all Markdown files in the folder and its sub-folders will be converted.

    Returns:
        None
    """
    # Find all .md files in the folder and its sub-folders
    
    if md_file_name:
        md_file = md_file_name
        pdf_file = md_file.replace('.md', '.pdf')
        print(f'Converting {md_file} to {pdf_file}')
        subprocess.run(['pandoc', md_file, '-o', pdf_file, '--pdf-engine=xelatex', '--include-in-header=md2pdf.tex'])
        print('Completed.')
        
    else:
        md_files = []
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file.endswith('.md'):
                    md_files.append(os.path.join(root, file))

        # Convert each .md file to .pdf
        for md_file in md_files:
            if 'Readme' in md_file:
                continue
            pdf_file = md_file.replace('.md', '.pdf')
            print(f'Converting {md_file} to {pdf_file}')
            subprocess.run(['pandoc', md_file, '-o', pdf_file, '--pdf-engine=xelatex', '--include-in-header=md2pdf.tex'])
            print('Completed.')


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--md_file_name", '-n', help="Name of the .md file to convert to .pdf")
    args = parser.parse_args()

    main(args.md_file_name)