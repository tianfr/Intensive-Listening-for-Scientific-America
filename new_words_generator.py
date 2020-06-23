import re
import os
import csv
import sys
import codecs
# reload(sys)
# sys.setdefaultencoding('utf-8')

curr_path = os.getcwd()
print(curr_path)
folders = os.listdir(curr_path)
for folder in folders:
    if os.path.isdir(folder) and folder != ".git":
        print(folder)
        folder_path = curr_path + "\\" + folder + "\\"
        break
new_word_match = "\*\*.*?\*\*"
csv_path = curr_path + "\\wordlist.csv"


def process_file(file):
    print(file)
    rs = []

    with open(file, 'r', encoding="utf-8") as f:
        content = f.read()
    words = re.findall(new_word_match, content)
    print("Words"+"\t\t\t\t\t"+"Descrptions")
    print("-"*60)
    for word in words:
        # print(word)
        Eng, Chi = word.strip("*").split("\\trans")
        print(Eng+"\t\t\t\t\t"+Chi)
        rs.append([Eng, Chi])
    return rs


def main():
    csv_write_content = []
    for file in os.listdir(folder_path):
        if file[-2:] != 'md':
            continue

        csv_write_content += process_file(folder_path + file)
    with codecs.open(csv_path, "w", encoding="utf-8-sig") as f:
        print(csv_path)
        f_csv = csv.writer(f)
        f_csv.writerows(csv_write_content)


if __name__ == "__main__":
    main()
