# import pandas as pd
# import sqlite3

# file_paths = {
#     "Expulsions": "/Users/dede/Desktop/AI-Bias-Audit/2017-18-crdc-data-corrected-publication 2/2017-18 Public-Use Files/Data/SCH/CRDC/CSV/Expulsions.csv",
#     "Suspensions": "/Users/dede/Desktop/AI-Bias-Audit/2017-18-crdc-data-corrected-publication 2/2017-18 Public-Use Files/Data/SCH/CRDC/CSV/Suspensions.csv",
#     "Referrals_Arrests": "/Users/dede/Desktop/AI-Bias-Audit/2017-18-crdc-data-corrected-publication 2/2017-18 Public-Use Files/Data/SCH/CRDC/CSV/Referrals_Arrests.csv",
#     "Restraint_Seclusion": "/Users/dede/Desktop/AI-Bias-Audit/2017-18-crdc-data-corrected-publication 2/2017-18 Public-Use Files/Data/SCH/CRDC/CSV/Restraint_Seclusion.csv",
#     "Offenses": "/Users/dede/Desktop/AI-Bias-Audit/2017-18-crdc-data-corrected-publication 2/2017-18 Public-Use Files/Data/SCH/CRDC/CSV/Offenses.csv",
#     "Enrollment": "/Users/dede/Desktop/AI-Bias-Audit/2017-18-crdc-data-corrected-publication 2/2017-18 Public-Use Files/Data/SCH/CRDC/CSV/Enrollment.csv",
#     "Corporal_punishment": "/Users/dede/Desktop/AI-Bias-Audit/2017-18-crdc-data-corrected-publication 2/2017-18 Public-Use Files/Data/SCH/CRDC/CSV/Corporal_punishment.csv",
# }

# conn = sqlite3.connect("school_data.db")
# cursor = conn.cursor()
# for name, path in file_paths.items():
#     print(f"Loading {name} into SQLite database...")
#     for chunk in pd.read_csv(path, low_memory=False, dtype=str, chunksize=10000, encoding='ISO-8859-1'):
#         chunk.to_sql(name, conn, if_exists="append", index=False)

# print("\nLoaded")


# tables = file_paths.keys()
# missing_schid_tables = []

# cursor.execute("PRAGMA table_info(Expulsions)")
# columns = cursor.fetchall()
# column_names = [col[1] for col in columns]  
# print("\n Columns in Expulsions:", column_names)

# for table in tables:
#     print(f"\nChecking columns in {table}...")
#     cursor.execute(f"PRAGMA table_info({table})")
#     columns = cursor.fetchall()
#     column_names = [col[1] for col in columns] 
#     print(column_names)

#     if "SCHID" not in column_names:
#         missing_schid_tables.append(table)

# if missing_schid_tables:
#     print("\n Missing SCHID", missing_schid_tables)
#     conn.close()
#     raise ValueError("needs SCHID")

# for table in tables:
#     print(f"SCHID in {table}...")
#     cursor.execute(f"PRAGMA table_info({table})")
#     columns = cursor.fetchall()
#     column_names = [col[1] for col in columns] 
# if "SCHID" in column_names:
#     print(f"\n SCHID exists in {table}")
# else:
#     print(f"\n⚠️ SCHID missing in {table}")
#     cursor.execute(f"ALTER TABLE {table}")
#     cursor.execute(f"UPDATE {table} SET SCHID = CAST(SCHID AS INTEGER);")
#     conn.commit()


# query = """
# SELECT *
# FROM Expulsions
# LEFT JOIN Suspensions USING(SCHID)
# LEFT JOIN Referrals_Arrests USING(SCHID)
# LEFT JOIN Restraint_Seclusion USING(SCHID)
# LEFT JOIN Offenses USING(SCHID)
# LEFT JOIN Enrollment USING(SCHID)
# LEFT JOIN Corporal_punishment USING(SCHID)
# """

# final_df = pd.read_sql(query, conn)
# final_df.to_csv("final_merged_data_sql.csv", index=False)

# print("\n dataset saved")
# conn.close()