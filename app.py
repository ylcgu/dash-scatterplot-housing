import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables ######

myheading = "Baseball Stats from the 1950s"
mytitle = "Batting Averages for 3 Hall of Famers"
x_values = ['1954', '1955', '1956', '1957', '1958', '1959']
y1_values = [345, 356, 345, 388, 328, 254]
y2_values = [300, 306, 353, 365, 304, 285]
y3_values = [280, 314, 328, 322, 326, 355]
color1 = '#fc9403'
color2 = '#0307fc'
color3 = '#9003fc'
name1 = 'Ted Williams'
name2 = 'Mickey Mantle'
name3 = 'Hank Aaron'
tabtitle = 'baseball'
sourceurl = 'https://www.baseball-reference.com'
githublink = 'https://github.com/austinlasseter/dash-linechart-example'

########### Set up the chart

# create traces
trace0 = go.Scatter(
    x = x_values,
    y = y1_values,
    mode = 'lines',
    marker = {'color': color1},
    name = name1
)
trace1 = go.Scatter(
    x = x_values,
    y = y2_values,
    mode = 'lines',
    marker = {'color': color2},
    name = name2
)
trace2 = go.Scatter(
    x = x_values,
    y = y3_values,
    mode = 'lines',
    marker = {'color': color3},
    name = name3
)

# assign traces to data
data = [trace0, trace1, trace2]
layout = go.Layout(
    title = mytitle
)

# Generate the figure dictionary
fig = go.Figure(data=data,layout=layout)

########### Initiate the app
app = dash.Dash()
server = app.server
app.title=tabtitle
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
