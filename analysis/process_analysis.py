import pandas as pd

def run_process_analysis():
    data = pd.read_csv("data/process_data.csv")

    avg_time = data.groupby("process_step")["time_minutes"].mean()
    total_cost = data.groupby("process_step")["cost"].sum()

    bottleneck_step = avg_time.idxmax()

    return {
        "avg_time": avg_time,
        "total_cost": total_cost,
        "bottleneck": bottleneck_step
    }
