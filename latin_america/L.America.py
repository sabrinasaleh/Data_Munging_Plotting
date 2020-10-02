#this code was made to continue or go along with the code  in main.ipynb 

latin_df = clean_data[clean_data.region == "Latin America"]

# Creating bar plot for "FDI in US (Yr 2018) for Latin America"
fig_la_bar = px.bar(
    latin_df,
    x="country_name",
    y="fdi_USA_2018 (million)",
    title="FDI in US (Yr 2018) for Latin America",
)

fig_la_bar.write_image("L.America FDI bar chart.png")
fig_la_bar.show()

scatter_la_tech = px.scatter(
    latin_df,
    y="fdi_USA_2018 (million)",
    x="tech_export_2018 (million)",
    color="country_name",
    title="FDI in USA vs Innovation-Technology by Countries (yr 2018)",
)
scatter_la_tech.write_image("L.America FDI vs Tech scatter plot.png")
scatter_la_tech.show()

scatter_la_db = px.scatter(
    latin_df,
    y="fdi_USA_2018 (million)",
    x="doing_business_2018",
    color="country_name",
    title="FDI in USA vs Ease Doing Business by Countries in Latin America (yr 2018)",
)
scatter_la_db.write_image("L.America Ease of Doing Business Rating scatter plot.png")
scatter_la_db.show()


scatter_la_gdp = px.scatter(
    latin_df,
    y="fdi_USA_2018 (million)",
    x="GDP_2018 (million)",
    color="country_name",
    title="FDI in USA vs GDP by Countries in Latin America (yr 2018)",
)
scatter_la_tech.write_image("L.America GDP scatter plot.png")
scatter_la_tech.show()

from config import mapbox_token

px.set_mapbox_access_token(mapbox_token)

la_scattermap = px.scatter_mapbox(
    latin_df,
    lat="lat",
    lon="lng",
    color="fdi_USA_2018 (million)",
    hover_data=["country_name"],
    zoom=1,
)
la_scattermap.write_image("Latin America FDI scatter map.png")
la_scattermap



#top 10 FDI within Latin America plots

dropna_latin_df = latin_df.dropna()

latin_sorted = dropna_latin_df.sort_values(
    ["fdi_USA_2018 (million)", "country_name"], ascending=False
)

top_10_fdi = latin_sorted.head(10)

fig_bar_fdi_lamerica = px.bar(
    top_10_fdi,
    y="fdi_USA_2018 (million)",
    x="country_name",
    color="country_name",
    text="fdi_USA_2018 (million)",
    height=600,
    title="Latin America: Top 10 Countries for FDI in USA (yr 2018)",
)
fig_bar_fdi_lamerica.update_traces(texttemplate="%{text:.2s}", textposition="outside")
fig_bar_fdi_lamerica.update_layout(uniformtext_minsize=8, uniformtext_mode="hide")
fig_bar_fdi_lamerica.show()


scatter_top10_tech = px.scatter(
    top_10_fdi,
    y="fdi_USA_2018 (million)",
    x="tech_export_2018 (million)",
    color="country_name",
    title="Latin America: Top 10 Countries for FDI in USA vs Innovation-Technology (yr 2018)",
)
scatter_top10_tech.write_image(
    "Top 10 L. American FDI countries vs Tech scatter plot.png"
)
scatter_top10_tech.show()

scatter_top10_gdp = px.scatter(
    top_10_fdi,
    y="fdi_USA_2018 (million)",
    x="GDP_2018 (million)",
    color="country_name",
    title="Latin America: Top 10 Countries for FDI in USA vs GDP (yr 2018)",
)
scatter_top10_gdp.write_image(
    "Top 10 L. American FDI countries vs GDP scatter plot.png"
)
scatter_top10_gdp.show()

scatter_top10_dbr = px.scatter(
    top_10_fdi,
    y="fdi_USA_2018 (million)",
    x="doing_business_2018",
    color="country_name",
    title="Latin America: Top 10 Countries for FDI in USA vs Ease of Doing Business Rating (yr 2018)",
)
scatter_top10_dbr.write_image(
    "Top 10 L. American FDI countries vs db rating scatter plot.png"
)
scatter_top10_dbr.show()


la10_scattermap = px.scatter_mapbox(
    top_10_fdi,
    lat="lat",
    lon="lng",
    color="fdi_USA_2018 (million)",
    hover_data=["country_name"],
    zoom=1,
)
la10_scattermap.write_image("Latin America top 10 FDI scatter map.png")
la10_scattermap