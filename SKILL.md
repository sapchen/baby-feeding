---
name: "baby-feeding"
description: "婴儿喂养记录管理技能，支持记录和查询母乳喂养、配方奶、米粉摄入，以及便便、护理记录。当用户需要记录婴儿喂养信息、便便情况或护理内容时调用此技能。"
---

# 婴儿喂养记录管理

## 功能概述

该技能用于管理婴儿的饮食、便便和护理记录，支持以下功能：

## 数据表格

### 饮食记录

| 字段 | 类型 | 说明 |
|------|------|------|
| 时间戳 | 日期时间 | 喂养记录的时间 |
| 母乳（ml） | 数字 | 母乳喂养量（毫升） |
| 配方奶（ml） | 数字 | 配方奶喂养量（毫升） |
| 米粉（g） | 数字 | 米粉喂养量（克） |
| 总奶量 | 数字 | 总喂养量（毫升） |
| 补剂 | 文本 | 补充剂类型（如AD、D3） |
| 今日体温 | 数字 | 婴儿体温 |
| 备注 | 文本 | 备注信息 |

### 便便记录

| 字段 | 类型 | 说明 |
|------|------|------|
| 时间戳 | 日期时间 | 记录时间 |
| 量（多/中/少） | 文本 | 便便量 |
| 颜色 | 文本 | 便便颜色（如黄、黄绿） |
| 形状（干/稀） | 文本 | 便便形状 |
| 其他 | 文本 | 备注信息 |

### 护理记录

| 字段 | 类型 | 说明 |
|------|------|------|
| 日期 | 日期 | 护理日期 |
| 时段 | 文本 | 护理时段（上午/下午/晚上） |
| 项目 | 文本 | 护理项目（洗澡/排气操/被动操/外出等） |
| 时间段 | 文本 | 具体时间范围 |
| 备注 | 文本 | 备注信息 |

## 主要功能

### 饮食记录
1. **添加喂养记录** - 记录单次喂养的详细信息
2. **查询喂养记录** - 根据日期查询历史记录
3. **每日总结** - 统计当日喂养情况
4. **周总结** - 统计一周喂养情况

### 便便记录
5. **添加便便记录** - 记录便便的量、颜色、形状等信息
6. **查询便便记录** - 根据日期查询历史记录

### 护理记录
7. **添加护理记录** - 记录护理项目和时间
8. **查询护理记录** - 根据日期查询历史记录

### 综合功能
9. **最近记录** - 查看最近的所有类型记录
10. **搜索记录** - 根据关键词搜索所有记录

## 使用场景

当用户需要：
- 记录婴儿的母乳喂养、配方奶喂养或辅食喂养
- 记录婴儿的便便情况
- 记录婴儿的护理项目（洗澡、排气操、被动操等）
- 查询特定日期的喂养、便便或护理历史
- 查看每日或每周的喂养量统计

## 数据来源

记录存储在Excel文件的三个sheet中：
- `饮食` - 喂养记录
- `便便` - 便便记录  
- `护理` - 护理记录

支持读取和写入操作。

## 项目结构

```
.
├── baby_feeding/              # 核心模块
│   ├── __init__.py           # 模块入口
│   └── core.py               # 核心功能实现
├── cli.py                    # 命令行界面入口
├── test_baby_feeding.py      # 单元测试
├── sample_data.xlsx          # 示例数据文件
├── SKILL.md                  # 技能说明文档
├── README.md                 # 项目说明文档
├── requirements.txt          # 依赖声明
├── LICENSE                   # MIT开源许可证
└── .gitignore               # Git忽略配置
```

## 安装和使用

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行命令行界面

```bash
python cli.py
```

### 作为Python模块使用

```python
from baby_feeding import (
    add_feeding_record,
    add_poop_record,
    add_care_record,
    get_records_by_date,
    get_poop_records_by_date,
    get_care_records_by_date,
    get_daily_summary,
    get_weekly_summary,
    get_recent_records,
    search_records
)

# 添加喂养记录
add_feeding_record(
    timestamp="2024-12-12 09:00:00",
    breast_milk=110,
    formula_milk=0,
    rice_flour=0,
    supplements="AD",
    temperature=36.5,
    notes=""
)

# 添加便便记录
add_poop_record(
    timestamp="2024-12-12 10:00:00",
    amount="多",
    color="黄",
    consistency="稀",
    notes=""
)

# 添加护理记录
add_care_record(
    date="2024-12-12",
    period="上午",
    item="洗澡",
    time_range="10:00-10:30",
    notes=""
)

# 获取每日综合总结
print(get_daily_summary("2024-12-12"))

# 获取最近记录
print(get_recent_records(5))
```

## API参考

### 饮食记录函数

- `add_feeding_record(timestamp, breast_milk, formula_milk, rice_flour, supplements, temperature, notes)` - 添加喂养记录
- `get_records_by_date(date_str)` - 获取指定日期的喂养记录
- `get_weekly_summary(start_date, end_date)` - 获取周总结

### 便便记录函数

- `add_poop_record(timestamp, amount, color, consistency, notes)` - 添加便便记录
- `get_poop_records_by_date(date_str)` - 获取指定日期的便便记录

### 护理记录函数

- `add_care_record(date, period, item, time_range, notes)` - 添加护理记录
- `get_care_records_by_date(date_str)` - 获取指定日期的护理记录

### 综合查询函数

- `get_daily_summary(date_str)` - 获取每日综合总结
- `get_recent_records(count)` - 获取最近记录
- `search_records(keyword)` - 搜索记录

## 测试

运行单元测试：

```bash
python -m unittest test_baby_feeding -v
```

## 许可证

MIT License
