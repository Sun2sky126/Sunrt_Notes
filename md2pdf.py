import glob
import subprocess
import os

# Find all .md files in the folder and its sub-folders
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