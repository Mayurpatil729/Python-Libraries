<!-- @format -->

### 1. **DIKW Hierarchy**

The DIKW (Data, Information, Knowledge, Wisdom) hierarchy is a framework that represents the relationships between data, information, knowledge, and wisdom.

- **Data**: Raw, unprocessed facts without context (e.g., numbers, text).
- **Information**: Processed data that provides meaning (e.g., sales data organized in a report).
- **Knowledge**: Insights gained from analyzing information, often answering "how" (e.g., sales trends over time).
- **Wisdom**: Applying knowledge to make decisions or solve problems, often answering "why."

### 2. **Process of Dashboard Design**

Designing a dashboard involves several steps:

- **Define Objectives**: Understand what questions the dashboard should answer and who the end-users are.
- **Identify Key Metrics**: Determine the KPIs (Key Performance Indicators) relevant to the objectives.
- **Collect Data**: Gather data from various sources ensuring it's accurate and up-to-date.
- **Choose Visualization Types**: Select appropriate charts and graphs to represent data effectively.
- **Design Layout**: Organize the dashboard for intuitive navigation and readability.
- **Iterate and Improve**: Regularly update and refine the dashboard based on user feedback.

### 3. **Why Streamlit?**

Streamlit is a popular Python framework for building web applications because:

- **Simplicity**: It allows you to create interactive web apps with minimal code.
- **Speed**: Rapid prototyping and deployment make it easy to build and test data apps quickly.
- **Integration**: It integrates seamlessly with popular Python libraries (e.g., Pandas, NumPy, Matplotlib).

### 4. **Why is Streamlit Fast and Easy to Build Web Apps?**

- **No HTML/CSS/JavaScript**: You only need Python to create web apps.
- **Reactive Programming**: Streamlit automatically updates the app in real-time when the data changes.
- **Minimal Boilerplate**: Streamlit handles much of the backend setup, so you focus only on the logic and data visualization.

### 5. **Installing Streamlit**

To install Streamlit, run the following command in your terminal:

```bash
pip install streamlit
```

After installation, you can start building your app by running:

```bash
streamlit run your_script.py
```

### 6. **Python Data Ecosystem**

The Python data ecosystem consists of various libraries and tools for data manipulation, visualization, and machine learning, such as:

- **Data Manipulation**: Pandas, NumPy
- **Data Visualization**: Matplotlib, Seaborn, Plotly
- **Machine Learning**: Scikit-learn, TensorFlow, PyTorch
- **Data Access**: SQLAlchemy, SQLite, CSV, JSON

### 7. **3 Simple Principles of Streamlit**

1. Embrace Scripting: Streamlit lets you build apps using just Python scripting. You can create a fully functional web app with only a few lines of code, making it accessible even to those with no web development experience.

2. Weave in Interaction: Adding interactive elements like sliders, buttons, and checkboxes is as simple as declaring a variable. Streamlit automatically updates your app in real-time as you save changes to the source file, without the need to write backend code, handle HTTP requests, or use HTML, CSS, or JavaScript.

3. Deploy Instantly: With Streamlit, you can effortlessly share, manage, and deploy your apps directly using Streamlit Cloud. This makes it easy to make your app available to others without needing to worry about complex deployment processes—all for free!

### 8. **Deploying a Streamlit App**

You can deploy a Streamlit app using:

- **Streamlit Cloud**: Streamlit offers its own cloud service for hosting apps.
- **Cloud Providers**: Use platforms like AWS, Google Cloud, Heroku, or Azure.
- **Docker**: Create a Docker container to deploy your app in any cloud environment.

---

Here's a detailed note on performing Exploratory Data Analysis (EDA) and data visualization using Altair and Plotly:

### **Performing EDA and Data Visualization**

**1. Experimental Phase:**

- The EDA phase involves experimenting with various libraries and creating visualizations to better understand the data's patterns, relationships, and distributions.
- This phase helps to identify trends, outliers, and potential data quality issues.

**2. Libraries Used for Visualization:**

- **Altair**: A declarative statistical visualization library in Python, ideal for creating complex and interactive plots with concise code.
- **Plotly**: An interactive graphing library that offers flexibility and rich visualization capabilities, suitable for dashboards and web applications.

**3. Visualizations Used in the Dashboard:**

- **Heatmap (Altair)**: A graphical representation of data where individual values are represented as colors. Useful for displaying correlation matrices, comparing variables, or showing patterns in data.
- **Donut Chart (Altair)**: A variation of the pie chart with a central cut-out, used to show the proportion of categorical data or segment comparisons within a whole.

- **Choropleth Map (Plotly)**: A map where regions are colored based on data values, often used for geographical data analysis, such as population density, sales across different regions, or COVID-19 case distributions.

These visualizations provide a comprehensive view of the dataset and are instrumental in identifying insights during the EDA process.

---

### **1. PyInstaller**

- **Purpose**: Converts Python applications into standalone executables that can run on Windows, macOS, and Linux without requiring users to install Python.
- **Key Features**:
  - Bundles Python code, dependencies, and resources into a single executable file or a folder.
  - Supports various formats: single executable, directory-based, or one-file mode.
  - Handles complex dependencies, including packages like NumPy, Pandas, and PyQt.
- **Use Case**: Ideal for distributing Python applications to users who may not have Python installed on their system.

### **2. PyOxidizer**

- **Purpose**: A modern tool for packaging Python applications into executables, optimized for speed and efficiency.
- **Key Features**:
  - Embeds the Python interpreter and your code into a single executable file.
  - Uses Rust as the underlying language, making it efficient and fast.
  - Creates small, self-contained executables with faster startup times.
- **Use Case**: Great for developers looking to create optimized, standalone executables with minimal dependencies.

### **3. cx_Freeze**

- **Purpose**: Another tool for converting Python scripts into executables that can be run on different platforms.
- **Key Features**:
  - Cross-platform support for Windows, macOS, and Linux.
  - Creates executables by analyzing dependencies and including necessary libraries.
  - Allows customization of build options via setup scripts.
- **Use Case**: Suitable for building simple Python applications into executables, especially when you need a straightforward, flexible, and cross-platform solution.

These libraries are helpful for packaging Python applications into distributable forms, ensuring that your software can be easily shared and used by others without requiring a Python environment.
