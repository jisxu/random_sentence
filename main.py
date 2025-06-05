import random
import json
import pyperclip

def main():
    lines=[]
    with open('sentence.json','r',encoding='utf-8') as f:
        for line in f:
            line=line.strip()
            if line:
                lines.append(line)
    if not lines:
        print("空文件")

    random_line=random.choice(lines)

    data=json.loads(random_line)
    name=data.get('name')
    fromwho=data.get('from')

    content=name+"---"+fromwho
    print(content)

    pyperclip.copy(content)


if __name__ == "__main__":
    main()
