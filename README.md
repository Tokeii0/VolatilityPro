
# VolatilityPro 

**推荐使用 Python 3.10+ 版本**，其他版本可能存在未知的 bug。

---
正在重构之前写的太烂了，只是一个勉强能用的情况，能用但不好用，准备加一点新功能，敬请期待

![image](https://github.com/Tokeii0/VolatilityPro/assets/111427585/037e9f53-4394-418a-b963-c617c0b0b85a)
![image](https://github.com/Tokeii0/VolatilityPro/assets/111427585/407764cd-6929-4426-aa40-92e34f0a4e4c)


## 更新记录

### 2023.6.18
- 新增镜像字符串搜索功能
- 表格宽度自适应

![嘻嘻](https://github.com/Tokeii0/VolatilityPro/assets/111427585/8e90b625-8c96-4f8a-bbfc-4fd66e7fa743)

---

### 2023.6.12

![动画2](https://github.com/Tokeii0/VolatilityPro/assets/111427585/19e089bb-4f68-47a1-ab3c-020e52a74847)

---

### 2023.6.10 晚上
- 支持选择 filescan 文件

![new](https://github.com/Tokeii0/VolatilityPro/assets/111427585/cece18ca-39ce-44cc-8f74-8d880ae6315a)

---

### 2023.6.10 
- 新增 GUI 界面，即开即用

![image](https://github.com/Tokeii0/VolatilityPro/assets/111427585/9cc796c8-b1bc-4b3c-90ac-a07fc1ccb1ec)

---

## 老版本帮助

### 使用方法

```shell
python volpro.py [imagename] (profile) (dumpfiles)
```

参数解释：
- `[imagename]`：映像文件路径。📁
- `(profile)`：可选的 profile 参数。提供此参数时，将跳过 imageinfo 任务。
- `(dumpfiles)`：可选的 dumpfiles 参数。使用此参数时，必须提供 profile 参数。

#### 示例

```shell
# 没有 profile，自动选择 imageinfo 的第一个
python Volpro.py ADMIN-PC-20220616-025554.raw

# 设置了 profile，跳过 imageinfo 节约时间
python Volpro.py ADMIN-PC-20220616-025554.raw Win7SP1x64

# dumpfiles 命令的使用方法
python Volpro.py ADMIN-PC-20220616-025554.raw Win7SP1x64 dumpfiles 0x000000007dcc4480
```

![image](https://github.com/Tokeii0/VolatilityPro/assets/111427585/d6917be9-6011-4e16-8d44-1d402e3131ab)

![image](https://github.com/Tokeii0/VolatilityPro/assets/111427585/a45582c1-c35f-4639-b133-5cff5f4e5c14)

![image](https://github.com/Tokeii0/VolatilityPro/assets/111427585/7bac9eb3-312e-4732-9d6c-6707cf869f97)
