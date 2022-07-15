import os
 
def reNameByTime(path):
 
    mlist = []
    # 获取文件名列表
    files = os.listdir(path)

    # 获得名称带时间戳的新文件名列表
    for filename in files:
        # 获得文件的最后修改时间
        modifytimes = os.path.getmtime(path + filename)
        filename_lower = filename.lower()
        # 筛选.jpg格式
        if ".jpg" in filename_lower:
            mlist.append(str(int(modifytimes)) + "-" + filename)   # .jpg
    
    # 按时间戳排序的列表
    mlist = sorted(mlist)

    # 新文件名列表
    classes_path = os.path.expanduser('./renamelist.txt')
    with open(classes_path,'r',encoding = 'UTF-8') as f:
        newnamelist = f.readlines()
    newnamelist = [c.strip() for c in newnamelist]

    # 检查要修改文件总数与txt给定新文件名总数是否一致，一致再进行重命名，否则提示
    if len(mlist) == len(newnamelist):
        # 遍历修改文件名
        for i in range(len(mlist)):
        # 截取获得原先的文件名
            oldname = mlist[i][11:]     # 切片操作，从11至后
        # 获得新文件名
            newname = newnamelist[i] + ".jpg"    
        # 测试输出新旧文件名
        #    print(newname, oldname)
        # 重命名文件，按修改时间排序并加序号前缀
            os.rename(path + oldname, path + newname)
        print("修改成功，请注意核查。")
    else:
        print("图片数量与新文件名称数量不一致，请检查。")
 
#如果想执行py文件，可以将后缀改为“.py”，如果想打包成exe，需要将后缀改为“.exe”
if __name__ == "__main__":
    filepath = os.sys.argv[0].replace("rename.py", "") 
    print(os.sys.argv[0])
    reNameByTime(filepath)
