#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import csv
from PyPDF2 import PdfFileReader

walk_dir = sys.argv[1]

print('walk_dir = ' + walk_dir)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
root = os.path.abspath(walk_dir)

print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))
list_file_path = os.path.join(root, 'my-ebooks-list.csv')
with open(list_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['File Name', 'File Path', 'No: of pages'])
    
    for (root, subdirs, files) in os.walk(walk_dir):
        print('--\nroot = ' + root)
        print('list_file_path = ' + list_file_path)
        
        with open(list_file_path, 'wb') as list_file:
            for subdir in subdirs:
                print ('\t- subdirectory ' + subdir)
                
            for filename in files:
                if not filename.endswith('.pdf'):
                    continue
                    
                file_details_list = []
                file_details_list.append(filename)
                file_path = os.path.join(root, filename)
                print('\t- file %s (full path: %s)' % (filename,
                        file_path))
                file_details_list.append(file_path)
                
                try:
                    with open(file_path, 'rb') as pdf_file:
                        pdf_reader = PdfFileReader(pdf_file,strict=False)
                        print("The total number of pages in the pdf document is " + str(pdf_reader.numPages))
                        file_details_list.append(pdf_reader.numPages)
                        writer.writerow(file_details_list)
                except Exception:
                    continue
		
