# BMI Calculator

A simple terminal-based Body Mass Index (BMI) calculator. Enter your weight and height to get your BMI and category.

## Requirements

- Python 3.x

## Run

```bash
python3 BMI-Calculator.py
```

## How to Use

1. Enter your weight in kilograms.
2. Enter your height in centimeters.
3. The program calculates your BMI and shows your category:
   - Underweight (≤ 18.5)
   - Normal (18.5 – 24.9)
   - Overweight (24.9 – 29.9)
   - Obese (> 29.9)

## Code Structure

- `BMI_hesaplama(kilo, boy_cm)` — calculates BMI from weight and height
- `BMI_kategori(BMI)` — determines the BMI category