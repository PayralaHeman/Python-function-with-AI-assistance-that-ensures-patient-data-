import pandas as pd
import uuid

def anonymize_patient_data(df):
    """
    Removes personal details and replaces PatientID with unique IDs.
    """
    df = df.copy()

    # Drop sensitive columns
    for col in ["Name", "Address", "Phone"]:
        if col in df.columns:
            df.drop(col, axis=1, inplace=True)

    # Replace PatientID with random UUIDs
    if "PatientID" in df.columns:
        df["PatientID"] = [str(uuid.uuid4()) for _ in range(len(df))]

    return df

# Example dataset
data = {
    "PatientID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 40, 55],
    "Disease": ["Flu", "Diabetes", "Hypertension"],
    "Address": ["NY", "CA", "TX"],
    "Phone": ["11111", "22222", "33333"]
}

df = pd.DataFrame(data)

print("📊 Original Data:\n", df)
print("\n✅ Anonymized Data:\n", anonymize_patient_data(df))
