# DEMO 2 – Sustainable Development Goals (SDG / ODS 2030) Euskadi

The main goal of this demo was to showcase an end-to-end data integration and ETL process in Power BI, consolidating heterogeneous datasets regarding the 2030 Agenda for Sustainable Development in the Basque Country (Euskadi).

Unlike [the previous demo](../00_DemoVentas/README.md), this dashboard features an advanced data model that integrates multiple geographical levels, demographic statistics, social welfare indicators, and spatial GeoJSON boundaries.

---

### Data Sources & ETL Artifacts

The standalone ZIP archive contains only the essential, trimmed tables directly required to run the main dashboard:

* `./ORIGENES-DATOS_Demo_2_ODS-2030-EUS.zip`

> [!NOTE]
> However, for the complete dataset, this main repository includes the full `./sources/` folder structure, containing every raw data source, individual `README.md` documentation files detailing provenance, all intermediate transformation files, and the full step-by-step ETL pipeline scripts:

---

## Data Model & Domain Overview

The underlying model correlates multiple datasets to analyze Euskadi's progress across various Sustainable Development Goals:

* **Geographical Hierarchies & Spatial Data:** Regional boundaries (*CAPV*), Historical Territories (*Araba, Bizkaia, Gipuzkoa*), functional region areas (comarcas), and municipal shapefiles formatted for Shape Maps, mainly in WGS84 coordinates.
* **Demographics:** Population census categorized by municipality, age cohorts, gender, and spatial coordinate mappings.
* **Social Welfare & Security:** Historical recipient stats for Minimum Guaranteed Income (*RGI*), social perception data, penal infractions, and gender violence tracking.
* **Health & Education:** Life expectancy metrics, mortality statistics, and ICT competency rates across demographics.
* **SDG Indicators:** Global and regional indicator tracking across Goals 1 through 17.

---

## Key Power BI Features Demonstrated

* **Complex ETL & Query Folding:** Power Query transformations across disparate file formats (`.csv`, `.xlsx`, `.mdb`, `.json`).
* **Spatial Mapping:** Integration of custom GeoJSON boundaries for regional and municipal filled maps.
* **Relational Modelling:** Multi-level dimensional schema connecting factual ODS metrics with geographical and demographic dimensions.
* **Advanced Analytics & Visuals:** Cross-filtering dashboards, custom KPIs, trend line projections, and decomposition trees for socio-economic indicators.
