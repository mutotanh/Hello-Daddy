# coding=gbk
# ������:SyntaxError: Non-UTF-8 code starting with '\xd0' in file���������������
#���ݴ������õĿ�
#��ͼ
import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts

# #��ȡ���ݣ���������ͷ��,�����д���
df = pd.read_excel('���A��2023-03-20 11-19-59.xlsx')
df = pd.DataFrame(df)
print(type(df))
# ɾ��ֵȫ��Ϊ�յ�ÿһ��
df.dropna(axis=0,how='all')
# # ɾ�������κκ��п�ֵ����
df.dropna(axis=0,how='any')
# ɾ������ȫ��ΪNaN����
df.dropna(axis=1, how='all')
# ɾ�������κκ��п�ֵ����
df.dropna(axis=1, how='any')
# # ---ɾ�������ظ���---
df.drop_duplicates()
print(df)
#
#
#
#
# df1=df['��Ʊ����'].iloc[:20]
# df2=df['�ɽ���'].iloc[:20]
# df3=df['�ɽ���'].iloc[:20]
#
#
# c=(
#     Bar()
#     .add_xaxis(list(df1))#��x��
#     .add_yaxis('��Ʊ�ɽ������',list(df2))#�趨y��ͼ�������y�����ݣ�����list�б����͵�����
#     .add_yaxis('��Ʊ�ɽ������', list(df3))  # �趨y��ͼ�������y�����ݣ�����list�б����͵�����
#     .set_global_opts(
#         xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)),#��б
#         title_opts=opts.TitleOpts(title="�ɽ���ͼ��",subtitle='2022-11-27 16-46-59'),#����
#         toolbox_opts=opts.ToolboxOpts(),
#         datazoom_opts=opts.DataZoomOpts()#���������
#
#     )
# )
# c.render("./app/templates/bar.html")
# print(type(c))
#
# # #���ȣ����ɱ�ͼ
# # import pandas as pd
# # from pyecharts.charts import Bar,Pie
# # from pyecharts import options as opts
# #
# # # # #��ȡ���ݣ���������ͷ��
# # df = pd.read_excel('���A��2022-11-27 16-46-59.xlsx')
# # df = pd.DataFrame(df)
# #
# #
# # df2=df['����']
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
# # data_pair_temp = [list(data) for data in zip(p, q)]  # month �൱���Ա���, temp �൱�������
# #
# # p = (
# #         Pie()  # ʵ����
# #         .add(
# #             series_name="����",  # ϵ������
# #             data_pair=data_pair_temp,# ��������
# #             radius="35%",            # ��ͼ�뾶����
# #             center=["50%", "50%"],   # ��ͼ��������
# #             label_opts=opts.LabelOpts(is_show=False, position="center"),  # ��ǩλ��
# #         )
# #         .set_global_opts(legend_opts=opts.LegendOpts(is_show=False))      # ����ʾͼʾ
# #         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))  # ��ǩ��ɫ
# #     .render("./app/templates/Pie.html")  # ��Ⱦ�ļ���������
# #     #.render_notebook()
# #
# # )
# #
# #
# #�״�ͼ
# import pyecharts.options as op
# from pyecharts.charts import Radar
#
# import pandas as pd
# from pyecharts.charts import Bar
# from pyecharts import options as opts
# # #��ȡ���ݣ���������ͷ��
# df = pd.read_excel('���A��2023-04-01 14-14-22.xlsx')
# df = pd.DataFrame(df)
# print(type(df))
#
#
#
# df1=df['��Ʊ����']
# df2=df['���'].iloc[:5]
# df3=df['���'].iloc[:5]
# df4=df['��'].iloc[:5]
# df5=df['����'].iloc[:5]
# df6=df['���¼�'].iloc[:5]
# # �����ά����,���ݵ����6��
# v0= list(df1)
# v1 = [list(df2)]
# v2 = [list(df3)]
# v3 = [list(df4)]
# v4 = [list(df5)]
# v5 = [list(df6)]
#
# # �����״��ά�ȵķ�Χ��С,ά��Ҫ����ά����
# x_schema = [
#         {"name": v0[0], "max": 200, "min": 0, "color": 'black', "font_size": 18},
#         {"name": v0[1], "max": 200, "min": 0, "color": 'black', "font_size": 18},
#         {"name": v0[2], "max": 200, "min": 0, "color": 'black', "font_size": 18},
#         {"name": v0[3], "max": 200, "min": 0, "color": 'black', "font_size": 18},
#         {"name": v0[4], "max": 200, "min":0, "color": 'black', "font_size": 18}
#     ]
#
# # ��ͼ
# radar_x = Radar()
# radar_x.add_schema(x_schema)
# radar_x.add('���', v1, color='red').set_colors(['red'])
# radar_x.add('���', v2, color='green').set_colors(['green'])
# radar_x.add('��', v3, color='orange').set_colors(['orange'])
# radar_x.add('����', v4, color='blue').set_colors(['blue'])
# radar_x.add('��߼�',v5,color='purple').set_colors(['purple'])
#
# radar_x.set_global_opts(
#         title_opts=op.TitleOpts(title="Miami Heat Starting Lineup", pos_right="center"),
#         legend_opts=op.LegendOpts(legend_icon="roundRect", align="left", pos_left='7%',
#                                   pos_bottom='14%', orient='vertical')
#     )
# #
# radar_x.render("./app/templates/Radar.html")
# #
# # #ɢ��ͼ��
# # import pyecharts.options as op
# # from pyecharts.charts import Radar
# #
# # import pandas as pd
# # from pyecharts.charts import Scatter
# # from pyecharts import options as opts
# # from pyecharts import options as opts
# # from pyecharts.charts import Scatter
# # # #��ȡ���ݣ���������ͷ��
# # df = pd.read_excel('���A��2022-11-27 16-46-59.xlsx')
# # df = pd.DataFrame(df)
# # print(type(df))
# #
# # df1=df['��Ʊ����'].iloc[:40]
# # df2=df['���¼�'].iloc[:40]
# # df3=df['����'].iloc[:40]
# # df1= list(df1)
# # df2 = list(df2)
# # df3=list(df3)
# #
# # scatter = Scatter()
# # scatter.add_xaxis(df1)
# # scatter.add_yaxis("���¼�",df2,symbol_size=20)# ɢ���С
# # scatter.add_yaxis("����",df3,symbol_size=20)# ɢ���С
# # scatter.set_global_opts(title_opts=opts.TitleOpts(title="��Ʊ���¼�ɢ��ͼ"),
# #
# #                         visualmap_opts=opts.VisualMapOpts(type_="size", max_=240, min_=2),
# #                         xaxis_opts=opts.AxisOpts(
# #                             # type_="value",    # ����X��Ϊ��ֵ��
# #                             splitline_opts=opts.SplitLineOpts(is_show=True)),# X��ָ���
# #                         yaxis_opts=opts.AxisOpts(
# #                             splitline_opts=opts.SplitLineOpts(is_show=True)),# Y��ָ���
# #                         )
# # scatter.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
# # scatter.render("./app/templates/scatter.html")
#
