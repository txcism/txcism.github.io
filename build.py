import os

main_name = 'index'

file_head = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style type="text/css">
a {color:red; text-indet:20%;}
</style>
</head>
<body>
'''
file_body = ''
file_tail = '''
</body>
</html>
'''

#path 是路径，包括:
#dir 是目录
#file 是文件

#all file path
def find_all(dirname = os.getcwd(), file_paths={}):
    for base_path in os.listdir(dirname):
        path = os.path.join(dirname, base_path)
        #
        if os.path.isdir(path):
            find_all(path)
        else:
            file_paths[path] = base_path
    return file_paths

# relative_path
def get_relative_paths(paths):
    relative_paths = {}
    ind = len(os.getcwd()) + 1
    for k, v in paths.items():
        relative_paths[k[ind:]] = v
    return relative_paths


#
def create_element(path, name):
    splits = name.split('.')
    if len(splits) > 1:
        file_type = splits[-1]
        file_name = splits[-2]
        if file_type == 'html' and file_name != main_name:
            return '<p class="entry"><a href="' + path + '">' + file_name + '</a></p>'
    return ''

#
def create_body(paths):
    body = ''
    for k, v in paths.items():
        body += create_element(k, v) + '\n'
        print(k, v)
    return body


if __name__=="__main__":
    paths = find_all()
    relative_paths = get_relative_paths(paths)
    file_body = create_body(relative_paths)
    file = file_head + file_body + file_tail
    with open(main_name+'.html', encoding='utf-8', mode='w') as f:
        f.write(file)