import os,re
curr_path = os.getcwd()
tar = "\-\-\-.*?\-\-\-"
prev_text = """
# Intensive-Listening-for-Scientific-America
Intensive Listening and Learning English\n
"""
def process_file(file):
    print(file)
    dic_rs = {}
    with open(file, 'r', encoding="utf-8") as f:
        content = f.read()
        # print(content)
        rs = re.findall(tar, content, flags=re.DOTALL)
        rs = rs[0]
        rs = rs.strip("-").strip("\n").split("\n")
        # print(rs)
        

        for each in rs:
            key, value = each.split(":")
            dic_rs[key] = value
        print(dic_rs)
    return dic_rs

def main():
    folders = os.listdir(curr_path)
    for folder in folders:
        if os.path.isdir(folder) and folder != ".git":
            print(folder)
            folder_path = curr_path + "\\" + folder + "\\"
            break
    
    files_dic = []
    for file in os.listdir(folder_path):
        if file[-2:] != 'md':
            continue
        file_dic = process_file(folder_path + file)
        files_dic.append(file_dic)
    write_str = ''
    write_str += prev_text
    with open("README.md", "w", encoding="utf-8") as f:
        # f.write(prev_text)
        for each_dic in files_dic:
            keys = list(each_dic.keys())
            # print(list(keys))
            keys.sort()
            
            for key in keys:
                write_str += key + ": **" + each_dic[key].strip() + "** "
            write_str += "\n"
        print(write_str)
        f.write(write_str)
main()