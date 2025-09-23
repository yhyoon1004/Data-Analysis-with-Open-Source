from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.io import output_notebook
import pandas as pd

# plt.rc('font', family='AppleGothic')
# plt.rcParams['axes.unicode_minus'] = False

# output_notebook( )

## 데이터프레임 생성
df = pd.DataFrame({
    '날짜': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    '매출': [200, 300, 250, 400, 500, 450, 600, 700, 650, 800],
    '지점': ['A'] * 10 })
df['날짜'] = pd.to_datetime(df['날짜'])
source = ColumnDataSource(df)

## 그래프 객체 생성
p = figure( x_axis_type='datetime', title='Bokeh 고급 인터랙티브 선 그래프',
           width=700, height=400, tools="pan,wheel_zoom,box_zoom,reset,save" )

## 선 그래프 추가
p.line( '날짜', '매출', source=source, line_width=3, color='navy',
       legend_label='A 지점 매출' )

## HoverTool 추가
hover = HoverTool( tooltips=[ ("지점", "@지점"),
        ("날짜", "@날짜{%F}"),
        ("매출", "@매출{0,0}원")],
    formatters={ '@날짜': 'datetime' },
    mode='mouse')

p.add_tools(hover)
p.legend.title = '지점 정보'
p.legend.label_text_font_size = '12pt'
show(p)