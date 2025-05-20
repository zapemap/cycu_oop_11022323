import pandas as pd

# Load CSV data
df = pd.read_csv('20250520/midterm_scores.csv')

subjects = ['Chinese', 'English', 'Math', 'History', 'Geography', 'Physics', 'Chemistry']

# List to store results
results = []

print("Students with more than 4 failing subjects (<60):")
for idx, row in df.iterrows():
    failed = [subj for subj in subjects if row[subj] < 60]
    if len(failed) >= 4:  # 修改條件為大於 4 科不及格
        # 將符合條件的學生資料加入 results 清單
        results.append({
            'Name': row['Name'],
            'StudentID': row['StudentID'],
            'FailedSubjects': ', '.join(failed)
        })
        print(f"{row['Name']} (ID: {row['StudentID']}), Failed subjects: {', '.join(failed)}")

# Convert results to DataFrame and export to CSV
results_df = pd.DataFrame(results)
results_df.to_csv('20250520/failing_students.csv', index=False)

print("Results have been exported to '20250520/failing_students.csv'.")