import pandas as pd
from connector_config import get_connection

def insert_cleaned_data():
    # Load CSV
    df = pd.read_csv("prescriptions.csv")

    # Clean duplicate records
    df_cleaned = df.drop_duplicates()

    # Connect and insert
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prescriptions (
            patient_id INT,
            patient_name VARCHAR(255),
            age INT,
            gender VARCHAR(10),
            disease VARCHAR(255),
            medicine VARCHAR(255),
            prescription_date DATE
        )
    """)
    conn.commit()

    insert_query = """
        INSERT INTO prescriptions (patient_id, patient_name, age, gender, disease, medicine, prescription_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    records = df_cleaned.values.tolist()
    cursor.executemany(insert_query, records)

    conn.commit()
    print(f"{cursor.rowcount} records inserted after cleaning.")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    insert_cleaned_data()