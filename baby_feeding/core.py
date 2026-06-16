import pandas as pd
import os
from datetime import datetime

EXCEL_FILE = "baby_feeding_data.xlsx"

def load_sheet(sheet_name):
    if os.path.exists(EXCEL_FILE):
        df = pd.read_excel(EXCEL_FILE, sheet_name=sheet_name)
        if '时间戳' in df.columns:
            df['时间戳'] = pd.to_datetime(df['时间戳'])
        if '日期' in df.columns:
            df['日期'] = pd.to_datetime(df['日期'])
        return df
    return None

def save_sheets(sheets):
    with pd.ExcelWriter(EXCEL_FILE) as writer:
        for sheet_name, df in sheets.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

def load_records():
    df = load_sheet('饮食')
    if df is None or df.empty:
        return pd.DataFrame(columns=['时间戳', '母乳（ml）', '配方奶（ml）', '米粉（g）', '总奶量', '补剂', '今日体温', '备注'])
    return df

def load_poop_records():
    df = load_sheet('便便')
    if df is None or df.empty:
        return pd.DataFrame(columns=['时间戳', '量（多/中/少）', '颜色', '形状（干/稀）', '其他'])
    return df

def load_care_records():
    df = load_sheet('护理')
    if df is None or df.empty:
        return pd.DataFrame(columns=['日期', '时段', '项目', '时间段', '备注'])
    return df

def save_records(df):
    if os.path.exists(EXCEL_FILE):
        sheets = {}
        xls = pd.ExcelFile(EXCEL_FILE)
        for sheet in xls.sheet_names:
            sheets[sheet] = pd.read_excel(xls, sheet)
    else:
        sheets = {'饮食': pd.DataFrame(), '便便': pd.DataFrame(), '护理': pd.DataFrame()}
    sheets['饮食'] = df
    save_sheets(sheets)

def save_poop_records(df):
    if os.path.exists(EXCEL_FILE):
        sheets = {}
        xls = pd.ExcelFile(EXCEL_FILE)
        for sheet in xls.sheet_names:
            sheets[sheet] = pd.read_excel(xls, sheet)
    else:
        sheets = {'饮食': pd.DataFrame(), '便便': pd.DataFrame(), '护理': pd.DataFrame()}
    sheets['便便'] = df
    save_sheets(sheets)

def save_care_records(df):
    if os.path.exists(EXCEL_FILE):
        sheets = {}
        xls = pd.ExcelFile(EXCEL_FILE)
        for sheet in xls.sheet_names:
            sheets[sheet] = pd.read_excel(xls, sheet)
    else:
        sheets = {'饮食': pd.DataFrame(), '便便': pd.DataFrame(), '护理': pd.DataFrame()}
    sheets['护理'] = df
    save_sheets(sheets)

def add_feeding_record(timestamp=None, breast_milk=0, formula_milk=0, rice_flour=0, supplements=None, temperature=None, notes=None):
    df = load_records()
    
    if timestamp is None:
        timestamp = datetime.now()
    elif isinstance(timestamp, str):
        timestamp = pd.to_datetime(timestamp)
    
    total_milk = breast_milk + formula_milk
    
    new_record = pd.DataFrame({
        '时间戳': [timestamp],
        '母乳（ml）': [breast_milk],
        '配方奶（ml）': [formula_milk],
        '米粉（g）': [rice_flour],
        '总奶量': [total_milk],
        '补剂': [supplements],
        '今日体温': [temperature],
        '备注': [notes]
    })
    
    df = pd.concat([df, new_record], ignore_index=True)
    save_records(df)
    return "喂养记录添加成功！"

def add_poop_record(timestamp=None, amount=None, color=None, consistency=None, notes=None):
    df = load_poop_records()
    
    if timestamp is None:
        timestamp = datetime.now()
    elif isinstance(timestamp, str):
        timestamp = pd.to_datetime(timestamp)
    
    new_record = pd.DataFrame({
        '时间戳': [timestamp],
        '量（多/中/少）': [amount],
        '颜色': [color],
        '形状（干/稀）': [consistency],
        '其他': [notes]
    })
    
    df = pd.concat([df, new_record], ignore_index=True)
    save_poop_records(df)
    return "便便记录添加成功！"

def add_care_record(date=None, period=None, item=None, time_range=None, notes=None):
    df = load_care_records()
    
    if date is None:
        date = datetime.now().date()
    elif isinstance(date, str):
        date = pd.to_datetime(date).date()
    
    new_record = pd.DataFrame({
        '日期': [date],
        '时段': [period],
        '项目': [item],
        '时间段': [time_range],
        '备注': [notes]
    })
    
    df = pd.concat([df, new_record], ignore_index=True)
    save_care_records(df)
    return "护理记录添加成功！"

def get_records_by_date(date_str):
    df = load_records()
    if df.empty:
        return "暂无喂养记录"
    
    target_date = pd.to_datetime(date_str).date()
    df['日期'] = df['时间戳'].dt.date
    filtered = df[df['日期'] == target_date]
    
    if filtered.empty:
        return f"{date_str} 暂无喂养记录"
    
    result = f"{date_str} 喂养记录：\n"
    for _, row in filtered.iterrows():
        time_str = row['时间戳'].strftime('%H:%M')
        result += f"- {time_str}: 母乳{row['母乳（ml）']}ml, 配方奶{row['配方奶（ml）']}ml, 米粉{row['米粉（g）']}g"
        if pd.notna(row['补剂']):
            result += f", 补剂:{row['补剂']}"
        if pd.notna(row['今日体温']):
            result += f", 体温:{row['今日体温']}℃"
        result += "\n"
    
    daily_total = filtered['总奶量'].sum()
    result += f"\n当日总奶量: {daily_total}ml"
    return result

def get_poop_records_by_date(date_str):
    df = load_poop_records()
    if df.empty:
        return "暂无便便记录"
    
    target_date = pd.to_datetime(date_str).date()
    df['日期'] = df['时间戳'].dt.date
    filtered = df[df['日期'] == target_date]
    
    if filtered.empty:
        return f"{date_str} 暂无便便记录"
    
    result = f"{date_str} 便便记录：\n"
    for _, row in filtered.iterrows():
        time_str = row['时间戳'].strftime('%H:%M')
        result += f"- {time_str}: "
        if pd.notna(row['量（多/中/少）']):
            result += f"量:{row['量（多/中/少）']}"
        if pd.notna(row['颜色']):
            result += f", 颜色:{row['颜色']}"
        if pd.notna(row['形状（干/稀）']):
            result += f", 形状:{row['形状（干/稀）']}"
        if pd.notna(row['其他']):
            result += f", 其他:{row['其他']}"
        result += "\n"
    
    return result

def get_care_records_by_date(date_str):
    df = load_care_records()
    if df.empty:
        return "暂无护理记录"
    
    target_date = pd.to_datetime(date_str).date()
    df['日期'] = df['日期'].dt.date
    filtered = df[df['日期'] == target_date]
    
    if filtered.empty:
        return f"{date_str} 暂无护理记录"
    
    result = f"{date_str} 护理记录：\n"
    for _, row in filtered.iterrows():
        result += f"- {row['项目']}"
        if pd.notna(row['时段']):
            result += f", 时段:{row['时段']}"
        if pd.notna(row['时间段']):
            result += f", 时间:{row['时间段']}"
        if pd.notna(row['备注']):
            result += f", 备注:{row['备注']}"
        result += "\n"
    
    return result

def get_daily_summary(date_str=None):
    if date_str is None:
        date_str = datetime.now().strftime('%Y-%m-%d')
    
    df = load_records()
    if df.empty:
        feeding_summary = "暂无喂养记录"
    else:
        target_date = pd.to_datetime(date_str).date()
        df['日期'] = df['时间戳'].dt.date
        filtered = df[df['日期'] == target_date]
        
        if filtered.empty:
            feeding_summary = f"{date_str} 暂无喂养记录"
        else:
            summary = {
                '总喂养次数': len(filtered),
                '总母乳量': int(filtered['母乳（ml）'].sum()),
                '总配方奶量': int(filtered['配方奶（ml）'].sum()),
                '总米粉量': round(filtered['米粉（g）'].sum(), 1),
                '总奶量': int(filtered['总奶量'].sum()),
                '补剂记录': filtered['补剂'].dropna().unique().tolist()
            }
            feeding_summary = f"{date_str} 喂养总结：\n"
            feeding_summary += f"喂养次数：{summary['总喂养次数']}次\n"
            feeding_summary += f"母乳总量：{summary['总母乳量']}ml\n"
            feeding_summary += f"配方奶总量：{summary['总配方奶量']}ml\n"
            feeding_summary += f"米粉总量：{summary['总米粉量']}g\n"
            feeding_summary += f"总奶量：{summary['总奶量']}ml\n"
            if summary['补剂记录']:
                feeding_summary += f"补剂：{', '.join(summary['补剂记录'])}\n"
    
    poop_summary = get_poop_records_by_date(date_str)
    care_summary = get_care_records_by_date(date_str)
    
    return f"{feeding_summary}\n{poop_summary}\n{care_summary}"

def get_weekly_summary(start_date=None, end_date=None):
    df = load_records()
    if df.empty:
        return "暂无喂养记录"
    
    if start_date is None:
        end_date = datetime.now()
        start_date = end_date - pd.Timedelta(days=7)
    else:
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date) if end_date else start_date + pd.Timedelta(days=7)
    
    mask = (df['时间戳'] >= start_date) & (df['时间戳'] <= end_date)
    filtered = df[mask]
    
    if filtered.empty:
        return f"{start_date.strftime('%Y-%m-%d')} 至 {end_date.strftime('%Y-%m-%d')} 暂无喂养记录"
    
    daily_stats = filtered.groupby(filtered['时间戳'].dt.date).agg({
        '母乳（ml）': 'sum',
        '配方奶（ml）': 'sum',
        '米粉（g）': 'sum',
        '总奶量': 'sum'
    }).reset_index()
    
    result = f"{start_date.strftime('%Y-%m-%d')} 至 {end_date.strftime('%Y-%m-%d')} 周总结：\n"
    for _, row in daily_stats.iterrows():
        date = row['时间戳'].strftime('%m-%d')
        result += f"{date}: 母乳{int(row['母乳（ml）'])}ml, 配方奶{int(row['配方奶（ml）'])}ml, 米粉{round(row['米粉（g）'], 1)}g, 总奶量{int(row['总奶量'])}ml\n"
    
    total_breast = int(daily_stats['母乳（ml）'].sum())
    total_formula = int(daily_stats['配方奶（ml）'].sum())
    total_rice = round(daily_stats['米粉（g）'].sum(), 1)
    total_milk = int(daily_stats['总奶量'].sum())
    
    result += f"\n总计：\n"
    result += f"母乳总量：{total_breast}ml\n"
    result += f"配方奶总量：{total_formula}ml\n"
    result += f"米粉总量：{total_rice}g\n"
    result += f"总奶量：{total_milk}ml\n"
    
    return result

def get_recent_records(count=5):
    df = load_records()
    if df.empty:
        feeding_result = "暂无喂养记录"
    else:
        recent = df.sort_values('时间戳', ascending=False).head(count)
        feeding_result = f"最近{len(recent)}条喂养记录：\n"
        for _, row in recent.iterrows():
            time_str = row['时间戳'].strftime('%Y-%m-%d %H:%M')
            feeding_result += f"- {time_str}: 母乳{row['母乳（ml）']}ml, 配方奶{row['配方奶（ml）']}ml, 米粉{row['米粉（g）']}g"
            if pd.notna(row['补剂']):
                feeding_result += f", 补剂:{row['补剂']}"
            if pd.notna(row['今日体温']):
                feeding_result += f", 体温:{row['今日体温']}℃"
            feeding_result += "\n"
    
    df_poop = load_poop_records()
    if df_poop.empty:
        poop_result = "暂无便便记录"
    else:
        recent_poop = df_poop.sort_values('时间戳', ascending=False).head(count)
        poop_result = f"\n最近{len(recent_poop)}条便便记录：\n"
        for _, row in recent_poop.iterrows():
            time_str = row['时间戳'].strftime('%Y-%m-%d %H:%M')
            poop_result += f"- {time_str}: "
            if pd.notna(row['量（多/中/少）']):
                poop_result += f"量:{row['量（多/中/少）']}"
            if pd.notna(row['颜色']):
                poop_result += f", 颜色:{row['颜色']}"
            if pd.notna(row['形状（干/稀）']):
                poop_result += f", 形状:{row['形状（干/稀）']}"
            poop_result += "\n"
    
    df_care = load_care_records()
    if df_care.empty:
        care_result = "暂无护理记录"
    else:
        recent_care = df_care.sort_values('日期', ascending=False).head(count)
        care_result = f"\n最近{len(recent_care)}条护理记录：\n"
        for _, row in recent_care.iterrows():
            date_str = row['日期'].strftime('%Y-%m-%d')
            care_result += f"- {date_str}: {row['项目']}"
            if pd.notna(row['时段']):
                care_result += f", 时段:{row['时段']}"
            care_result += "\n"
    
    return f"{feeding_result}{poop_result}{care_result}"

def search_records(keyword):
    df = load_records()
    if df.empty:
        feeding_result = "暂无喂养记录"
    else:
        filtered = df[df['备注'].astype(str).str.contains(keyword, na=False) | 
                      df['补剂'].astype(str).str.contains(keyword, na=False)]
        if filtered.empty:
            feeding_result = f"未找到包含'{keyword}'的喂养记录"
        else:
            feeding_result = f"找到{len(filtered)}条匹配的喂养记录：\n"
            for _, row in filtered.iterrows():
                time_str = row['时间戳'].strftime('%Y-%m-%d %H:%M')
                feeding_result += f"- {time_str}: 母乳{row['母乳（ml）']}ml, 配方奶{row['配方奶（ml）']}ml"
                if pd.notna(row['补剂']):
                    feeding_result += f", 补剂:{row['补剂']}"
                if pd.notna(row['备注']):
                    feeding_result += f", 备注:{row['备注']}"
                feeding_result += "\n"
    
    df_poop = load_poop_records()
    if df_poop.empty:
        poop_result = "暂无便便记录"
    else:
        filtered = df_poop[df_poop['其他'].astype(str).str.contains(keyword, na=False) |
                          df_poop['颜色'].astype(str).str.contains(keyword, na=False)]
        if filtered.empty:
            poop_result = f"未找到包含'{keyword}'的便便记录"
        else:
            poop_result = f"\n找到{len(filtered)}条匹配的便便记录：\n"
            for _, row in filtered.iterrows():
                time_str = row['时间戳'].strftime('%Y-%m-%d %H:%M')
                poop_result += f"- {time_str}: "
                if pd.notna(row['量（多/中/少）']):
                    poop_result += f"量:{row['量（多/中/少）']}"
                if pd.notna(row['颜色']):
                    poop_result += f", 颜色:{row['颜色']}"
                if pd.notna(row['其他']):
                    poop_result += f", 其他:{row['其他']}"
                poop_result += "\n"
    
    df_care = load_care_records()
    if df_care.empty:
        care_result = "暂无护理记录"
    else:
        filtered = df_care[df_care['项目'].astype(str).str.contains(keyword, na=False)]
        if filtered.empty:
            care_result = f"未找到包含'{keyword}'的护理记录"
        else:
            care_result = f"\n找到{len(filtered)}条匹配的护理记录：\n"
            for _, row in filtered.iterrows():
                date_str = row['日期'].strftime('%Y-%m-%d')
                care_result += f"- {date_str}: {row['项目']}"
                if pd.notna(row['备注']):
                    care_result += f", 备注:{row['备注']}"
                care_result += "\n"
    
    return f"{feeding_result}{poop_result}{care_result}"
