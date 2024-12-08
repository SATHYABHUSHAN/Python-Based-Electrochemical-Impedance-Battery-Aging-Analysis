import pandas as pd
import plotly.express as px

#  path
file_path = r"C:\Users\sathy\Downloads\interview_assignment\cleaned_dataset\metadata.csv"

try:
    data = pd.read_csv(file_path)
    print("Dataset loaded successfully!")

    # Filter data for impedance operations
    impedance_data = data[data['type'] == 'impedance']

    
    if 'Re' in impedance_data.columns and 'Rct' in impedance_data.columns:
        
        impedance_data = impedance_data[['test_id', 'Re', 'Rct']].dropna()

        
        impedance_data['Cycle'] = impedance_data['test_id']

        # Ploting Re (Electrolyte Resistance) across cycles
        fig_re = px.line(
            impedance_data, x='Cycle', y='Re',
            title="Change in Estimated Electrolyte Resistance (Re) Over Cycles",
            labels={'Cycle': 'Cycle Number', 'Re': 'Electrolyte Resistance (Ohms)'},
            template='plotly_dark'
        )
        fig_re.show()

        # Ploting Rct (Charge Transfer Resistance) across cycles
        fig_rct = px.line(
            impedance_data, x='Cycle', y='Rct',
            title="Change in Estimated Charge Transfer Resistance (Rct) Over Cycles",
            labels={'Cycle': 'Cycle Number', 'Rct': 'Charge Transfer Resistance (Ohms)'},
            template='plotly_dark'
        )
        fig_rct.show()
    else:
        print("Error: The required columns 'Re' and 'Rct' are not present in the dataset.")

except FileNotFoundError:
    print(f"Error: File not found at path: {file_path}. Please check the file path.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
