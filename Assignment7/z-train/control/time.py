from datetime import datetime

data = f"{datetime.now().strftime('%Y/%m/%d %HH %MM %SS')}" \
    f"cpu usage (%): {cpu_usage_mean}% \n"