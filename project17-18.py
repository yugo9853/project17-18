import pandas as pd
import matplotlib.pyplot as plt

# 1. 從外部檔案讀取數據（讀取名為 'MAC DATA' 的檔案）
# 注意: もしこれでも「FileNotFoundError」が出る場合は、実際のファイル名が「MAC DATA.csv」になっている可能性があります。
# その場合はここの括弧内を 'MAC DATA.csv' に書き換えてください。
df = pd.read_csv('MAC DATA')

# 2. 計算 CP 值（每 1 塊錢可以買到的熱量）
df['CP_Value'] = df['Calories'] / df['Price_TWD']

# 3. 依照 CP 值由低到高進行排序（為了讓長條圖的顯示順序正確）
df_sorted = df.sort_values(by='CP_Value', ascending=True)

# 4. 建立圖表（儀表板視覺化）
plt.figure(figsize=(10, 6))
plt.barh(df_sorted['Item'], df_sorted['CP_Value'], color='#FFC72C', edgecolor='#DA291C', height=0.6)

# 圖表美化與標籤設定 (避免 Mac 字體錯誤，維持英文標示)
plt.xlabel('CP Value (Calories / TWD)', fontsize=12)
plt.ylabel('Menu Items', fontsize=12)
plt.title('McDonalds: CP Value Ranking (Calories per 1 TWD)', fontsize=16, fontweight='bold')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()

# 5. 儲存與顯示圖表
plt.savefig('mcdonalds_cp_dashboard.png')
plt.show()

# 6. 終端機輸出計算結果
print("【分析完成】CP值第一名（性價比霸主）的計算結果:\n")
print(df_sorted[['Item', 'Calories', 'Price_TWD', 'CP_Value']].sort_values(by='CP_Value', ascending=False))