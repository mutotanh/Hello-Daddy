# coding=gbk
# 若报错:SyntaxError: Non-UTF-8 code starting with '\xd0' in file，则把上面这句加上
#数据处理所用的库
#饼图
import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts

# #读取数据（不包含表头）,并进行处理
df = pd.read_excel('沪深京A股2023-03-20 11-19-59.xlsx')
df = pd.DataFrame(df)
print(type(df))
# 删除值全部为空的每一行
df.dropna(axis=0,how='all')
# # 删除表中任何含有空值的行
df.dropna(axis=0,how='any')
# 删除表中全部为NaN的列
df.dropna(axis=1, how='all')
# 删除表中任何含有空值的列
df.dropna(axis=1, how='any')
# # ---删除所有重复行---
df.drop_duplicates()
print(df)
#
#
#
#
# df1=df['股票名称'].iloc[:20]
# df2=df['成交量'].iloc[:20]
# df3=df['成交额'].iloc[:20]
#
#
# c=(
#     Bar()
#     .add_xaxis(list(df1))#做x轴
#     .add_yaxis('股票成交量情况',list(df2))#设定y轴图例，添加y轴数据，接收list列表类型的数据
#     .add_yaxis('股票成交额情况', list(df3))  # 设定y轴图例，添加y轴数据，接收list列表类型的数据
#     .set_global_opts(
#         xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)),#倾斜
#         title_opts=opts.TitleOpts(title="成交量图表",subtitle='2022-11-27 16-46-59'),#表名
#         toolbox_opts=opts.ToolboxOpts(),
#         datazoom_opts=opts.DataZoomOpts()#添加缩放条
#
#     )
# )
# c.render("./app/templates/bar.html")
# print(type(c))
#
# # #量比：生成饼图
# # import pandas as pd
# # from pyecharts.charts import Bar,Pie
# # from pyecharts import options as opts
# #
# # # # #读取数据（不包含表头）
# # df = pd.read_excel('沪深京A股2022-11-27 16-46-59.xlsx')
# # df = pd.DataFrame(df)
# #
# #
# # df2=df['量比']
# # df2=list(df2)
# # m=0
# # n=0
# # t=1
# # h=0
# # g=0
# # k=0
# # q=[]
# # for i in range(len(df2)):
# #     if 0.00<df2[i]<0.50:
# #         m+=1
# #     if 0.50<df2[i] < 1.00:
# #         n += 1
# #     if  1.00<df2[i] < 2.00:
# #         t += 1
# #     if 2.00<df2[i] < 3.00:
# #         h += 1
# #     if 3.00<df2[i] < 4.00:
# #         g += 1
# #     if df2[i] > 4.00:
# #         k += 1
# # q.append(m)
# # q.append(n)
# # q.append(t)
# # q.append(h)
# # q.append(g)
# # q.append(k)
# # print(q)
# # p=["0.00-0.50","0.50-1.00","1.00-2.00","2.00-3.00","3.00-4.00"]
# # data_pair_temp = [list(data) for data in zip(p, q)]  # month 相当于自变量, temp 相当于因变量
# #
# # p = (
# #         Pie()  # 实例化
# #         .add(
# #             series_name="量比",  # 系列名称
# #             data_pair=data_pair_temp,# 馈入数据
# #             radius="35%",            # 饼图半径比例
# #             center=["50%", "50%"],   # 饼图中心坐标
# #             label_opts=opts.LabelOpts(is_show=False, position="center"),  # 标签位置
# #         )
# #         .set_global_opts(legend_opts=opts.LegendOpts(is_show=False))      # 不显示图示
# #         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))  # 标签颜色
# #     .render("./app/templates/Pie.html")  # 渲染文件及其名称
# #     #.render_notebook()
# #
# # )
# #
# #
# #雷达图
# import pyecharts.options as op
# from pyecharts.charts import Radar
#
# import pandas as pd
# from pyecharts.charts import Bar
# from pyecharts import options as opts
# # #读取数据（不包含表头）
# df = pd.read_excel('沪深京A股2023-04-01 14-14-22.xlsx')
# df = pd.DataFrame(df)
# print(type(df))
#
#
#
# df1=df['股票名称']
# df2=df['最高'].iloc[:5]
# df3=df['最低'].iloc[:5]
# df4=df['今开'].iloc[:5]
# df5=df['昨收'].iloc[:5]
# df6=df['最新价'].iloc[:5]
# # 传入多维数据,数据点最多6个
# v0= list(df1)
# v1 = [list(df2)]
# v2 = [list(df3)]
# v3 = [list(df4)]
# v4 = [list(df5)]
# v5 = [list(df6)]
#
# # 调整雷达各维度的范围大小,维度要求四维以上
# x_schema = [
#         {"name": v0[0], "max": 200, "min": 0, "color": 'black', "font_size": 18},
#         {"name": v0[1], "max": 200, "min": 0, "color": 'black', "font_size": 18},
#         {"name": v0[2], "max": 200, "min": 0, "color": 'black', "font_size": 18},
#         {"name": v0[3], "max": 200, "min": 0, "color": 'black', "font_size": 18},
#         {"name": v0[4], "max": 200, "min":0, "color": 'black', "font_size": 18}
#     ]
#
# # 画图
# radar_x = Radar()
# radar_x.add_schema(x_schema)
# radar_x.add('最高', v1, color='red').set_colors(['red'])
# radar_x.add('最低', v2, color='green').set_colors(['green'])
# radar_x.add('今开', v3, color='orange').set_colors(['orange'])
# radar_x.add('昨收', v4, color='blue').set_colors(['blue'])
# radar_x.add('最高价',v5,color='purple').set_colors(['purple'])
#
# radar_x.set_global_opts(
#         title_opts=op.TitleOpts(title="Miami Heat Starting Lineup", pos_right="center"),
#         legend_opts=op.LegendOpts(legend_icon="roundRect", align="left", pos_left='7%',
#                                   pos_bottom='14%', orient='vertical')
#     )
# #
# radar_x.render("./app/templates/Radar.html")
# #
# # #散点图：
# # import pyecharts.options as op
# # from pyecharts.charts import Radar
# #
# # import pandas as pd
# # from pyecharts.charts import Scatter
# # from pyecharts import options as opts
# # from pyecharts import options as opts
# # from pyecharts.charts import Scatter
# # # #读取数据（不包含表头）
# # df = pd.read_excel('沪深京A股2022-11-27 16-46-59.xlsx')
# # df = pd.DataFrame(df)
# # print(type(df))
# #
# # df1=df['股票名称'].iloc[:40]
# # df2=df['最新价'].iloc[:40]
# # df3=df['昨收'].iloc[:40]
# # df1= list(df1)
# # df2 = list(df2)
# # df3=list(df3)
# #
# # scatter = Scatter()
# # scatter.add_xaxis(df1)
# # scatter.add_yaxis("最新价",df2,symbol_size=20)# 散点大小
# # scatter.add_yaxis("昨收",df3,symbol_size=20)# 散点大小
# # scatter.set_global_opts(title_opts=opts.TitleOpts(title="股票最新价散点图"),
# #
# #                         visualmap_opts=opts.VisualMapOpts(type_="size", max_=240, min_=2),
# #                         xaxis_opts=opts.AxisOpts(
# #                             # type_="value",    # 设置X轴为数值轴
# #                             splitline_opts=opts.SplitLineOpts(is_show=True)),# X轴分割线
# #                         yaxis_opts=opts.AxisOpts(
# #                             splitline_opts=opts.SplitLineOpts(is_show=True)),# Y轴分割线
# #                         )
# # scatter.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
# # scatter.render("./app/templates/scatter.html")
#
