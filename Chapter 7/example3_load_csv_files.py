"""
Example 3: Working with CSV Files
"""
from langchain_community.document_loaders.csv_loader import CSVLoader

# Load the CSV file
loader = CSVLoader(file_path="./sample_data/california_housing_test.csv")
data = loader.load()

# Print the loaded data
for row in data:
    print(f"Content: {row.page_content}\n")
    print(f"Metadata: {row.metadata}\n")
    print("---")

# Customizing CSV parsing
custom_loader = CSVLoader(
    file_path="./sample_data/mlb_teams_2012.csv",
    csv_args={"delimiter": ",", "quotechar": '"', "fieldnames": ["Team", "Payroll", "Wins"]}
)
custom_data = custom_loader.load()
print(custom_data)
