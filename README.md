# VolatilityPro ![10A2CDC8](https://github.com/Tokeii0/VolatilityPro/assets/111427585/cb6d8b58-2923-4147-9ac7-9491678af765)

## 最好使用3.10+版本python 其他版本可能有莫名奇妙bug

## 2023.6.18 更新一下 新增了个镜像字符串搜索功能 顺便表格宽度自适应也加上去了

![嘻嘻](https://github.com/Tokeii0/VolatilityPro/assets/111427585/8e90b625-8c96-4f8a-bbfc-4fd66e7fa743)

------------------------------------------
## 2023.6.12 更新一下

![动画2](https://github.com/Tokeii0/VolatilityPro/assets/111427585/19e089bb-4f68-47a1-ab3c-020e52a74847)


------------------------------------------
## 2023.6.10 晚上更新一下
支持选择filescan文件了
![new](https://github.com/Tokeii0/VolatilityPro/assets/111427585/cece18ca-39ce-44cc-8f74-8d880ae6315a)

------------------------------------------
## 2023.6.10 更新
方便大伙使用整了个GUI界面，即开即用
![image](https://github.com/Tokeii0/VolatilityPro/assets/111427585/9cc796c8-b1bc-4b3c-90ac-a07fc1ccb1ec)




下面是老版本帮助了
------------------------------------------
## 帮助 

```shell
python volpro.py [imagename] (profile) (dumpfiles)
```
- `[imagename]`：你的映像文件路径。！📁
- `(profile)`：可选的profile参数。如果你提供了它，我们会跳过imageinfo任务。
- `(dumpfiles)`：可选的dumpfiles参数。如果你想使用它，一定要提供profile参数。

### 比如
```shell
# 没有profile 自动取imageinfo第一个
python Volpro.py ADMIN-PC-20220616-025554.raw
# 设置了profile 跳过节约时间
python Volpro.py ADMIN-PC-20220616-025554.raw Win7SP1x64
# dumpfiles命令使用方法
python Volpro.py ADMIN-PC-20220616-025554.raw Win7SP1x64 dumpfiles 0x000000007dcc4480
```

![image](https://github.com/Tokeii0/VolatilityPro/assets/111427585/d6917be9-6011-4e16-8d44-1d402e3131ab)

![image](https://github.com/Tokeii0/VolatilityPro/assets/111427585/a45582c1-c35f-4639-b133-5cff5f4e5c14)

![image](https://github.com/Tokeii0/VolatilityPro/assets/111427585/7bac9eb3-312e-4732-9d6c-6707cf869f97)
