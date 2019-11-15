from typing import *
from utils.messages import *
from utils.errors import *
from django.conf import settings

from .forms import KualiForm, SunapsisForm

import datetime
import os
import xlrd

class FileError(Exception):
    def with_message(self, request, message):
        messages.error(request, message)
        return self
    
def date_of(s):
    ''' 1997-03-01 -> datetime object '''
    year, month, day = s.split('-')
    year = int(year)
    month = int(month if month[0] != '0' else month[1:])
    day = int(day if day[0] != '0' else day[1:])
    return datetime.datetime(year, month, day)
    
def upload_file(request, f):
    name = datetime.datetime.now().strftime('%m%d%H%M') + '.xlsx'
    path = os.path.join(settings.FILES_ROOT, name)
    with open(path, 'wb+') as outfile:
        for chunk in f.chunks():
            outfile.write(chunk)
        return path
    raise ServerError('file writing failed')
            
def sheet_of(request, workbook: xlrd.book.Book) -> Tuple[Tuple[int, int], Callable[[int, int], str]]:
    if workbook.nsheets != 1:
        raise FileError().with_message(request, f'excel can only contain 1 sheet, sheets: {workbook.nsheets}')
    sheet = workbook.sheet_by_index(0)
    m, n = sheet.nrows, sheet.ncols
    if m == 0 or n == 0:
        raise FileError().with_message(request, 'empty excel sheet')
    
    def value_of(i, j) -> str:
        cell = sheet.cell(i, j)
        if cell.ctype == xlrd.XL_CELL_EMPTY:
            return ''
        elif cell.ctype == xlrd.XL_CELL_TEXT:
            return cell.value
        elif cell.ctype == xlrd.XL_CELL_NUMBER:
            return str(cell.value)
        elif cell.ctype == xlrd.XL_CELL_DATE:
            date = xlrd.xldate.xldate_as_tuple(cell.value, datemode=0) # datemode
            return f'{date[0]}-{date[1]}-{date[2]}'
        elif cell.ctype == xlrd.XL_CELL_BOOLEAN:
            return str(True if cell.value == 1 else False)
        else:
            raise FileError().with_message(request, f'cell type error at ({i},{j})')
    
    return (m,n), value_of
            
def validate_excel(request, path):
    titles = set((
        'doc_id,tracking_id,fullname_kuali,siss_account,dept_account,'
        'amount_kuali,date_kuali,ref_id,sunapsis_id,firstname_sunapsis,'
        'lastname_sunapsis,job_title_sunapsis,position_id_sunapsis,'
        'dept_name_sunapsis,dept_contact_sunapsis,visa_amount_sunapsis,'
        'visa_sunapsis,amount_sunapsis,date_sunapsis'
    ).split(','))
    
    (m, n), sheet = sheet_of(request, xlrd.open_workbook(path))
    
    valid_file = True
    for j in range(0, n):
        if sheet(0, j) not in titles:
            messages.error(request, f'(0,{j}) not a valid title, value ({sheet(0, j)})')
            valid_file = False
    if not valid_file:
        raise FileError()
        
    for i in range(1, m):
        entry = {sheet(0, j): sheet(i, j) for j in range(0, n)}
        if not entry:
            continue
        kf, sf = KualiForm(entry), SunapsisForm(entry)
        if not kf.is_valid():
            valid_file = False
            messages.error(request, f'{i} row, {kf.errors.as_json()}')
        if not sf.is_valid():
            valid_file = False
            messages.error(request, f'{i} row, {sf.errors.as_json()}')
            
    if not valid_file:
        raise FileError()
        
def compose(request, path):
    (m, n), sheet = sheet_of(request, xlrd.open_workbook(path))
    count = 0
    for i in range(1, m):
        entry = {sheet(0, j): sheet(i, j) for j in range(0, n)}
        if not entry:
            continue
        KualiForm(entry).save()
        SunapsisForm(entry).save()
        count += 1