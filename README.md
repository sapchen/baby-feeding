# 婴儿喂养记录管理工具

一个通用的婴儿喂养记录管理 Python 包，可作为独立工具、命令行应用或集成到各种 IDE/Skill 平台（如 Trae、CodeBuddy、Cursor、Qoder 等）。

## 功能特性

- **饮食记录**：记录母乳喂养、配方奶、米粉摄入量，以及补剂（AD/D3）和体温
- **便便记录**：记录便便的量、颜色、形状等信息
- **护理记录**：记录护理项目（洗澡、排气操、被动操、外出等）
- **数据统计**：每日/每周喂养量统计分析
- **数据持久化**：使用 Excel 文件存储数据
- **多平台支持**：可作为独立工具或集成到各种 IDE/Skill 平台

## 安装方式

### 使用 pip 安装

```bash
pip install baby-feeding
```

### 从源码安装

```bash
git clone https://github.com/example/baby-feeding.git
cd baby-feeding
pip install .
```

## 使用方式

### 1. 命令行工具

安装后直接运行：

```bash
baby-feeding
```

或使用 Python 模块方式：

```bash
python -m baby_feeding.cli
```

### 2. 作为 Python 模块使用

```python
from baby_feeding import (
    add_feeding_record,
    add_poop_record,
    add_care_record,
    get_daily_summary,
    get_recent_records,
    search_records
)

# 添加喂养记录
add_feeding_record(
    breast_milk=110,
    formula_milk=0,
    rice_flour=2.5,
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

# 获取最近记录
print(get_recent_records(5))

# 搜索记录
print(search_records("洗澡"))
```

### 3. 作为 Skill 集成

该工具可轻松集成到各种 IDE/Skill 平台：

```python
# 示例：通用 Skill 调用接口
def handle_skill_request(request):
    """处理来自各种平台的 Skill 请求"""
    action = request.get("action")
    
    if action == "add_feeding":
        return add_feeding_record(
            breast_milk=request.get("breast_milk", 0),
            formula_milk=request.get("formula_milk", 0),
            rice_flour=request.get("rice_flour", 0),
            supplements=request.get("supplements"),
            temperature=request.get("temperature"),
            notes=request.get("notes")
        )
    
    elif action == "add_poop":
        return add_poop_record(
            amount=request.get("amount"),
            color=request.get("color"),
            consistency=request.get("consistency"),
            notes=request.get("notes")
        )
    
    elif action == "add_care":
        return add_care_record(
            period=request.get("period"),
            item=request.get("item"),
            time_range=request.get("time_range"),
            notes=request.get("notes")
        )
    
    elif action == "daily_summary":
        return get_daily_summary(request.get("date"))
    
    elif action == "recent_records":
        return get_recent_records(request.get("count", 5))
    
    elif action == "search":
        return search_records(request.get("keyword"))
    
    return "未知操作"
```

## 项目结构

```
.
├── baby_feeding/
│   ├── __init__.py      # 模块入口，导出公共 API
│   ├── core.py          # 核心功能实现
│   └── cli.py           # 命令行界面入口
├── pyproject.toml       # 包配置文件（支持 pip 安装）
├── requirements.txt     # 依赖声明
├── README.md            # 项目说明文档
├── SKILL.md             # Skill 元数据（可选）
├── LICENSE              # MIT开源许可证
└── .gitignore          # Git忽略配置
```

## API 参考

### 饮食记录函数

| 函数 | 说明 |
|------|------|
| `add_feeding_record(breast_milk, formula_milk, rice_flour, supplements, temperature, notes)` | 添加喂养记录 |
| `get_records_by_date(date_str)` | 获取指定日期的喂养记录 |
| `get_weekly_summary(start_date, end_date)` | 获取周总结 |

### 便便记录函数

| 函数 | 说明 |
|------|------|
| `add_poop_record(amount, color, consistency, notes)` | 添加便便记录 |
| `get_poop_records_by_date(date_str)` | 获取指定日期的便便记录 |

### 护理记录函数

| 函数 | 说明 |
|------|------|
| `add_care_record(period, item, time_range, notes)` | 添加护理记录 |
| `get_care_records_by_date(date_str)` | 获取指定日期的护理记录 |

### 综合查询函数

| 函数 | 说明 |
|------|------|
| `get_daily_summary(date_str)` | 获取每日综合总结 |
| `get_recent_records(count)` | 获取最近记录 |
| `search_records(keyword)` | 搜索记录 |

## 数据文件

所有数据存储在 `baby_feeding_data.xlsx` 文件中，包含三个工作表：

| 工作表 | 字段 |
|--------|------|
| 饮食 | 时间戳、母乳（ml）、配方奶（ml）、米粉（g）、总奶量、补剂、今日体温、备注 |
| 便便 | 时间戳、量（多/中/少）、颜色、形状（干/稀）、其他 |
| 护理 | 日期、时段、项目、时间段、备注 |

## 技术栈

- Python 3.8+
- pandas - 数据处理
- openpyxl - Excel 文件读写

## 许可证

MIT License
