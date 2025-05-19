# FDI Flask Agent

This is a simple prototype agent to be triggered from Oracle Fusion Data Intelligence (FDI) via a Data Action.

## 🔧 How It Works

- Accepts a POST request with `scenario_id` and `segment_name`
- Returns a JSON response with a recommendation

## 🧪 Sample Input
```json
{
  "scenario_id": "S123",
  "segment_name": "High Value Customers"
}
