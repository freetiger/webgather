# -*- coding: utf-8 -*-
import pickle
#start
jobpath = []

jobpath.append({
        "url":['http://songshuhui.net/archives/tag/%E5%8E%9F%E5%88%9B',],
        "regexps":[{        
        "str":"nextPageUrl",
        "exp":['<a class="nextpostslink" href="([^"]*)"[^>]*>[^<]*</a>',],
        "unique":"1",
        }, ],
       "getblocks":{"start_str":'<html>',"end_str":'</html>',"cnt_str":"comblock"},
       "encoding":"UTF-8",
       "needLoop":"1",
       "loopUrl":["${nextPageUrl1}",],
       "job_description":"科学松鼠会-原创列表"
    })

jobpath.append({
    "url":['inline:///${comblock}',],
    "regexps":[{        
        "str":"title",
        "exp":['<h3 class="storytitle"><a class="black" href="([^"]*)"[^>]*>([^<]*)</a></h3>',],
        "unique":"0",
        },],
   "encoding":"UTF-8",
   "needLoop":"0",
   "loopUrl":[],
   "job_description":"科学松鼠会-原创标题链接"
})

jobpath.append({"endflag":"1","outputkeys":["title1","title2",]})
#end

cc = pickle.dumps(jobpath)
#print cc

tmp_file = open("output.txt","wb")
tmp_file.write(cc)
tmp_file.close()

