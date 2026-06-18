#!/usr/bin/env python3
"""
婴儿喂养记录管理系统 - 命令行界面
"""

from datetime import datetime
from .core import (
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

def main():
    print("=" * 40)
    print("    婴儿喂养记录管理系统")
    print("=" * 40)
    
    while True:
        print("\n【菜单】")
        print("=" * 30)
        print("【饮食记录】")
        print("1. 添加喂养记录")
        print("2. 查询当日喂养记录")
        print("3. 查询指定日期喂养记录")
        print("4. 每日喂养总结")
        print("5. 周喂养总结")
        print("-" * 30)
        print("【便便记录】")
        print("6. 添加便便记录")
        print("7. 查询当日便便记录")
        print("8. 查询指定日期便便记录")
        print("-" * 30)
        print("【护理记录】")
        print("9. 添加护理记录")
        print("10. 查询当日护理记录")
        print("11. 查询指定日期护理记录")
        print("-" * 30)
        print("【综合功能】")
        print("12. 最近记录")
        print("13. 搜索记录")
        print("0. 退出")
        
        try:
            choice = input("\n请输入选择：")
            
            if choice == '1':
                breast = int(input("母乳（ml）："))
                formula = int(input("配方奶（ml）："))
                rice = float(input("米粉（g）："))
                supplements = input("补剂（AD/D3/空）：") or None
                temp_input = input("是否记录体温？(y/n)：")
                temp = float(input("体温（℃）：")) if temp_input.lower() == 'y' else None
                notes = input("备注：") or None
                print(add_feeding_record(
                    breast_milk=breast, 
                    formula_milk=formula, 
                    rice_flour=rice, 
                    supplements=supplements, 
                    temperature=temp, 
                    notes=notes
                ))
            
            elif choice == '2':
                today = datetime.now().strftime('%Y-%m-%d')
                print(get_records_by_date(today))
            
            elif choice == '3':
                date = input("请输入日期（YYYY-MM-DD）：")
                print(get_records_by_date(date))
            
            elif choice == '4':
                date = input("请输入日期（YYYY-MM-DD，空则今日）：") or None
                print(get_daily_summary(date))
            
            elif choice == '5':
                start = input("请输入开始日期（YYYY-MM-DD）：")
                end = input("请输入结束日期（YYYY-MM-DD，空则默认一周）：") or None
                print(get_weekly_summary(start, end))
            
            elif choice == '6':
                amount = input("量（多/中/少）：") or None
                color = input("颜色：") or None
                consistency = input("形状（干/稀/正常）：") or None
                notes = input("其他备注：") or None
                print(add_poop_record(
                    amount=amount, 
                    color=color, 
                    consistency=consistency, 
                    notes=notes
                ))
            
            elif choice == '7':
                today = datetime.now().strftime('%Y-%m-%d')
                print(get_poop_records_by_date(today))
            
            elif choice == '8':
                date = input("请输入日期（YYYY-MM-DD）：")
                print(get_poop_records_by_date(date))
            
            elif choice == '9':
                period = input("时段（上午/下午/晚上）：") or None
                item = input("项目（洗澡/排气操/被动操等）：")
                time_range = input("时间段（如：10:00-11:00）：") or None
                notes = input("备注：") or None
                print(add_care_record(
                    period=period, 
                    item=item, 
                    time_range=time_range, 
                    notes=notes
                ))
            
            elif choice == '10':
                today = datetime.now().strftime('%Y-%m-%d')
                print(get_care_records_by_date(today))
            
            elif choice == '11':
                date = input("请输入日期（YYYY-MM-DD）：")
                print(get_care_records_by_date(date))
            
            elif choice == '12':
                count = int(input("显示最近几条记录（默认5）：") or 5)
                print(get_recent_records(count))
            
            elif choice == '13':
                keyword = input("请输入搜索关键词：")
                print(search_records(keyword))
            
            elif choice == '0':
                print("感谢使用婴儿喂养记录管理系统！")
                break
            
            else:
                print("无效选择，请重新输入")
        
        except ValueError as e:
            print(f"输入错误：{e}")
        except Exception as e:
            print(f"发生错误：{e}")

if __name__ == "__main__":
    main()
