# Stock-Signal-Generation
The Stock Signal Generation project wants to implement a Python-based system of generating buy and sell signals for stocks from various technical indicators. These messages can prompt traders and investors to make deliberate decisions regarding the buying, selling, or holding of stocks.
Users will run the main Python script output to signaling generation from beginning to end. The developed system gets stock data, cleans it, generates signals, calculates profit/loss, stores results in the database and visualizes trading signals.
## Setup

1. **Set up PostgreSQL Database:**
   - Install PostgreSQL on your machine if you haven't already.
   - Create a new database named "Stock" using PostgreSQL command line or pgAdmin.
   - Run the provided SQL script `create_tables.sql` to create the necessary tables for storing stock equities data.

2. **Data Cleaning (Optional):**
   - If required, clean the data to ensure consistency and accuracy using Python scripts in the `data_cleaning` directory.

3. **Python Program Development:**
   - Navigate to the `python_program` directory.
   - Install the required Python packages using `pip install -r requirements.txt`.
   - Run the Python scripts to interact with the PostgreSQL database, generate trading signals, calculate profit/loss, and store results.
   - View the code comments for detailed explanations.

4. **Visualize Trading Data:**
   - Use the provided Python scripts in the `visualization` directory to visualize trading data.
   - Execute the scripts and view the generated plots to analyze stock performance and trading signals.
