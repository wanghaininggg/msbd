def print_directory_contents(sPath):
    """
    这个函数接受文件夹名称作为参数
    反回该文件夹中的文件路径
    已经其包含文件夹中文件的路径
    """
    import os

    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)