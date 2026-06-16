# 婴儿喂养记录管理系统

一个基于Python的婴儿喂养记录管理工具，支持记录和管理婴儿的饮食、便便和护理记录。

## 功能特点

- **饮食记录**：记录母乳喂养、配方奶、米粉摄入量，以及补剂和体温
- **便便记录**：记录便便的量、颜色、形状等信息
- **护理记录**：记录护理项目（洗澡、排气操、被动操等）
- **数据统计**：每日/每周喂养量统计分析
- **数据持久化**：使用Excel文件存储数据，支持多sheet管理
- **命令行界面**：提供友好的交互式命令行操作界面

## 技术栈

- Python 3.x
- pandas - 数据处理
- openpyxl - Excel文件读写

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行命令行界面

```bash
python cli.py
```

### 作为模块使用

```python
from baby_feeding import (
    add_feeding_record,
    add_poop_record,
    add_care_record,
    get_daily_summary,
    get_recent_records
)

# 添加喂养记录
add_feeding_record(
    breast_milk=110,
    formula_milk=0,
    rice_flour=0,
    supplements="AD",
    temperature=36.5
)

# 添加便便记录
add_poop_record(
    amount="多",
    color="黄",
    consistency="稀"
)

# 添加护理记录
add_care_record(
    period="上午",
    item="洗澡",
    time_range="10:00-10:30"
)

# 获取每日总结
print(get_daily_summary())
```

## 项目结构

```
.
├── baby_feeding/              # 核心模块
│   ├── __init__.py           # 模块入口
│   └── core.py               # 核心功能实现
├── cli.py                    # 命令行界面入口
├── test_baby_feeding.py      # 单元测试
├── sample_data.xlsx          # 示例数据文件
├── README.md                 # 项目说明文档
├── requirements.txt          # 依赖声明
├── LICENSE                   # MIT开源许可证
└── .gitignore               # Git忽略配置
```

## 数据文件格式

数据存储在 `baby_feeding_data.xlsx` 文件中，包含三个sheet：

### 饮食记录
| 字段 | 类型 | 说明 |
|------|------|------|
| 时间戳 | 日期时间 | 喂养记录时间 |
| 母乳（ml） | 数字 | 母乳喂养量 |
| 配方奶（ml） | 数字 | 配方奶喂养量 |
| 米粉（g） | 数字 | 米粉喂养量 |
| 总奶量 | 数字 | 总喂养量 |
| 补剂 | 文本 | 补充剂类型 |
| 今日体温 | 数字 | 婴儿体温 |
| 备注 | 文本 | 备注信息 |

### 便便记录
| 字段 | 类型 | 说明 |
|------|------|------|
| 时间戳 | 日期时间 | 记录时间 |
| 量（多/中/少） | 文本 | 便便量 |
| 颜色 | 文本 | 便便颜色 |
| 形状（干/稀） | 文本 | 便便形状 |
| 其他 | 文本 | 备注信息 |

### 护理记录
| 字段 | 类型 | 说明 |
|------|------|------|
| 日期 | 日期 | 护理日期 |
| 时段 | 文本 | 护理时段 |
| 项目 | 文本 | 护理项目 |
| 时间段 | 文本 | 具体时间范围 |
| 备注 | 文本 | 备注信息 |

## 使用示例

### 添加喂养记录

```python
add_feeding_record(
    timestamp="2024-12-12 09:00:00",
    breast_milk=110,
    formula_milk=0,
    rice_flour=5.0,
    supplements="AD",
    temperature=36.5,
    notes="上午喂养"
)
```

### 查询每日总结

```python
summary = get_daily_summary("2024-12-12")
print(summary)
```

### 搜索记录

```python
results = search_records("洗澡")
print(results)
```

## 命令行界面

运行 `python cli.py` 后，系统提供以下菜单选项：

1. 添加喂养记录
2. 查询当日喂养记录
3. 查询指定日期喂养记录
4. 每日喂养总结
5. 周喂养总结
6. 添加便便记录
7. 查询当日便便记录
8. 查询指定日期便便记录
9. 添加护理记录
10. 查询当日护理记录
11. 查询指定日期护理记录
12. 最近记录
13. 搜索记录
0. 退出

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request！

## 联系方式

如有问题或建议，请通过GitHub Issues联系。
