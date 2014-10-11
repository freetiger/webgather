# -*- coding: utf-8 -*-

from mysql import connector

from . import configure


def getConnect():
    host = configure.db_mysql_host
    port = configure.db_mysql_port
    database = configure.db_mysql_db
    user = configure.db_mysql_user
    password = configure.db_mysql_passwd
    return connector.connect(host=host, port=port, database=database,user=user,password=password)

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


