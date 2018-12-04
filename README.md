# Search by dates
## Introduction
> Find the files whose access, modification or creation date is in the specified date range.

> This script has been created by David González Pérez for the second job of the subject Informática Forense in Computer Engineer at UVa, Spain.

## Requirements
1. Python 2.7 installed into C:\Python27
2. PyWin32 224. It can be downloaded from https://github.com/mhammond/pywin32/releases

## Examples for use
> **INIT_DATE** and **FINAL_DATE** have to have the format **dd-mm-yyyy**
### Find files created between INIT_DATE and FINAL_DATE
> python search_by_dates.py INIT_DATE FINAL_DATE -c

> This will copy all the files found in the ./search_by_dates_copy directory with the same relative directory structure

### Find files updated between INIT_DATE and FINAL_DATE and select the found files that I want to copy
> python search_by_dates.py INIT_DATE FINAL_DATE -u -f

> This will show a UI where we could select the files to copy. Then, it will copy all selected files in the ./search_by_dates_copy directory with the same relative directory structure

### Start searching for files whose last access date is in the range of dates INIT_DATE and FINAL_DATE from the directory specified by the -s option.
> python search_by_dates.py INIT_DATE FINAL_DATE -a -s ../

> The start directory could be specified by absolut or relative path

### To specify the directory where we want to copy the found files, we have to use -t option.
> python search_by_dates.py INIT_DATE FINAL_DATE -a -t ../

> This will copy all the files found in the directory ../ with the same relative directory structure