# log-reader
Log reader for 2015+ Subaru WRX. Supports both VA and VB platforms. The tool reviews the ECU sensor data to identify issues related to engine air fuel corrections and knock detection.

The following monitors will need to be enabled on the Cobb Accessport:
```
Accel Position (%)
Feedback Knock (degrees)
Fine Knock Learn (degrees)
Dyn Adv Mult (value)
AF Sens 1 Ratio (AFR)
Comm Fuel Final (AFR)
AF Correction 1 (%)
AF Learning 1 (%)
```

To run the tool:
```bash
python3 readlog.py datalog1.csv
```
