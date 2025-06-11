import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import sql_job

path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','Scraper','Selenium'))
sys.path.insert(0,path)
import Sele_General
path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','GeneralTools'))
sys.path.insert(0,path)
import time_convertor
path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','Outputs',))
sys.path.insert(0,path)
import csv_out

site = 'https://remoteok.com/'
DB = "./Deliverables/job-scraper-tracker/remoteOK"
table = "jobs"
CSV_ = "./Deliverables/job-scraper-tracker/remoteOK"


def seperate_salary(location):
    if re.search(r"\$\d{1,3}[kK](?:\s*-\s*\$\d{1,3}[kK])?",location):
        salary = re.findall(r"\$\d{1,3}[kK](?:\s*-\s*\$\d{1,3}[kK])?",location)
        location = re.sub(r"\💰\s*\$\d{1,3}[kK](?:\s*-\s*\$\d{1,3}[kK])?","",location)
        location = re.sub(r"[^a-zA-Z0-9\s]","",location)
        location = re.sub(r"^\s+","",location)
        return salary[0],location
    else: 
        location = re.sub(r"[^a-zA-Z0-9\s]","",location)
        location = re.sub(r"^\s+|\s+$","",location)
        return "",location

def main():
    driver = Sele_General.selenium(['Edge',"google",[5,10]])
    driver.open_edge()
    driver.navigate_address_bar(site) 
    jobs=driver.find_elements(By.CSS_SELECTOR,"tr.job",get_text=True)
    driver.close_page()


    primary = None
    columns = {"positions":"TEXT","company":"TEXT","salary":"TEXT","location":"TEXT","req":"TEXT","post_date":"TEXT"}
    unique = ["positions","company","salary","location","req"]

    positions = []
    company = []
    salary = []
    location = []
    req = []
    roles = []
    post_date = []

    sql_job.create_table_statement(DB,table,primary=None,columns=columns,unique=unique)
    dict_keys= sql_job.all_column_names_stripped(sql_job.all_column_names(DB,table))
    dict = {}
    for x in dict_keys:
        dict[x] = ''
    #print(dict)

    clean = lambda s: re.sub(r'\s+', ' ', s.strip())
    for job in jobs:
        for attributes in job:
            att = attributes.split('\n')
            entry = {}

            if re.fullmatch(r"[A-Z]{1,2}", att[0]):
                entry['positions'] = att[1]
                entry['company'] = att[2]
                s, l = seperate_salary(att[3])
                entry['salary'] = s
                entry['location'] = l
                roles = [att[x] for x in range(4, len(att)-1)]
            else:
                entry['positions'] = att[0]
                entry['company'] = att[1]
                s, l = seperate_salary(att[2])
                entry['salary'] = s
                entry['location'] = l
                roles = [att[x] for x in range(3, len(att)-1)]

            entry['req'] = ' '.join(roles)
            time_raw = att[-1]
            time_num = re.sub(r"[h,d,m,y,mo]", '', time_raw)
            unit_time = re.sub(r'[0-9]{1,2}', '', time_raw)
            dt = time_convertor.convert(time_num, unit_time)
            entry['post_date'] = dt.strftime('%Y-%m-%d')
            for k in entry:
                entry[k] = clean(entry[k])
        sql_job.insert(DB, table, entry)
    print(sql_job.all_rows(DB,table))
    sql_job.check_def(DB,table)
    csv_out.export_sqlite_to_csv(DB,table,CSV_)
main()