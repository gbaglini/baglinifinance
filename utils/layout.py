import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px

blog_template = dict(
    layout_colorway=px.colors.qualitative.T10,

    layout=go.Layout(

        title_font=dict(family="merriserif", size=24),
        title=dict(x=0.5, xanchor="center", text=None),
        font=dict(family="merriserif", size=12),
        legend=dict(x=0.5,
                    xanchor="center",
                    y=-0.20,
                    traceorder="reversed",
                    bgcolor="white",
                    bordercolor="Black",
                    borderwidth=1,
                    orientation='h'),
    )
)

pio.templates["blog_mra"] = blog_template

def to_jupyter_latex(df, digits=2):
    print(df.head().to_latex(index=True, float_format="{:.2f}".format,).replace('\\toprule', '\\hline').replace('\\midrule', '\\hline').replace('\\bottomrule','\\hline').replace('tabular', 'array'))
