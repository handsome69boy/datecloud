# import pandas as pd
# path=r"./日期與時間統整.xlsx"
# # 在.py檔路徑前面要變成/mnt/c才能讀取
# df= pd.read_excel(path,usecols=[2])

# print(df)

import pandas as pd

def parse_date_with_nan(df, column_name):
    # 自定義日期時間格式列表，根據您的需求添加更多的格式
    date_formats = ["%Y-%m-%d %H:%M:%S", "%m/%d/%Y","%Y/%m/%d","%Y-%m-%d" ,"%d-%m-%Y", "%Y-%m-%d %H:%M:%S",
                    "%Y-%m-%d %H:%M:%S.%f", "%Y/%m/%d 下午%H:%M:%S", "%Y/%m/%d 上午%H:%M:%S","%Y/%m/%d %H:%M:%S","%Y-%m-%dT%H:%M:%S",
                    "%H:%M:%S", "%I:%M:%S %p", "%H:%M", "%Y年%m月%d日", "%d %b %Y",
                    "%d %b %Y %H:%M:%S", "%d/%m/%Y %H:%M:%S", "%m/%d/%y", "%Y%m%d","%Y.%m.%d","%Y.%m.%d %H:%M:%S",]
    df.insert(df.columns.get_loc(column_name) + 1,f"{column_name}_time", "")
    for idx, value in enumerate(df[column_name]):
        if pd.isna(value):
            continue  # 如果該值為 NaN，則跳過

        for date_format in date_formats:
            try:
                # 嘗試使用不同的日期時間格式進行解析
                datetime_obj = pd.to_datetime(value, format=date_format)
                datepart = datetime_obj.date()
                timepart = datetime_obj.time()
                df.at[idx, column_name] = datepart.strftime("%Y-%m-%d")
                if datepart == pd.to_datetime("1900-01-01").date():
                    df.at[idx,column_name] = "no data"
                else:
                    df.at[idx,column_name] = datepart.strftime("%Y-%m-%d")
                if timepart == pd.to_datetime("00:00:00").time():
                    df.at[idx, f"{column_name}_time"] = "no data"
                else:
                    df.at[idx, f"{column_name}_time"] = timepart.strftime("%H:%M:%S")
                break  # 成功解析後跳出內層迴圈
            except ValueError:
                pass  # 格式不匹配，繼續嘗試下一個日期格式

    return df

# df = parse_date_with_nan(df, "date")

# print(df)
