from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

f = open("D:\\python\\1960-2019全球GDP数据.csv","r",encoding="GB2312")
data_lines = f.readlines()
f.close()
data_lines.pop(0)
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])
    contry = line.split(",")[1]
    gdp = float(line.split(",")[2])
    try:
        data_dict[year].append([contry,gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([contry, gdp])


timeline = Timeline({"theme": ThemeType.LIGHT})
sorted_year = sorted(data_dict.keys())
for year in sorted_year:
    data_dict[year].sort(key=lambda x:x[1],reverse=True)
    year_data = data_dict[year][0:8:1]
    x_data = []
    y_data = []
    for data in year_data:
        x_data.append(data[0])
        y_data.append(data[1]/100000000)
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP（亿）",y_data,label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    bar.set_global_opts(title_opts= TitleOpts(title = f"{year}年GDP"))
    timeline.add(bar,str(year))

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)
print(timeline.render())
