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
```shell
    python search_by_dates.py INIT_DATE FINAL_DATE -c
```

> This will copy all the files found in the **./search_by_dates_copy** directory with the same relative directory structure

### Find files updated between INIT_DATE and FINAL_DATE and select the found files that I want to copy
```shell
    python search_by_dates.py INIT_DATE FINAL_DATE -u -f
```

> This will show a UI where we could select the files to copy. Then, it will copy all selected files in the ./search_by_dates_copy directory with the same relative directory structure

> ![comando_-c_and_-f](/uploads/12af33cf48096d0277186fc0b0e2dbc4/comando_-c_and_-f.PNG)

### Start searching for files whose last access date is in the range of dates INIT_DATE and FINAL_DATE from the directory specified by the -s option.
```shell
    python search_by_dates.py INIT_DATE FINAL_DATE -a -s PATH_START
```

> The start directory could be specified by absolut or relative path

> **PATH_START** can be a relative or absolute path. If **PATH_START** contains spaces, put it in double quotes like this: "some/relative path/with spaces" or "C:some/absolute path/with spaces"

### To specify the directory where we want to copy the found files, we have to use -t option.
```shell
    python search_by_dates.py INIT_DATE FINAL_DATE -a -t PATH_TO
```

> This will copy all the files found in the directory ../ with the same relative directory structure

> **PATH_TO** can be a relative or absolute path. If **PATH_TO** contains spaces, put it in double quotes like this: "some/relative path/with spaces" or "C:some/absolute path/with spaces"

### For more help use -h
```shell
    python search_by_dates.py -h
```
![comando_-h](/uploads/60c224d1026344e19e5479833ad5c839/comando_-h.PNG)