def format_size(size: int, precision: int = 2) -> str:
    '''
    格式化文件大小
    size: 文件大小，字节表示
    precision: 精度
    返回值: 格式化后的文件大小字符串
    '''
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB']
    index = 0
    while size >= 1024 and index < len(suffixes) - 1:
        size /= 1024
        index += 1
    return f'{size:.{precision}f} {suffixes[index]}'