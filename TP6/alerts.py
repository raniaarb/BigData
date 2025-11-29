def check_alerts(data):
    alerts = []

    if data["temperature"] > 80:
        alerts.append(f"🔥 HIGH TEMPERATURE on machine {data['machine_id']}")

    if data["vibration"] > 4:
        alerts.append(f"⚠️ HIGH VIBRATION on machine {data['machine_id']}")

    if data["pressure"] > 9:
        alerts.append(f"🔴 DANGEROUS PRESSURE on machine {data['machine_id']}")

    return alerts
