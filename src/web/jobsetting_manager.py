# -*- coding: utf-8 -*-

import twisted
from twisted.web import resource, static, server
from . import jsdb

class UpdateJob(resource.Resource):
    
    def __init__(self):

        resource.Resource.__init__(self)

    def render(self, request):

        jobmap = {  'jobid':'',
                    'jobname':'',
                    'searchbase':'',
                    'searchword':'',
                    'getrule':''                   
                }
        for key, values in list(request.args.items( )):
            jobmap[key] = values[0]

        jsdb.updatejob((jobmap['jobid'],jobmap['jobname'],'',jobmap['getrule'],jobmap['searchword'],jobmap['searchbase']))        

        return ListJob(jobmap['jobid']).render(request)

class AddJob(resource.Resource):
    
    def __init__(self):

        resource.Resource.__init__(self)

    def render(self, request):

        jobmap = {  'jobname':'',
                    'searchbase':'',
                    'searchword':'',
                    'getrule':''                   
                }
        for key, values in list(request.args.items( )):
            jobmap[key] = values[0]

        jsdb.addjob((jobmap['jobname'],0,jobmap['getrule'],jobmap['searchword'],jobmap['searchbase']))        

        return ListJob(-1).render(request)

class DelJob(resource.Resource):
    
    def __init__(self):

        resource.Resource.__init__(self)

    def render(self, request):

        jobmap = {  'jobid':-1,}
        for key, values in list(request.args.items( )):
            jobmap[key] = values[0]

        jsdb.deletejob(int(jobmap['jobid']))        

        return ListJob(-1).render(request)

class RunJob(resource.Resource):

    def __init__(self):

        resource.Resource.__init__(self)
        
    def render(self, request):
        
        jobmap = {  'jobid':-1,'searchword':'','searchbase':''}
        for key, values in list(request.args.items( )):
            jobmap[key] = values[0]

        import os
        jobmap['searchbase'] = jobmap['searchbase'].decode("UTF-8","ignore").encode("GBK","ignore")
        jobmap['searchword'] = jobmap['searchword'].decode("UTF-8","ignore").encode("GBK","ignore")
        
        for items in jobmap['searchword'].split(","):
            os.system("start python wg_jshell.py --jobid=%s > scaningjob%s.log &" % (str(jobmap['jobid']),str(jobmap['jobid']))   )
            print("start python wg_jshell.py --jobid=%s > scaningjob%s.log &" % (str(jobmap['jobid']),str(jobmap['jobid'])))
                
        return ListJob(-1).render(request)


class ListJob(resource.Resource):
    
    def __init__(self,jobid=-1):

        resource.Resource.__init__(self)
        self.jobid = jobid

    def render(self, request):

        
        jobitem = None
        for key, values in list(request.args.items( )):

            if key=="jobid" and len(values)>0:                
                try:
                   self.jobid = int(values[0])
                except:
                   self.jobid = -1
                   
        tmp_dts = jsdb.readjobs()
        #设置抓取任务的选择列表
        slt_str = """<form name="slt_form" method="post" action="list">
                        <script type="text/javascript">
                                function subform()
                                    {
                                        document.forms["slt_form"].submit();
                                        return
                                    }
                        </script>
                        <select name="jobid" onchange="subform();">
                    """
        for items in tmp_dts:
            if str(items[0]) != str(self.jobid):
                slt_str += '<option value="'+str(items[0])+'">'+items[1]+'</option>\n'
            else:
                slt_str += '<option selected="selected" value="'+str(items[0])+'">'+items[1]+'</option>\n'
                jobitem = items
                                
        slt_str += '</select></form>'
        #保存任务的更新
        edit_str = '<form name="edit_form" method="post" action="update"><table style="width:100%">'
        
        if len(tmp_dts)>0:
            if jobitem == None:
                jobitem = tmp_dts[0]
                
            tmp_flag_str = "未进行扫描"
            if str(jobitem[2]) == "2":
                tmp_flag_str = "扫描完成"
            elif str(jobitem[2]) == "1":
                tmp_flag_str = "扫描进行中"
            
            edit_str += '<tr><td>任务编号：</td><td>'+str(jobitem[0])+'<input type="hidden" id="jobid" name="jobid" value="'+str(jobitem[0])+'" /></td></tr>\n'
            edit_str += '<tr><td>任务名称：</td><td><input type="text" id="jobname" name="jobname" size="41" value="'+str(jobitem[1])+'" /></td></tr>\n'
            edit_str += '<tr><td>搜索范围：</td><td><input type="text" id="searchbase" name="searchbase" size="41" value="'+str(jobitem[5])+'" /></td></tr>\n'        
            edit_str += '<tr><td>搜索关键字：</td><td><input type="text" id="searchword" name="searchword" size="41" value="'+str(jobitem[4])+'" /></td></tr>\n'        
            edit_str += '<tr><td>任务抓取设置：</td><td><textarea name="getrule" cols="60" rows="10" id="myarea">'+str(jobitem[3])+'</textarea></td></tr>\n'
            edit_str += '<tr><td>任务状态：</td><td>'+tmp_flag_str+'</td></tr>\n'
            edit_str += '<tr><td><input type="submit" value="保存更新" /></td><td></td></tr>\n'

        edit_str += '</table></form>'
        #启动抓取任务
        if jobitem != None:
            edit_str += '<form name="run_form" method="post" action="run">\
            <input type="hidden" id="jobid" name="jobid" value="'+str(jobitem[0])+'" />\
            <input type="hidden" id="searchbase" name="searchbase" value="'+str(jobitem[5])+'" />\
            <input type="hidden" id="searchword" name="searchword" value="'+str(jobitem[4])+'" />\
            <input type="submit" value="启动任务" /></form>'
        #保存新建的抓取任务
        add_str = '<form name="add_form" method="post" action="add"><table style="width:100%">'
        add_str += '<tr><td>任务名称：</td><td><input type="text" id="jobname" name="jobname" size="41"  /></td></tr>\n'
        add_str += '<tr><td>搜索范围：</td><td><input type="text" id="searchbase" name="searchbase" size="41"  /></td></tr>\n'        
        add_str += '<tr><td>搜索关键字：</td><td><input type="text" id="searchword" name="searchword" size="41"  /></td></tr>\n'        
        add_str += '<tr><td>任务抓取设置：</td><td><textarea name="getrule" cols="60" rows="10" id="myarea"></textarea></td></tr>\n'      
        add_str += '<tr><td><input type="submit" value="保存" /></td><td></td></tr>\n'
        add_str += '</table></form>'

        del_str = ""
        if jobitem != None:
            del_str = '<form name="del_form" method="post" action="del"><input type="hidden" id="jobid" name="jobid" value="'+str(jobitem[0])+'" /><input type="submit" value="删除此任务" /></form>'
        #获得页面的基本源码，并“创建任务”、“更新任务”等代码块加入其中，最后返回应答页面的最终源码
        tmp_file = open("jspage.html","r")        
        rtv = tmp_file.read()
        tmp_file.close()
        rtv = rtv.replace("${slt_str}",slt_str)
        rtv = rtv.replace("${del_str}",del_str)
        rtv = rtv.replace("${edit_str}",edit_str)
        rtv = rtv.replace("${add_str}",add_str)

        return rtv

        
class HomePage(resource.Resource):

    def render(self, request):

        return """

        <html>

        <head>

          <title>Colors</title>

          <link type='text/css' href='/styles.css' rel='Stylesheet' />

        </head>

        <body>

        <h1>Colors Demo</h1>

        What's here:

        <ul>

          <li><a href='/color'>Color viewer</a></li>

        </ul>

        </body>

        </html>

        """


#启动twisted程序，加载了对客户端具体请求的响应.web服务启动了，等待客户端请求
if __name__ == "__main__":

    from twisted.internet import reactor

    root = resource.Resource( )

    root.putChild('', HomePage( ))

    root.putChild('list', ListJob(-1))

    root.putChild('update', UpdateJob())

    root.putChild('add', AddJob( ))

    root.putChild('del', DelJob( ))

    root.putChild('run', RunJob( ))

    site = server.Site(root)

    reactor.listenTCP(8000, site)

    reactor.run( )
