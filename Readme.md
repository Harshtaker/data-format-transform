# 🧠 Data Format Transformation Project

This project transforms two telemetry datasets — one using ISO 8601 timestamps and the other using Unix milliseconds — into a unified format.

✅ Designed to demonstrate:
- Timestamp conversion
- JSON parsing
- Data merging
- Sorting by time and sensor

---

## 📁 Files

| Filename         | Description                               |
|------------------|-------------------------------------------|
| `main.py`        | Main Python script to run the transformation and tests |
| `data-1.json`    | Telemetry data with ISO timestamp format  |
| `data-2.json`    | Telemetry data with Unix milliseconds     |
| `data-result.json` | Expected result (used for testing output) |

---

## ⚙️ How It Works

1. Loads both input JSON files
2. Converts ISO timestamps (if needed) to milliseconds
3. Merges the datasets
4. Sorts the result by:
   - `timestamp` ascending
   - `sensor` descending (so `"beta"` comes before `"alpha"`)
5. Compares output to the expected result

---

## 🚀 How to Run

```bash
python main.py
