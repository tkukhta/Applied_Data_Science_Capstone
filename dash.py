dcc.Dropdown(id='site-dropdown',
			  options=[
                  {'label': 'All Sites', 'value': 'ALL'},
                  {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                  {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                  {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                  {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
              ],
              value='ALL',
              placeholder="Select a Launch Site Here",
              searchable=True
              ),


# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.pie(spacex_df, values='class', 
        names='pie chart names', 
        title='title')
        return fig
    else:
        fig = px.pie(spacex_df, values='class', 
        names='pie chart names', 
        title='title')
        return fig