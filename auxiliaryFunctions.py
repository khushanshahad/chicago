# auxiliaryFunctions.py
def stats(dataframe):
    with open('IllinoisHauntingStats.txt', 'w') as f:
        f.write(f"Total Illinois hauntings: {len(dataframe)}\n")
        if 'city' in dataframe.columns:
            f.write("\nTop cities:\n")
            f.write(dataframe['city'].value_counts().head(10).to_string())

def success_message():
    print("Chicago hauntings heatmap created successfully!")
    