import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px

image_trace = go.layout.Image(
            name="Logo",
            source="Logo Blue BagliniFInance.png",
            xref="paper",
            yref="paper",
            x=1.05,
            y=-0.314,
            sizex=0.13,
            sizey=0.2,
            sizing="stretch",
            opacity=1,
            layer="above",
            xanchor="right",
            yanchor="bottom",
            visible=True
)

# Create layout template
blog_template_logo = dict(

    layout_colorway=px.colors.qualitative.T10,
    layout=go.Layout(
        title_font=dict(family="merriserif", size=24),
        title=dict(x=0.5, xanchor="center", text=None),
        font=dict(family="merriserif", size=12),
        legend=dict(
            x=0.5,
            xanchor="center",
            y=-0.20,
            traceorder="reversed",
            bgcolor="white",
            bordercolor="Black",
            borderwidth=1,
            orientation='h'
        ),
        images= [image_trace]  # Add the image trace to the layout template
    )
)
#pio.templates["blog_mra"] = blog_template
pio.templates["blog_mra"] = blog_template_logo

def to_jupyter_latex(df, digits=2):
    print(df.head().to_latex(index=True, float_format="{:.2f}".format,).replace('\\toprule', '\\hline').replace('\\midrule', '\\hline').replace('\\bottomrule','\\hline').replace('tabular', 'array'))
