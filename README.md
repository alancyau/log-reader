# log-reader
Log reader for 2015+ Subaru WRX. Supports both VA and VB platforms. The tool reviews the ECU sensor data to identify issues related to engine air fuel corrections and knock detection.

The following monitors will need to be enabled on the Cobb Accessport:

- AF Correction 1 (%)
- AF Learning 1 (%)
- AF Sens 1 Ratio (AFR)
- AVCS Exh Left (retard (degrees))
- AVCS Exh Right (retard (degrees))
- AVCS In Left (advance (degrees))
- AVCS In Right (advance (degrees))
- Accel Position (%)
- Baro Pressure (psi)
- Boost (psi)
- Calculated Load (g/rev)
- Closed Loop Sw (status)
- Comm Fuel Final (AFR)
- Coolant Temp (F)
- Dyn Adv Mult (value)
- Feedback Knock (degrees)
- Fine Knock Learn (degrees)
- Fuel Pressure (psi)
- Gear Position (gear)
- Ignition Timing (degrees)
- Inj Duty Cycle (%)
- Intake Temp (F)
- Intake Temp Manifold (F)
- Limits Boost Table Base Rel SL (psi)
- MAF Freq (kHz)
- Oil Temp (F)
- RPM (RPM)
- Req Torque (N-m)
- Roughness Cyl 1 (misfire count)
- Roughness Cyl 2 (misfire count)
- Roughness Cyl 3 (misfire count)
- Roughness Cyl 4 (misfire count)
- TGV Map Ratio (multiplier)
- Target Boost Final Rel SL (psi)
- Throttle Pos (%)
- Wastegate Pos Actual (mm)

To run the tool:
```bash
python3 readlog.py datalog1.csv
```
