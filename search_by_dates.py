#!C:\Python27 python
# -*- coding: utf-8 -*-
import sys
import argparse
import os
from os import walk, makedirs
from os.path import join, dirname, exists, basename
from stat import ST_MTIME, ST_ATIME, ST_CTIME
from datetime import date
import datetime, time
import shutil
import errno
from Tkinter import Tk, Label, Checkbutton, Button, BooleanVar
import win32security

date_format = "%d-%m-%Y"
PROGRAM_NAME = 'search_by_dates'
PROGRAM_VERSION = '0.1'

def valid_date(s):
    try:
        return datetime.datetime.strptime(s, date_format)
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)

def copy_files(files, src ,dst):
    for archivo in files:
        path_archivo = archivo[len(src):]
        if archivo[len(src):][0] == '\\' or archivo[len(src):][0] == '/':
            path_archivo = path_archivo[1:]
        destino = join(dst, path_archivo)
        if not exists(dirname(destino)):
            try:
                makedirs(dirname(destino))
                shutil.copy2(archivo, destino)
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
        else:
            shutil.copy2(archivo, destino)
    if len(files) == 0:
        print "None files copied into " + dst
    else:
        print "Files copied into " + dst
    

parser = argparse.ArgumentParser(prog=PROGRAM_NAME, description='%(prog)s is a file search by dates. Tested on Windows SO with Python 2.7.15. PyWin32 224 is required to be installed. It can be downloaded from https://github.com/mhammond/pywin32/releases')
parser.add_argument("init_date", help="Set the starting date of the range - Format DD-MM-YYYY", type=valid_date)
parser.add_argument("final_date", help="Set the final date of the range - Format DD-MM-YYYY", type=valid_date)
parser.add_argument("-s", "--start", help="Set the directory where start to search - By default, it will start in the same directory as %(prog)s", type=str)
parser.add_argument("-t", "--to", help="Set the directory where to copy the found files - By default, found files will be copied into "+PROGRAM_NAME+"_copy", type=str)
parser.add_argument("-f", "--few", help="Use this option to select which files do you want to copy - Without this option, it will copy all found files", action="store_true")

parser.add_argument('-v', '--version', action='version', version='%(prog)s v{}'.format(PROGRAM_VERSION), help="Show program's version number and exit")
search_by = parser.add_argument_group('Search by', 'Specify what kind of date do you want to search. An option must be selected').add_mutually_exclusive_group(required=True)

search_by.add_argument("-c", "--create", help="Specify that you want to search by creation date", action="store_true")
search_by.add_argument("-a", "--access", help="Specify that you want to search by last access date", action="store_true")
search_by.add_argument("-u", "--updated", help="Specify that you want to search by updated date", action="store_true")
args = parser.parse_args()

# rango de fechas introducidas por el usuario 
u_init_date = args.init_date
u_final_date = args.final_date


start_directory = "."
if args.start:
    start_directory = args.start

dir_to_copy = PROGRAM_NAME + "_copy" 
if args.to:
    dir_to_copy = args.to

date_type = ""
if args.create: # creation date
    date_type = ST_CTIME
elif args.access: # last access date
    date_type = ST_ATIME
else: # updated date
    date_type = ST_MTIME

archivos_encontrados = []
for (path, carpetas, archivos) in walk(start_directory):
    for archivo in archivos:
        ruta_relativa_archivo = join(path, archivo)
        f = open(ruta_relativa_archivo)
        st = os.fstat(f.fileno())
        file_date = datetime.datetime.fromtimestamp(st[date_type])
        file_date = datetime.datetime.strftime(file_date, date_format) # formateamos la fecha a dd-mm-yyyy
        file_date = valid_date(file_date)
        if file_date >= u_init_date and file_date <= u_final_date:
            archivos_encontrados.append(ruta_relativa_archivo)
        f.close()

if args.few:
    check_boxes = {}
    master = Tk()
    master.title("Select files")
    Label(master, text="Select the files that you want to copy").pack()
    for archivo in archivos_encontrados:
        aux = BooleanVar()
        check_boxes[archivo] = aux
        sd = win32security.GetFileSecurity(archivo, win32security.OWNER_SECURITY_INFORMATION)
        owner_sid = sd.GetSecurityDescriptorOwner()
        name, domain, kind = win32security.LookupAccountSid(None, owner_sid)
        checkbox_text = "{} -- OWNER: {}\\{}".format(archivo[len(start_directory):], domain, name)
        Checkbutton(master, text=checkbox_text, variable=check_boxes[archivo]).pack()
        #Checkbutton(master, text=archivo[len(start_directory):], variable=check_boxes[archivo]).pack()
    
    selected = []

    def copySelectedFiles():
        for key in check_boxes:
            if check_boxes[key].get():
                selected.append(key)
        copy_files(selected, start_directory, dir_to_copy)
        master.quit()

    Button(master, text="Select", command=copySelectedFiles).pack()
    master.mainloop()
else:
    copy_files(archivos_encontrados, start_directory, dir_to_copy)