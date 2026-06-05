def calculate_payout():
    # --- 請在此處填入數據 ---
    total_income = 0          # 總收入
    
    jiahao_days = 0           # 家豪 工作天數
    jiahao_wage = 0           # 家豪 工資費用
    jiahao_material = 0       # 家豪 材料費用
    jiahao_lunch = 0          # 家豪 中餐費用
    
    dingyang_days = 0         # 定暘 工作天數
    dingyang_wage = 0         # 定暘 工資費用
    dingyang_material = 0     # 定暘 材料費用
    dingyang_lunch = 0        # 定暘 中餐費用
    # -----------------------

    # 計算每人應扣除的成本
    jiahao_cost = (jiahao_days * jiahao_wage) + jiahao_material + jiahao_lunch
    dingyang_cost = (dingyang_days * dingyang_wage) + dingyang_material + dingyang_lunch
    
    # 總淨利
    net_profit = total_income - jiahao_cost - dingyang_cost
    
    # 每人分紅 (總淨利除以 2)
    per_person_payout = net_profit / 2
    
    print(f"--- 計算結果 ---")
    print(f"總收入: {total_income}")
    print(f"家豪總成本: {jiahao_cost}")
    print(f"定暘總成本: {dingyang_cost}")
    print(f"總淨利: {net_profit}")
    print(f"每人可分: {per_person_payout}")

# 執行計算
calculate_payout()
