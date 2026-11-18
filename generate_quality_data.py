import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
n_rows = 5000
start_date = datetime(2025, 1, 1)

# Lookup lists
shifts = ['Morning', 'Afternoon', 'Night']
product_lines = ['Hydraulic Valve A', 'Actuator X-200', 'Pressure Sensor Pro', 'Control Valve B']
suppliers = ['Supplier Alpha', 'Supplier Beta', 'Supplier Gamma']
defect_categories = ['Dimensional Error', 'Surface Finish', 'Material Flaw', 'Assembly Issue', 'None']
unit_costs = {'Hydraulic Valve A': 120, 'Actuator X-200': 250, 'Pressure Sensor Pro': 85, 'Control Valve B': 180}

# Generate random dates over 12 months
date_list = [start_date + timedelta(days=int(np.random.randint(0, 365))) for _ in range(n_rows)]
date_list.sort()

data = []
for i in range(n_rows):
    prod_date = date_list[i]
    shift = np.random.choice(shifts, p=[0.4, 0.4, 0.2])
    product = np.random.choice(product_lines)
    supplier = np.random.choice(suppliers, p=[0.5, 0.3, 0.2])
    units_produced = int(np.random.randint(50, 200))
    
    # Base defect rate
    defect_rate = np.random.uniform(0.01, 0.04)
    
    # INJECTING THE ANOMALY: Supplier Beta, Q3 (July-Sept), Night Shift -> Higher dimensional errors
    is_q3 = 7 <= prod_date.month <= 9
    if supplier == 'Supplier Beta' and is_q3 and shift == 'Night':
        defect_rate = np.random.uniform(0.12, 0.22) # Spike up to 22% defect rate
    
    defective_units = int(np.round(units_produced * defect_rate))
    
    # Choose primary defect category based on context
    if defective_units == 0:
        category = 'None'
    elif supplier == 'Supplier Beta' and is_q3 and shift == 'Night':
        category = np.random.choice(['Dimensional Error', 'Surface Finish'], p=[0.8, 0.2])
    else:
        category = np.random.choice(defect_categories[:-1], p=[0.3, 0.3, 0.2, 0.2])
        
    cost_per_unit = unit_costs[product]

    data.append({
        'Batch_ID': f'BATCH-{1000 + i}',
        'Production_Date': prod_date.strftime('%Y-%m-%d'),
        'Shift': shift,
        'Product_Line': product,
        'Supplier_ID': supplier,
        'Units_Produced': units_produced,
        'Defective_Units': defective_units,
        'Defect_Category': category,
        'Unit_Cost': cost_per_unit
    })

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('manufacturing_quality_data.csv', index=False)
print("Dataset generated successfully: manufacturing_quality_data.csv with 5,000 rows!")