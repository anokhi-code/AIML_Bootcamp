import pandas as pd
import numpy as np
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, Select
from bokeh.layouts import row, column
from bokeh.plotting import figure

# Dummy sales data
np.random.seed(42)
dates = pd.date_range("2025-01-01", periods=12, freq="ME")

regions = ["North", "South", "East", "West"]
categories = ["Electronics", "Clothing", "Furniture"]

data = []
for region in regions:
    for cat in categories:
        sales = np.random.randint(50, 200, size=len(dates))
        for d, s in zip(dates, sales):
            data.append([d, region, cat, s])

df = pd.DataFrame(data, columns=["Date", "Region", "Category", "Sales"])

def get_dataset(region):
    df_region = df[df["Region"] == region]
    monthly_sales = df_region.groupby("Date")['Sales'].sum().reset_index()
    category_sales = df_region.groupby("Category")['Sales'].sum().reset_index()
    return ColumnDataSource(monthly_sales), ColumnDataSource(category_sales)

# Initialize with default region
region_default = "North"
source_line, source_bar = get_dataset(region_default)

# Line chart
p1 = figure(
    title=f"Monthly Sales - {region_default} Region",
    x_axis_type="datetime",
    height=300, width=500,
    toolbar_location="right"
)
p1.line("Date", "Sales", source=source_line, line_width=3, color="blue")
p1.circle("Date", "Sales", source=source_line, size=8, color="red")

p1.xaxis.axis_label = "Date"
p1.yaxis.axis_label = "Sales"

# Bar chart
p2 = figure(
    title=f"Total Sales by Category - {region_default} Region",
    x_range=categories,
    height=300, width=400,
    toolbar_location="right"
)
p2.vbar(x="Category", top="Sales", width=0.5, source=source_bar, color="green")

p2.xaxis.axis_label = "Category"
p2.yaxis.axis_label = "Sales"

# Dropdown
region_select = Select(title="Select Region:", value=region_default, options=regions)

def update(attr, old, new):
   region = region_select.value
   new_source_line, new_source_bar = get_dataset(region)

    source_line.data = new_source_line.data
    source_bar.data = new_source_bar.data

    # Update titles dynamically
    p1.title.text = f"Monthly Sales - {region} Region"
    p2.title.text = f"Total Sales by Category - {region} Region"


region_select.on_change("value", update)

layout = column(region_select, row(p1, p2))

curdoc().add_root(layout)
curdoc().title = "Sales Dashboard"
