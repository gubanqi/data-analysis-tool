# 成绩分析工具

这是一个使用 Python 分析 Excel 成绩数据的小项目。

## 功能

- 读取 Excel 成绩表
- 计算学生总分、平均分和排名
- 计算各科平均分
- 生成成绩分析结果表
- 生成平均分柱状图

## 输入文件

程序读取：

data/scores.xlsx

表格必须包含以下列：

- 姓名
- 语文
- 数学
- 英语

## 安装依赖

python -m pip install -r requirements.txt

## 运行程序

python main.py

## 输出文件

- results/成绩分析结果.xlsx
- figures/各科平均分.png

## 使用技术

- Python
- pandas
- openpyxl
- matplotlib