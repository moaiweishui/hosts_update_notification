# hosts_update_notification
- 对[老D博客hosts更新页](https://laod.cn/hosts/2017-google-hosts.html)进行定时爬取，若检测到hosts文件有更新，则发送邮件至指定邮箱进行提醒
- windows平台可以通过pyInstaller将python文件打包成exe文件，设置为定时任务，进行监控
## Introduction
- Python 2.X

## Project framework
- **main.py**：主函数
- **get_update_info.py**：爬取hosts更新页面，获得更新日期
- **push_update_info.py**：发送E-mail至指定邮箱
- **content_parsing.py**：信息提取工具

## Todo
- [ ] 自动下载最新的hosts文件，并以附件的形式随邮件发送至目标邮箱
- [ ] 代码重构
