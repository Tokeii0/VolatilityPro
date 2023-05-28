import concurrent.futures
import subprocess
import sys
import time

volatility_path = "volatility_2.6_win64_standalone.exe" 
starttime = time.time()
try:
    memorydump_path = sys.argv[1]
except:
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

如果你有任何问题或需要进一步的帮助，随时告诉我哦！我会尽力解答你的疑问。祝你使用愉快！💖
''')
    sys.exit()



def run_command(command, task_name):
    try:
        #print(command)
        result = subprocess.run(command, stdout=subprocess.PIPE,shell=True)
        try:
            output = result.stdout.decode("UTF-8", errors="ignore")
        except:
            output = result.stdout.decode("ISO-8859-1", errors="ignore")
        
        if output is not None:
            with open("output/{}.txt".format(task_name), "w") as f:
                f.write(output)
        else:
            print("[-] No output for task {}".format(task_name))
    except Exception as e:
        print("[-] {} \n[-] Error while running command: {}".format(command,str(e)))
try:
    if sys.argv[3]=="dumpfiles":
        memlocal = sys.argv[4]
        command = [volatility_path, "-f", memorydump_path, '--profile={}'.format(sys.argv[2]), "dumpfiles", "-Q", memlocal,"-D",'./output']
        print(' '.join(command))
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

tasks = {
    "netscan": ["--profile={}".format(profile), "-f", memorydump_path, "netscan"],
    "pslist": ["--profile={}".format(profile), "-f", memorydump_path, "pslist"],
    "pstree": ["--profile={}".format(profile), "-f", memorydump_path, "pstree"],
    "cmdscan": ["--profile={}".format(profile), "-f", memorydump_path, "cmdscan"],
    "consoles": ["--profile={}".format(profile), "-f", memorydump_path, "consoles"],
    "cmdline": ["--profile={}".format(profile), "-f", memorydump_path, "cmdline"],
    "editbox": ["--profile={}".format(profile), "-f", memorydump_path, "editbox"],
    "clipboard" : ["--profile={}".format(profile), "-f", memorydump_path, "malfind"],
    "iehistory" : ["--profile={}".format(profile), "-f", memorydump_path, "iehistory"],
    "hivelist" : ["--profile={}".format(profile), "-f", memorydump_path, "hivelist"],
    "filescan(Desktop)" : ["--profile={}".format(profile), "-f", memorydump_path, "filescan", "|","findstr", "Desktop"],
    "filescan(Downloads)" : ["--profile={}".format(profile), "-f", memorydump_path, "filescan", "|","findstr", "Downloads"],
    "filescan(zip)" : ["--profile={}".format(profile), "-f", memorydump_path, "filescan", "|","findstr", ".zip"],
    "filescan(flag)" : ["--profile={}".format(profile), "-f", memorydump_path, "filescan", "|","findstr", "flag"],
    
}

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = {executor.submit(run_command, [volatility_path] + command, task_name): task_name for task_name, command in tasks.items()}
concurrent.futures.wait(futures)
print("[+] 🏆️All tasks completed!")
def generate_markdown():
    markdown = ""
    for task_name in tasks.keys():
        markdown += f"# {task_name}\n"
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
print("[+] 🏆️Markdown summary generated in summary.md")
