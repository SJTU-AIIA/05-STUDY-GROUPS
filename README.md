欢迎来到AI创协开发的共学项目管理中心！每个共学小组都有自己的项目管理器，同学们可以在这里部署代码，方便与他人分享或展示成果 :O

### 其他语言 Other Languages：
[English README.md Version](https://github.com/SJTU-AIIA/02-PROJECTS/blob/main/locales/EN-US/README.md)

# 新手操作指南：

### 初始步骤  
若还未安装，安装 AIIA-CLI（共学部开发的项目管理工具）  
```bash  
pip install --upgrade aiia-cli  
```  
用git clone或Github Desktop等软件，进入 `05-STUDY-GROUPS` 仓库根目录打开命令行  

```bash
cd SG2025-xx-xx_YOUR-STUDYGROUP
```
cd进入你已经报名的共学小组

```bash
proj-cli sgroup self-register real_name
```
输入这行命令，名字写自己真名（例: 伯涵峥 -> bohanzheng，Emmanuel Macron -> emmanuelmacron），即可“开户”，在学习小组`/studyspace`中可查看到自己的文件夹。

今后所有这个共学小组的项目都可以在github中完成，方便分享、查错、交流等。

PROJ-CLI中`proj-cli deploy`和`proj-cli run`均可正常使用。

# STUDY-GROUPS功能介绍
`05-STUDY-GROUPS`是建立在[02-PROJECTS](https://github.com/SJTU-AIIA/02-PROJECTS)之上的一套直观的共学系统。所有的全大写文件(`README.md`， `STUDYGROUPS.md`, `REGISTRY.md`)都做了可视化，可供同学们查阅。
- `README.md`：studyspace中每个同学的项目文件夹中都有一个`README.md`。此文件无系统作用（有系统效力的是`_manifest.json`），但可以写自己想要别人看到的内容，如个人介绍，项目介绍，QNA等。
- `STUDYGROUPS.md`：在根目录下。`STUDYGROUPS.md`记录了存在仓库里的所有共学小组及其信息，供同学们查阅。
- `REGISTRY.md`

# STUDY-GROUPS权限
GITHUB的一大优点就是所有同学都可以看到各自的代码，相互促进与借鉴，强大的commit系统亦可以跟踪同学们的学习进度，让学习更高效。但同时，为了避免同学们误操作删除重要信息，权限开放如下：
每个学习小组内登记的所有同学都可以随意更改自己的文件夹，但若老师或同学们commit中更改了其他同学文件夹中的内容，将会为该同学发出pull-request，该同学同意后才能成功更改内容。这样能避免同学们误删他人的劳动成果（当然，github的东西真的要删也不容易，历史保存的很好）

本仓库还在试运营阶段。若出现bug或想提出建议，可在Github中上栏选择Issues并提出，亦可直接微信/飞书联系负责人。希望我们的共学小组可以越办越好！