from file_define import *
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import *

jsonreader = JsonReader("D:\\python\\2011年2月销售数据JSON.txt")
textreader = TextReader("D:\\python\\2011年1月销售数据.txt")

jan_data: list[Record] = textreader.read_data()
feb_data: list[Record] = jsonreader.read_data()
all_data: list[Record] = jan_data + feb_data

data_dict = {}
for d in all_data:
    if d.date in data_dict.keys():
        data_dict[d.date] += d.money
    else:
        data_dict[d.date] = d.money

# print(data_dict)

bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)
bar.render("每日销售额.html")

