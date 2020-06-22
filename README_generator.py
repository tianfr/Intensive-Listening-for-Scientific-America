import os,re
curr_path = os.getcwd()
tar = "\-\-\-.*?\-\-\-"
def process_file(file):
    print(file)
    with open(file, 'r') as f:
        content = f.read()
        # print(content)
        rs = re.findall(tar, content, flags=re.DOTALL)
        rs = rs[0]
        rs = rs.strip("-").strip("\n").split("\n")
        print(rs)

def main():
    folders = os.listdir(curr_path)
    for folder in folders:
        if os.path.isdir(folder) and folder != ".git":
            print(folder)
            folder_path = curr_path + "\\" + folder + "\\"
            break
    
    for file in os.listdir(folder_path):
        if file[-2:] != 'md':
            continue
        process_file(folder_path + file)
main()