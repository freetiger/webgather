# -*- coding: utf-8 -*-
import configure
import MySQLdb
import datetime
import pickle
import os

def getConnect():
    return MySQLdb.connect(host=configure.db_mysql_host,port=configure.db_mysql_port,db=configure.db_mysql_db,user=configure.db_mysql_user,passwd=configure.db_mysql_passwd)

def readjobs():
    conn = getConnect()
    cur = conn.cursor()
    cur.execute("select job_id ,job_name, job_flag,get_rules,searchwords,searchbase from wg_job order by job_id desc")    
    conn.commit()
    rtv = cur.fetchall()
    conn.close()           
    return rtv


def updatejob(items):
    conn = getConnect()
    cur = conn.cursor()
    cur.execute("update wg_job set job_name=%s,get_rules=%s,searchwords=%s,searchbase=%s where job_id =%s",(items[1],items[3],items[4],items[5],items[0]))
    conn.commit()
    conn.close() 
    return

def addjob(jobitems):
    conn = getConnect()
    cur = conn.cursor()
    cur.execute("insert into wg_job(job_name,job_flag,get_rules,searchwords,searchbase) values(%s,%s,%s,%s,%s)",jobitems)
    conn.commit()
    conn.close()
    
    return

def deletejob(jobid):
    conn = getConnect()
    cur = conn.cursor()
    cur.execute("delete from wg_job where job_id =%s",(jobid,))
    conn.commit()
    conn.close()
    
    return


