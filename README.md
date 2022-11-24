# log-reader
Log reader for 2015+ Subaru WRX. Supports both VA and VB platforms. The tool reviews the ECU sensor data to identify issues related to engine air fuel corrections and knock detection.

The following monitors will need to be enabled on the Cobb Accessport:

- AF Correction 1
- AF Learning 1
- AF Sens 1 Ratio
- AVCS Exh Left 
- AVCS Exh Right
- AVCS In Left 
- AVCS In Right
- Accel Position
- Baro Pressure
- Boost
- Calculated Load
- Closed Loop Sw
- Comm Fuel Final
- Coolant Temp
- Dyn Adv Mult
- Feedback Knock
- Fine Knock Learn
- Fuel Pressure
- Gear Position
- Ignition Timing
- Inj Duty Cycle
- Intake Temp
- Intake Temp Manifold
- Limits Boost Table Base Rel SL
- MAF Freq or MAF Volt
- Oil Temp
- RPM
- Req Torque
- Roughness Cyl 1
- Roughness Cyl 2
- Roughness Cyl 3
- Roughness Cyl 4
- TGV Map Ratio
- Target Boost Final Rel SL
- Throttle Pos
- Wastegate Pos Actual or Wastegate Duty

To run the tool:
```bash
python3 readlog.py datalog1.csv
```
