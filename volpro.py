import concurrent.futures
import subprocess
import sys
import time
import os
import random

# 随机emoji
def random_emoji():
    emoji_list = ['🎉', '🚀', '📝', '📁', '📋', '💭', '🦄', '🤗', '💖']
    return random.choice(emoji_list)

def get_remaining_tasks(output_path, tasks):
    remaining_tasks = []
    for task_name in tasks.keys():
        try:
            with open(os.path.join(output_path, f"{task_name}.txt"), 'r') as f:
                pass
        except FileNotFoundError:
            remaining_tasks.append(task_name)
    return remaining_tasks

def run_command(command, task_name, output_path, tasks):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, shell=True, timeout=60)
        try:
            output = result.stdout.decode("UTF-8", errors="ignore")
        except:
            output = result.stdout.decode("ISO-8859-1", errors="ignore")
        if output is not None:
            with open(os.path.join(output_path, f"{task_name}.txt"), "w") as f:
                f.write(output)
        else:
            print("[-] No output for task {}".format(task_name))
        remaining_tasks = get_remaining_tasks(output_path, tasks)
        if len(remaining_tasks) > 0:
            print(f"[*] {random_emoji()}尚未执行的任务:{','.join(remaining_tasks)}")
    except subprocess.TimeoutExpired:
        print(f"[-] {task_name} timed out after 60 seconds.")
    except Exception as e:
        print("[-] {} \n[-] Error while running command: {}".format(command, str(e)))

def generate_markdown(tasks, output_path, tasklist, tasklist_help, task_filescanlist, task_filescanlist_help):
    markdown = ""
    for task_name in tasks.keys():
        try:
            markdown += f"# {task_name} \n## {tasklist_help[tasklist.index(task_name)]}\n"
        except:
            if "filescan" in task_name:
                markdown += f"# {task_name} \n## {task_filescanlist_help[task_filescanlist.index(task_name.split('(')[1].split(')')[0])]} \n"
        try:
            with open(os.path.join(output_path, f"{task_name}.txt"), 'r') as f:
                markdown += f"```\n{f.read()}\n```\n"
        except FileNotFoundError:
            print(f"[-] File {os.path.join(output_path, f'{task_name}.txt')} not found")
    with open(os.path.join(output_path, "summary.md"), 'w', encoding='utf-8') as f:
        f.write(markdown)


def main():
    continuerun = 1    
    volatility_path = "vol.exe"
    starttime = time.time()

    try:
        memorydump_path = sys.argv[1]
    except:
        sys.exit()

    # 提示是否情况output文件夹,如果是则删除但保留summary.md,如果否则继续
    output_path = os.path.join(os.path.dirname(memorydump_path), 'output')
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    # 省略部分代码...

    try:
        profile = sys.argv[2]
        if sys.argv[3] == "dumpfiles":
            continuerun = 0
            memlocal = sys.argv[4]
            command = [volatility_path, "-f", memorydump_path,"--profile={}".format(profile), "dumpfiles", "-Q", memlocal, "-D", './']
            print("[*]🥰正在执行dumpfiles")
            dumpfiles_output = subprocess.run(command, stdout=subprocess.PIPE).stdout.decode("cp1252", errors="ignore")
            print(dumpfiles_output)
            print("[+] 🏆️dumpfiles任务完毕!")
    except :
        pass

    if continuerun == 1:
        try:
            profile = sys.argv[2]
            print("[*] 🥰检测到Profile参数,正在跳过imageinfo")
        except:
            print("[*] 🥰未检测到Profile,正在执行 imageinfo")
            command = [volatility_path, "-f", memorydump_path, "imageinfo"]
            imageinfo_output = subprocess.run(command, stdout=subprocess.PIPE).stdout.decode("cp1252", errors="ignore")
            lines = imageinfo_output.split("\n")
            for line in lines:
                if "Suggested Profile(s)" in line:
                    suggested_profiles = line.split(":")[1].strip()
                    profile = suggested_profiles.split(",")[0].strip()
                    print("[+] 🥰设置的Profile: {}".format(profile))
                    break

        tasklist = []
        tasklist_help = []
        with open("tasklist.cfg", 'r', encoding='utf-8') as f:
            for line in f.readlines():
                tasklist.append(line.split('-')[0])
                tasklist_help.append(line.split('-')[1])

        task_filescanlist = ["Desktop", "Downloads", ".zip", "flag", 'evtx']
        task_filescanlist_help = ["桌面", "下载", "压缩包", "flag", '日志']
        tasks = {}
        print(f"[*] 🥰正在生成任务列表,共导入{len(tasklist) + len(task_filescanlist)}个任务")
        for task in tasklist:
            tasks[task] = ["--profile={}".format(profile), "-f", memorydump_path, task]
        for task_filescan in task_filescanlist:
            tasks["filescan({})".format(task_filescan)] = ["--profile={}".format(profile), "-f", memorydump_path, "filescan",
                                                        "|", "findstr", task_filescan]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(run_command, [volatility_path] + command, task_name, output_path, tasks): task_name for task_name, command in
                    tasks.items()}
        concurrent.futures.wait(futures)
        print("[+] 🏆️全部任务已完成,即将进行文件合并!")

        endtime = time.time()
        print("[+] 🕡️总共用时:", endtime - starttime)
        print("[*] 🎀正在创建Markdown 汇总")
        generate_markdown(tasks, output_path, tasklist, tasklist_help, task_filescanlist, task_filescanlist_help)
        print("[+] 🏆️Markdown 汇总已生成在 summary.md 文件中")


if __name__ == '__main__':
    main()
