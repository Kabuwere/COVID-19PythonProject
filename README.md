# COVID-19PythonProject
🚀 Project Overview
The COVID-19 Global Data Tracker analyzes worldwide COVID-19 cases, deaths, recoveries, and vaccinations. It uses Python and data science tools to perform exploratory data analysis (EDA), visualize trends, and provide data-driven insights into the pandemic.

🏗 Project Features
✅ Data Collection → Loads COVID-19 data from Our World in Data (owid-covid-data.csv).
✅ Data Cleaning → Handles missing values, filters key countries (Kenya, USA, India, Brazil, Germany).
✅ Exploratory Analysis → Tracks cases, deaths, vaccinations, and fatality rates over time.
✅ Visualizations → Generates line charts, bar charts, and maps to show trends.
✅ Automated Reporting → Saves plots & outputs into an outputs/ directory.
✅ Interactive Map → Uses Plotly to display a choropleth map of global cases.

🔹 Required Libraries
Ensure you have the following Python libraries installed:
pip install pandas matplotlib seaborn plotly

📂 Project Structure
COVID-19-Tracker/
│── data/
│   ├── owid-covid-data.csv    # COVID-19 dataset
│── outputs/plots/             # Saved analysis images
│── outputs/global_cases_map.html  # Choropleth map HTML
│── covid_tracker.py           # Main Python script
│── README.md    

Example output (map)

![image](https://github.com/user-attachments/assets/c68c47f9-6e40-44fc-b640-34b88bcb836b)

🔍 How to Run the Project
1️⃣ Download the dataset from Our World in Data.
2️⃣ Save the CSV in the COVID-19-Tracker/data/ folder.
3️⃣ Run the script in a terminal or Jupyter Notebook:

python covid_tracker.py
4️⃣ Check results → Visualization files will be saved in the outputs/plots/ folder.
5️⃣ Open the choropleth map → View outputs/global_cases_map.html in your browser.

📊 Analysis Covered
1️⃣ COVID-19 Cases Over Time
2️⃣ Fatality Rate Comparison Between Countries
3️⃣ Vaccination Progress → Tracks % of population vaccinated.
4️⃣ Interactive Global Case Map → Using Plotly Choropleth.

🚀 Key Insights (Sample Findings)
🔹 Vaccination Disparity → Developed nations show higher vaccination rates.
🔹 Fatality Trends → Countries with strong healthcare systems maintain lower fatality rates.
🔹 Wave Patterns → Peaks occur every 3-4 months, influenced by seasonal factors & policies.
🔹 Vaccination Impact → Countries with early vaccine rollouts saw fewer cases post-peak.

🛠 Future Enhancements
✅ Interactive Dashboard using Streamlit or Dash
✅ Machine Learning Forecasts for case trends
✅ Real-time Data API Integration
✅ Geospatial Analysis using GeoPandas

📧 Contributors & Contact
Susan Kabuwere 📧 Email → kabuwere@gmail.com
