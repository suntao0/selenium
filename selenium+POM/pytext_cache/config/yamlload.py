# 开发人员:Sun
# 开发时间:2021/6/28  23:41:41
# 文件名称:yamlload.PY
# 开发工具:PyCharm
import  yaml
# 用封装方法
def loadyaml(filename):
    # 读取yaml文件  
    files = open(filename,'r',encoding='utf-8')
    # 读取files里面内容
    data = yaml.load(files,Loader=yaml.FullLoader)
    return data


