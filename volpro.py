import concurrent.futures
import subprocess
import sys
import time
import os
import shutil
import random

print('''
嗨嗨！欢迎使用VolPro脚本，By.Tokeii🎉

让我们快速了解一下如何使用它吧！准备好了吗？🚀

📝 输入以下命令格式开始使用VolPro：
```
python volpro.py [imagename] (profile) (dumpfiles)
```
记住，小括号里的参数是可选的哦！如果你想使用dumpfiles功能，就一定要提供profile参数。

让我来解释一下各个参数的含义吧：
- `[imagename]`：你的映像文件路径。告诉我它在哪里！📁
- `(profile)`：可选的profile参数。如果你提供了它，我们会跳过imageinfo任务。
- `(dumpfiles)`：可选的dumpfiles参数。如果你想使用它，一定要提供profile参数。

不要着急，VolPro会帮你自动执行一系列任务，并将结果保存在output文件夹中。而且，我们还会把这些结果打包成漂亮的markdown文档，方便你查阅！📋

让我们一起开始吧！现在，告诉我你的memorydump路径是什么呢？💭


好了，现在你只需要运行脚本，其他的事情就交给VolPro吧！我们会以可爱又活泼的方式帮你完成任务，你只需要坐等结果就好啦！🤗

''')
# 随机emoji
def random_emoji():
    emoji_list = ['🎉','🚀','📝','📁','📋','💭','🦄','🤗','💖']
    return random.choice(emoji_list)

#提示是否情况output文件夹,如果是则删除但保留summary.md，如果否则继续
if not os.path.exists("output"):
    os.mkdir("output")
while True:
    delete_output = input("🎀是否清空output文件夹？(y/n)")
    if delete_output == "y":
        shutil.rmtree("output")
        os.mkdir("output")
        break
    elif delete_output == "n":
        break
    else:
        print("[-] 请输入y或n！")

volatility_path = "vol.exe"
starttime = time.time()
try:
    memorydump_path = sys.argv[1]
except:
    sys.exit()

#获取剩下的未执行的任务
def get_remaining_tasks():
    remaining_tasks = []
    for task_name in tasks.keys():
        try:
            with open(f"output/{task_name}.txt", 'r') as f:
                pass
        except FileNotFoundError:
            remaining_tasks.append(task_name)
    return remaining_tasks

def run_command(command, task_name):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, shell=True, timeout=60)
        try:
            output = result.stdout.decode("UTF-8", errors="ignore")
        except:
            output = result.stdout.decode("ISO-8859-1", errors="ignore")
        #打印尚未执行的任务
        
        if output is not None:
            with open("output/{}.txt".format(task_name), "w") as f:
                f.write(output)
        else:
            print("[-] No output for task {}".format(task_name))
        remaining_tasks = get_remaining_tasks()
        if len(remaining_tasks) > 0:
            print(f"[*] {random_emoji()}尚未执行的任务：{','.join(remaining_tasks)}")
    except subprocess.TimeoutExpired:
        print(f"[-] {task_name} timed out after 60 seconds.")
    except Exception as e:
        print("[-] {} \n[-] Error while running command: {}".format(command,str(e)))
try:
    if sys.argv[3]=="dumpfiles":
        memlocal = sys.argv[3]
        command = [volatility_path, "-f", memorydump_path, "dumpfiles", "-Q", memlocal,"-D",'./']
        print("[*]🥰正在执行dumpfiles")
        dumpfiles_output = subprocess.run(command, stdout=subprocess.PIPE).stdout.decode("cp1252", errors="ignore")
        sys.exit(0)
except:
    pass
try:
    profile = sys.argv[2]
    print("[*] 🥰检测到Profile参数，正在跳过imageinfo")
except:
    print("[*] 🥰未检测到Profile，正在执行 imageinfo")
    command = [volatility_path, "-f", memorydump_path, "imageinfo"]
    imageinfo_output = subprocess.run(command, stdout=subprocess.PIPE).stdout.decode("cp1252", errors="ignore")
    lines = imageinfo_output.split("\n")
    for line in lines:
        if "Suggested Profile(s)" in line:
            suggested_profiles = line.split(":")[1].strip()
            profile = suggested_profiles.split(",")[0].strip()
            print("[+] 🥰设置的Profile: {}".format(profile))
            break
#tasklist = ["netscan","pslist","pstree","cmdscan","consoles","cmdline","editbox","clipboard","iehistory","hivelist","envars"]
#逐行读取tasklist.cfg，取每行 '-'分割的第一个参数作为任务名，后面为帮助
tasklist = []
tasklist_help = []
with open("tasklist.cfg", 'r',encoding = 'utf-8') as f:
    for line in f.readlines():
        tasklist.append(line.split('-')[0])
        tasklist_help.append(line.split('-')[1])

task_filescanlist = ["Desktop","Downloads",".zip","flag",'evtx']
task_filescanlist_help = ["桌面","下载","压缩包","flag",'日志']
tasks = {}
print(f"[*] 🥰正在生成任务列表，共导入{len(tasklist)+len(task_filescanlist)}个任务")
for task in tasklist:
    tasks[task] = ["--profile={}".format(profile), "-f", memorydump_path, task]
for task_filescan in task_filescanlist:
    tasks["filescan({})".format(task_filescan)] = ["--profile={}".format(profile), "-f", memorydump_path, "filescan", "|","findstr", task_filescan]
    
# tasks = {
#     "netscan": ["--profile={}".format(profile), "-f", memorydump_path, "netscan"],
#     "pslist": ["--profile={}".format(profile), "-f", memorydump_path, "pslist"],
#     "pstree": ["--profile={}".format(profile), "-f", memorydump_path, "pstree"],
#     "cmdscan": ["--profile={}".format(profile), "-f", memorydump_path, "cmdscan"],
#     "consoles": ["--profile={}".format(profile), "-f", memorydump_path, "consoles"],
#     "cmdline": ["--profile={}".format(profile), "-f", memorydump_path, "cmdline"],
#     "editbox": ["--profile={}".format(profile), "-f", memorydump_path, "editbox"],
#     "clipboard" : ["--profile={}".format(profile), "-f", memorydump_path, "malfind"],
#     "iehistory" : ["--profile={}".format(profile), "-f", memorydump_path, "iehistory"],
#     "hivelist" : ["--profile={}".format(profile), "-f", memorydump_path, "hivelist"],
#     "envars" : ["--profile={}".format(profile), "-f", memorydump_path, "envars"],
#     "filescan(Desktop)" : ["--profile={}".format(profile), "-f", memorydump_path, "filescan", "|","findstr", "Desktop"],
#     "filescan(Downloads)" : ["--profile={}".format(profile), "-f", memorydump_path, "filescan", "|","findstr", "Downloads"],
#     "filescan(zip)" : ["--profile={}".format(profile), "-f", memorydump_path, "filescan", "|","findstr", ".zip"],
#     "filescan(flag)" : ["--profile={}".format(profile), "-f", memorydump_path, "filescan", "|","findstr", "flag"],  
# }

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = {executor.submit(run_command, [volatility_path] + command, task_name): task_name for task_name, command in tasks.items()}
concurrent.futures.wait(futures)
print("[+] 🏆️全部任务已完成，即将进行文件合并!")
def generate_markdown():
    markdown = ""
    for task_name in tasks.keys():
        #标题加上tasklist.cfg文件中中的注释,'-'后面的内容
        try:
            markdown += f"# {task_name} \n## {tasklist_help[tasklist.index(task_name)]}\n"
        except:
            #filescan任务，对应关键词
            if "filescan" in task_name:
                markdown += f"# {task_name} \n## {task_filescanlist_help[task_filescanlist.index(task_name.split('(')[1].split(')')[0])]} \n"
        try:
            with open(f"output/{task_name}.txt", 'r') as f:
                markdown += f"```\n{f.read()}\n```\n"
        except FileNotFoundError:
            print(f"[-] File output/{task_name}.txt not found")
    with open("output/summary.md", 'w') as f:
        f.write(markdown)

endtime = time.time()
print("[+] 🕡️总共用时：",endtime-starttime)
print("[*] 🎀正在创建Markdown 汇总")
generate_markdown()
print("[+] 🏆️Markdown 汇总已生成在 summary.md 文件中")
