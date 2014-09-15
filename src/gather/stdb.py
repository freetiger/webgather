# -*- coding: utf-8 -*-
import configure
import MySQLdb
import datetime
from Queue import Queue
import threading
import pickle
import os
import urllib2,cookielib

def getConnect():
    return MySQLdb.connect(host=configure.db_mysql_host,port=configure.db_mysql_port,db=configure.db_mysql_db,user=configure.db_mysql_user,passwd=configure.db_mysql_passwd)

'''有啥用存疑，找以前完整程序看看
class CGWorker(threading.Thread):
    def __init__(self, threadname, queue):
        
        threading.Thread.__init__(self, name = threadname)
        self.sharedata = queue

    def run(self):

        print self.getName(),'Started'
        import homepageretrieve       
        
        while True:

            gw_name = self.sharedata.get()
            rts = homepageretrieve.hpgrabber(gw_name)
            tmp_conn = getConnect()
            tmp_cur = tmp_conn.cursor()
            tmp_cur.execute("update wg_corp set gwdz = %s where corpname = %s and gwdz='na'",(rts,gw_name))
            tmp_conn.commit()
            tmp_conn.close()
                        
            self.sharedata.task_done()
        
        print self.getName(),'Finished'
 '''   
    
class dbpipe(object):
    def __init__(self):
        self.threadNo = 0
        self.conn = None
        self.scanid = None
        self.jobid = None
        self.projid = None
        self.jobsetting = []
        self.dbprefix = "db_"
        self.scanprefix = "scan_data_"
        self.tablestruct = "data_struct_"
        self.coltype = {}
        self.col_list = ""
        self.value_list = ""
        self.cwd = os.getcwd()        
        if not os.path.isdir(self.cwd+"/localfiles"):
            os.mkdir(self.cwd+"/localfiles")
    
    def prepareScan(self,jobid):
        type_map = {"0":"REAL","1":"TEXT","2":"TEXT","3":"BLOB"}
        self.jobid = jobid
        self.conn = getConnect()
        cur = self.conn.cursor()
        date_str = datetime.datetime.now()
        cur.execute("insert into wg_scan(scan_start,job_id,scan_flag,isfinish) values (%s,%s,%s,0)",(date_str,jobid,2))
        self.scanid = cur.lastrowid
        self.conn.commit()
        cur.execute("update wg_job set job_flag = 1 where job_id = %s ",(self.jobid,))
        self.conn.commit()      
        
        self.projid = 1
        
        #cr_str = open('foshan.rule','rb').read()
        #cr_str = items[0][2]
        #if len(cr_str)>10:
        #    cr_str = cr_str.replace("\r","")
        #    self.jobsetting = pickle.loads(cr_str)
        #else:
        #    return None

        cur.execute("select get_rules from wg_job where job_id = %s ",(self.jobid,))
        self.conn.commit()
        
        tmp_dts = cur.fetchall()
        if len(tmp_dts)>0:
            cr_str = tmp_dts[0][0]
            cr_str = cr_str.replace("\r","")
            self.jobsetting = pickle.loads(cr_str)
            
        #else:
        #    return None
        
        #cur.execute("select field_id,col_name,field_name,field_type,field_len,is_hide,gradation from wg_data_structure where job_id =%s",(self.jobid,))
        #fieldstr = open('foshan.col','rb').read()
        #fields = []
        #for line in fieldstr.splitlines():
        #    fields.append(line.split('\t'))
        #items = cur.fetchall()
        #tmp_conn.commit()
        #tmp_conn.close()
        
      

        return 0

    def finishscan(self):
        
        self.conn = getConnect()
        cur = self.conn.cursor()
        cur.execute("update wg_scan set scan_end=%s, isfinish = 1,scan_flag=0 where scan_id = %s",(datetime.datetime.now(),self.scanid))
        cur.execute("update wg_job set job_flag = 2 where job_id = %s ",(self.jobid,))
        self.conn.commit()
        self.conn.close()
        
        return 0
        
if __name__ == "__main__" :
    pass
