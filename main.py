import pandas as pd
import matplotlib.pyplot as plt
from mysql.connector import Error
from connector_config import get_connection

def show_common_medications():
    try:
        conn = get_connection()
        query = """
            SELECT medicine, COUNT(*) as count 
            FROM prescriptions 
            GROUP BY medicine 
            ORDER BY count DESC 
            LIMIT 5
        """
        df = pd.read_sql(query, conn)
        print("\n Top 5 Common Medications:")
        print(df.to_string(index=False))
        df.plot(kind='bar', x='medicine', y='count', title='Top 5 Common Medications', color='orange')
        plt.xlabel('Medicine')
        plt.ylabel('Count')
        plt.tight_layout()
        plt.show()
    except Error as e:
        print(" Error:", e)

def show_monthly_disease_report():
    try:
        conn = get_connection()
        query = """
            SELECT DATE_FORMAT(prescription_date, '%Y-%m') AS month, disease, COUNT(*) as count
            FROM prescriptions
            GROUP BY month, disease
        """
        df = pd.read_sql(query, conn)
        report = df.pivot(index='month', columns='disease', values='count').fillna(0)
        print("\n Monthly Disease Report:")
        print(report)
        report.plot(kind='bar', stacked=True, figsize=(10, 6))
        plt.title("Monthly Disease Count")
        plt.xlabel("Month")
        plt.ylabel("Disease Count")
        plt.tight_layout()
        plt.show()
    except Error as e:
        print("Error generating monthly disease report:", e)

def show_monthly_patient_report():
    try:
        conn = get_connection()
        query = """
            SELECT DATE_FORMAT(prescription_date, '%Y-%m') AS month, COUNT(DISTINCT patient_id) AS patient_count
            FROM prescriptions
            GROUP BY month
        """
        df = pd.read_sql(query, conn)
        print("\n Monthly Unique Patient Count:")
        print(df.to_string(index=False))
        df.plot(x='month', y='patient_count', kind='line', marker='o', title='Monthly Patient Count')
        plt.xlabel("Month")
        plt.ylabel("Unique Patients")
        plt.tight_layout()
        plt.show()
    except Error as e:
        print("Error generating monthly patient report:", e)

def show_most_affected_disease():
    try:
        conn = get_connection()
        query = """
            SELECT disease, COUNT(*) AS count 
            FROM prescriptions 
            GROUP BY disease 
            ORDER BY count DESC 
            LIMIT 1
        """
        df = pd.read_sql(query, conn)
        print("\n Most Affected Disease:")
        print(df.to_string(index=False))
    except Error as e:
        print("Error:", e)

def show_patients_with_common_disease():
    try:
        conn = get_connection()
        query = """
            SELECT patient_id, patient_name, disease 
            FROM prescriptions 
            WHERE disease = (
                SELECT disease 
                FROM prescriptions 
                GROUP BY disease 
                ORDER BY COUNT(*) DESC 
                LIMIT 1
            )
        """
        df = pd.read_sql(query, conn)
        print("\n Patients with the Most Common Disease:")
        print(df.to_string(index=False))

        df['patient_name'].value_counts().plot(kind='barh', figsize=(8, 5), color='skyblue')
        plt.title('Patients with the Most Common Disease')
        plt.xlabel('Number of Records')
        plt.ylabel('Patient Name')
        plt.tight_layout()
        plt.show()

    except Error as e:
        print("Error:", e)

def show_patient_count_per_disease():
    try:
        conn = get_connection()
        query = """
            SELECT disease, COUNT(DISTINCT patient_id) AS patient_count
            FROM prescriptions
            GROUP BY disease
            ORDER BY patient_count DESC
        """
        df = pd.read_sql(query, conn)
        print("\n Patient Count per Disease:")
        print(df.to_string(index=False))
        df.plot(x='disease', y='patient_count', kind='bar', figsize=(9, 5), color='green', title='Patients per Disease')
        plt.tight_layout()
        plt.show()
    except Error as e:
        print("Error:", e)

def run_app():
    while True:
        print("\n Menu:")
        print("1. Show Top 5 Common Medications")
        print("2. Show Monthly Disease Report")
        print("3. Show Monthly Patient Report")
        print("4. Show Most Affected Disease")
        print("5. Show Patients with Common Disease")
        print("6. Show Patient Count per Disease")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            show_common_medications()
        elif choice == '2':
            show_monthly_disease_report()
        elif choice == '3':
            show_monthly_patient_report()
        elif choice == '4':
            show_most_affected_disease()
        elif choice == '5':
            show_patients_with_common_disease()
        elif choice == '6':
            show_patient_count_per_disease()
        elif choice == '7':
            print("Exiting the program.Thak You!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the app
if __name__ == "__main__":
    run_app()
