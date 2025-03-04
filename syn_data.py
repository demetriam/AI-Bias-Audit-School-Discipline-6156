import numpy as np
import pandas as pd

np.random.seed(42)


num_schools = 5000  

synthetic_data = pd.DataFrame({
    "SCHID": np.arange(100000, 100000 + num_schools) 
})


synthetic_data["SCH_PSDISC_OOMOOS_BL_M"] = np.random.poisson(lam=5, size=num_schools)  
synthetic_data["SCH_PSDISC_OOMOOS_WH_F"] = np.random.poisson(lam=3, size=num_schools)  
synthetic_data["TOT_PSDISC"] = synthetic_data["SCH_PSDISC_OOMOOS_BL_M"] + synthetic_data["SCH_PSDISC_OOMOOS_WH_F"]


mask = np.random.rand(num_schools) < 0.05 
synthetic_data.loc[mask, "SCH_PSDISC_OOMOOS_BL_M"] = np.nan


synthetic_data.to_csv("synthetic_school_discipline.csv", index=False)

print("\n Dataset saved !")
print(synthetic_data.head())