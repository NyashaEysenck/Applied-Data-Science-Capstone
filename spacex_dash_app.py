# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

launch_sites = spacex_df['Launch Site'].unique()
dropdown_options = [{'label': 'All Sites', 'value': 'ALL'}] + [{'label': site, 'value': site} for site in launch_sites]

total_success_count = len(spacex_df[spacex_df['class'] == 1])

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown',
                                options=dropdown_options,
                                value='ALL',  # Default value
                                placeholder='Select a Launch Site here',
                                searchable=True  # Allows for keyword search
                                ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(
                                    id='payload-slider',
                                    min=0,
                                    max=10000,
                                    step=1000,
                                    value=[min_payload, max_payload],
                                    marks={
                                        0: '0',
                                        1000: '1000',
                                        2000: '2000',
                                        3000: '3000',
                                        4000: '4000',
                                        5000: '5000',
                                        6000: '6000',
                                        7000: '7000',
                                        8000: '8000',
                                        9000: '9000',
                                        10000: '10000'
                                    }
                                )
                                ,
                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
 # Function decorator to specify function input and output
# Function decorator to specify function input and output
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def update_pie_chart(selected_site):
    if selected_site == 'ALL':
        # Calculate total success counts for each launch site
        site_success_counts = []
        for site in spacex_df['Launch Site'].unique():
            site_df = spacex_df[spacex_df['Launch Site'] == site]
            success_count = len(site_df[site_df['class'] == 1])
            site_success_counts.append({'Launch Site': site, 'Success Count': success_count})
        
        # Create a dataframe for the pie chart
        site_success_counts_df = pd.DataFrame(site_success_counts)
        fig = px.pie(site_success_counts_df, values='Success Count', names='Launch Site', title='Total Successful Launches by Site')
    else:
        # Filter dataframe for selected launch site
        filtered_df = spacex_df[spacex_df['Launch Site'] == selected_site]
        success_count = len(filtered_df[filtered_df['class'] == 1])
        fail_count = len(filtered_df[filtered_df['class'] == 0])
        labels = ['Success', 'Failure']
        values = [success_count, fail_count]
        title = f'Success vs. Failure for {selected_site}'
        
        # Create pie chart figure using Plotly Express
        fig = px.pie(names=labels, values=values, title=title)
    
    return fig

    
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'), 
     Input(component_id='payload-slider', component_property='value')]
)
def update_scatter_chart(selected_site, payload_range):
    min_payload, max_payload = payload_range
    if selected_site == 'ALL':
        filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= min_payload) & 
                                (spacex_df['Payload Mass (kg)'] <= max_payload)]
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version Category',
                         title='Payload vs. Outcome for All Sites',
                         labels={'class': 'Outcome'})
    else:
        filtered_df = spacex_df[(spacex_df['Launch Site'] == selected_site) &
                                (spacex_df['Payload Mass (kg)'] >= min_payload) & 
                                (spacex_df['Payload Mass (kg)'] <= max_payload)]
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version Category',
                         title=f'Payload vs. Outcome for {selected_site}',
                         labels={'class': 'Outcome'})
    
    fig.update_layout(xaxis_title='Payload Mass (kg)', yaxis_title='Outcome')
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server()
