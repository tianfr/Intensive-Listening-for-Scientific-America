import re, os
curr_path = os.getcwd()
print(curr_path)
new_word_match = "\*\*.*?\*\*"

def process_file(file):
    print(file)
    with open(file,'r', encoding="utf-8") as f:
        content = f.read()
    words = re.findall(new_word_match, content)
    print("Words"+"\t\t\t\t\t"+"Descrptions")
    print("-"*60)
    for word in words:
        Eng, Chi = word.strip("*").split("\\trans")
        print(Eng+"\t\t\t\t\t"+Chi)

def main():
    
    for file in os.listdir(curr_path):
        if file[-2:] != 'md': continue
        
        process_file(file)

if __name__ == "__main__":
    main()
    
    
    
    

    