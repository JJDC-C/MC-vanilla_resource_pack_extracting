import json
import os


def input_client(version):
  '''输入文件 client.json'''
  json_path = input_path + '/versions/' + version + '/' +  version + '.json'
  with open(json_path, 'r', encoding='utf-8') as mf:
    main = json.load(mf) #将json转为字典
  return main

def version_mainfest(file):
  '''提取索引'''
  #file为字典
  version_mainfest = file['assetIndex']['id'] #获取versison_mainfest id号
  return str(version_mainfest)

def get_index(index_id):
  '''文件信息获取'''
  indexes_json = input_path + '/assets/indexes/' + index_id + '.json'
  with open(indexes_json) as file:
    ind =  json.load(file)
  obj = ind['objects']
  return obj

def get_output_file(obj):
  '''寻找并复制文件'''
  
  for path0, hash0 in dict.items(obj):
    #文件原位置
    hash1 = hash0['hash']
    hash2 = hash1[:2]
    hash_path = input_path + '/assets/' + 'objects/' + hash2
    hash_file = (hash_path + '/' + hash1).replace('/', '\\') #原位置(完整路径)(含\\)

    #输出路径
    path1 = path0.split('/')
    path = '/'.join((path1)[0:-1])
    cmd_path = (mc_res_path + path).replace('/', '\\')#组合路径(\\)
    new_file_name = ''.join(path1[-1:])
    new_file_path = (mc_res_path + path0).replace('/', '\\') #输出位置(完整路径)(含\\)
    if os.path.exists(cmd_path): #去除重复文件夹
      pass
    else:
      cmd = 'md ' + cmd_path #创建文件夹
      os.system(cmd) #发送到cmd
    
    #复制
    cmd_copy = 'copy ' + hash_file + ' ' + cmd_path + '>nul'
    os.system(cmd_copy) #复制hash到输出
    cmd_ren = 'ren ' + cmd_path + '\\' + hash1 + ' ' + new_file_name + '>nul'
    os.system(cmd_ren) #重命名
    if not os.path.isfile('./noprint.txt'):
      print(new_file_path)


print('MC原版资源包提取\n输入（或拖入）.minectaft文件夹位置')
input_path = input('路径：')
t = input_path.find('.minectaft')
if t == -1:
  input_path = input_path + '\\.minecraft'
input_path.replace('\\', '/')

print('输出到（会到此文件夹的"/<版本>-resources"下）：')
output_path = input('请输入路径：')

print('输入版本，如"1.20.1","24w17a"')
版本 = input()
print('大约需要五分钟...\n按下Ctrl+C以终止\n')

mc_res_path = (output_path.replace('\\', '/')) + '/' + 版本 + '-resources/'

main =  input_client(version=版本)
index_id = version_mainfest(file=main)
index_obj = get_index(index_id=index_id)
get_output_file(obj=index_obj)
print('提取完成')