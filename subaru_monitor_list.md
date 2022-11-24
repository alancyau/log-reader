Source: https://cobbtuning.atlassian.net/wiki/spaces/PRS/pages/97687600/Subaru+Monitor+List

Introduction
This document provides descriptions of each of the data monitors available to view and log in the current Accesstuner software and V3 Accessport firmware. Not all monitors are available for all vehicles due to differences in vehicle hardware and/or engine control unit (ECU) capabilities. Some monitors are only available in the latest ECU version (strategy) for a given vehicle.

For help with monitors specific to the COBB Custom Features, please see the separate COBB custom monitor guide.

Glossary of Acronyms
A/F = Air/Fuel

AT = Automatic Transmission

AVCS = Subaru's Active Valve Control System (i.e. variable valve timing)

CL = Closed Loop fueling

CVT = Continuously Variable Transmission

DAM = Dynamic Advance Multiplier

DIT = Subaru's "Direct Injection Turbo" motor (14-18 FXT, 15+ WRX, 19+ Ascent)

EQ Ratio = Equivalence Ratio

ECU = Engine Control Unit

FXT = Forester XT model

LGT = Legacy GT model

MAF = Mass Airflow

MT = Manual Transmission

OL = Open Loop fueling

RPM = Revolutions Per Minute (referring to engine speed)

TGV = Tumble Generator Valve

TPS = Throttle Position Sensor (or more generically referring to throttle position)

VDC = Vehicle Dynamics Control

VSS = Vehicle Speed Sensor (or more generically referring to vehicle speed)
Monitor Descriptions (in alphabetical order)
Note: Accesstuner name shown first; Accessport name shown second in parentheses.

NOTE: ALL MONITORS ARE NOT AVAILABLE FOR ALL VEHICLES DUE TO DIFFERENCES IN VEHICLE HARDWARE AND/OR ENGINE CONTROL UNIT (ECU) DIFFERENCES. SOME MONITORS ARE ONLY AVAILABLE IN THE LATEST ECU VERSION (STRATEGY).
AC Compressor Switch (AC Compressor Sw) -> Air conditioning compressor state as dictated by the ECU. Value is ON (or 1) when the compressor is commanded to engage.

Accelerator Position (Accel Position) -> Accelerator pedal opening angle percentage as determined by the accelerator position sensor.

Accelerator Voltage MAIN (Accel Volts Main) -> Main accelerator pedal position sensor output voltage.

Accelerator Voltage SUB (Accel Volts Sub) -> Sub accelerator pedal position sensor output voltage.

AF Correction 1 (AF Correction 1) -> Short-term (immediate) fueling correction in closed loop based on input from the front oxygen sensor. This is a percentage correction of the injector pulse width. Positive values indicate fuel is being added as a result of the correction. Negative values indicate fuel is being removed.

AF Correction 3 (AF Correction 3) -> Short-term (immediate) fueling correction in closed loop based on input from the rear oxygen sensor. This is a percentage correction of the closed loop fueling target. Positive values indicate fuel is being added as a result of the correction. Negative values indicate fuel is being removed.

AF Learning 1 (AF Learning 1) -> Long-term (learned) fueling correction based on patterns of 'A/F Correction #1' in closed loop, which is based on input from the front oxygen sensor. This is a percentage correction of the injector pulse width. These values are determined and applied based on four separate mass airflow ranges. This value represents the current correction that is being applied. Positive values indicate fuel is being added as a result of the correction. Negative values indicate fuel is being removed.

AF Learning 1 Idle 1 (AF Learning Idle1) -> Long-term (learned) fueling correction during idle conditions below the RPM breakpoint.

AF Learning 1 Idle 2 (AF Learning Idle2) -> Long-term (learned) fueling correction during idle conditions above RPM breakpoint.

AF Learning 1 Range A (AF Learning 1 A) -> Long-term (learned) fueling correction for airflow range 'A' based on patterns of 'A/F Correction #1'. This is a percentage correction of the injector pulse width. Positive values indicate fuel is being added as a result of the correction. Negative values indicate fuel is being removed. This value is determined and applied based on the first mass airflow range only. The mass airflow ranges are determined by the axis of the 'A/F Learning #1' table.

AF Learning 1 Range A1 (AF Learning 1 A1) -> Long-term (learned) fueling correction for load range 'A' during non-idle conditions below the RPM breakpoint.

AF Learning 1 Range A2 (AF Learning 1 A2) -> Long-term (learned) fueling correction for load range 'A' during non-idle conditions above the RPM breakpoint.

AF Learning 1 Range B (AF Learning 1 B) -> Long-term (learned) fueling correction for airflow range 'B' based on patterns of 'A/F Correction #1'. This is a percentage correction of the injector pulse width. Positive values indicate fuel is being added as a result of the correction. Negative values indicate fuel is being removed. This value is determined and applied based on the second mass airflow range only. The mass airflow ranges are determined by the axis of the 'A/F Learning #1' table.

AF Learning 1 Range B1 (AF Learning 1 B1) -> Long-term (learned) fueling correction for load range 'B' during non-idle conditions below the RPM breakpoint.

AF Learning 1 Range B2 (AF Learning 1 B2) -> Long-term (learned) fueling correction for load range 'B' during non-idle conditions above the RPM breakpoint.

AF Learning 1 Range C (AF Learning 1 C) -> Long-term (learned) fueling correction for airflow range 'C' based on patterns of 'A/F Correction #1'. This is a percentage correction of the injector pulse width. Positive values indicate fuel is being added as a result of the correction. Negative values indicate fuel is being removed. This value is determined and applied based on the third mass airflow range only. The mass airflow ranges are determined by the axis of the 'A/F Learning #1' table.

AF Learning 1 Range C1 (AF Learning 1 C1) -> Long-term (learned) fueling correction for load range 'C' during non-idle conditions below the RPM breakpoint.

AF Learning 1 Range C2 (AF Learning 1 C2) -> Long-term (learned) fueling correction for load range 'C' during non-idle conditions above the RPM breakpoint.

AF Learning 1 Range D (AF Learning 1 D) -> Long-term (learned) fueling correction for airflow range 'D' based on patterns of 'A/F Correction #1'. This is a percentage correction of the injector pulse width. Positive values indicate fuel is being added as a result of the correction. Negative values indicate fuel is being removed. This value is determined and applied based on the fourth mass airflow range only. The mass airflow ranges are determined by the axis of the 'A/F Learning #1' table.

AF Learning 1 Range D1 (AF Learning 1 D1) -> Long-term (learned) fueling correction for load range 'D' during non-idle conditions below the RPM breakpoint.

AF Learning 1 Range D2 (AF Learning 1 D2) -> Long-term (learned) fueling correction for load range 'D' during non-idle conditions above the RPM breakpoint.

AF Learning 1 Range E1 (AF Learning 1 E1) -> Long-term (learned) fueling correction for load range 'E' during non-idle conditions below the RPM breakpoint.

AF Learning 1 Range E2 (AF Learning 1 E2) -> Long-term (learned) fueling correction for load range 'E' during non-idle conditions above the RPM breakpoint.

AF Learning 3 (AF Learning 3) -> Long-term (learned) fueling correction based on patterns of 'A/F Correction #3', which is based on input from the rear oxygen sensor. This is a percentage correction of the injector pulse width. Positive values indicate fuel is being added as a result of the correction. Negative values indicate fuel is being removed.

AF Sensor 1 Current (AF Sens 1 Curr) -> Front oxygen sensor output current in milliamps (mA).

AF Sensor 1 Ratio (AF Sens 1 Ratio) -> Air/fuel ratio based on the front oxygen sensor.

AF Sensor 3 Voltage (AF Sens 3 Volts) -> Rear oxygen sensor output voltage.

AF Sensor 3 Voltage DIRECT (AF Sens 3 Volts Direct) -> Rear oxygen sensor output voltage direct (higher precision and full 0-5v range as compared to non-direct monitor).

Aggressive Start 1 Active (Aggr Start 1 Active) -> Aggressive start state (type 1) which determines specific table switching in the ECU. Value is ON (or 1) when an aggressive start (for type 1 switching) is detected (generally higher and/or quicker positive accelerator movement).

Aggressive Start 2 Active (Aggr Start 2 Active) -> Aggressive start state (type 2) which determines specific table switching in the ECU. Value is ON (or 1) when an aggressive start (for type 2 switching) is detected (generally higher and/or quicker positive accelerator movement).

Air Bypass Valve Commanded (Air Bypass Valve Open) -> Commanded air bypass valve state as dictated by the ECU. Valve is either commanded 'Closed' (or 0) or 'Open' (or 1).

Ambient Air Temperature EST (Ambient Air Temp Est) -> Estimated ambient temperature as determined by the ECU based on intake temperature and coolant temperature.

AT Fuel Cut Switch (AT Fuel Cut Sw) -> Automatic transmission fuel cut request as relayed by the transmission control module.

AT Lock up Switch (AT Lock up Sw) -> Lock-up status of the automatic transmission as relayed by the transmission control module.

AT Retard Switch (AT Retard Sw) -> Automatic transmission ignition retard request as relayed by the transmission control module.

AT Torque Down Perm Switch (AT Torq Per Sw) -> Automatic transmission torque-down permission as relayed by the transmission control module.

AVCS Exhaust Activation Post Reset Flag (AVCS Exh Activate Post Reset Flag) -> Value is 'ON' (or 1) when the post-reflash/reset AVCS exhaust control learned state is complete and 'OFF' (or 0) when it is not yet complete. After an ECU reflash or reset, the ECU defaults to disabling AVCS control until certain conditions are met at idle. The post-reflash/reset AVCS learned state must be complete before active AVCS control is allowed.

AVCS Exhaust Control Flag (AVCS Exh Control Flag) -> Value is 'ON' (or 1) when the AVCS exhaust control is currently active and 'OFF' (or 0) when it is inactive.

AVCS Exhaust Left (AVCS Exh Left) -> Exhaust Active Valve Control System (AVCS) timing for the left bank based on the corresponding exhaust camshaft position sensor.

AVCS Exhaust Right (AVCS Exh Right) -> Exhaust Active Valve Control System (AVCS) timing for the right bank based on the corresponding exhaust camshaft position sensor.

AVCS Exhaust Target Final LEFT (AVCS Exh Target Final L) -> Exhaust Active Valve Control System (AVCS) final target timing for the left bank.

AVCS Exhaust Target Final RIGHT (AVCS Exh Target Final R) -> Exhaust Active Valve Control System (AVCS) final target timing for the right bank.

AVCS Exhaust Target TABLE FINAL (AVCS Exh Table Final) -> This is the final AVCS exhaust table value after TGV blending and compensations are applied.

AVCS Exhaust Target TABLE TGV CLOSED (AVCS Exh TGV CL Table) -> This is the table value from the AVCS Exhaust Cam Retard Target (TGVs Closed) table before any compensations are applied.

AVCS Exhaust Target TABLE TGV OPEN (AVCS Exh TGV OP Table) -> This is the table value from the AVCS Exhaust Cam Retard Target (TGVs Open) table before any compensations are applied.

AVCS Exhaust Target With Comps TABLE (AVCS Exh Table) -> This is the table value from the AVCS Exhaust Cam Retard Target table with some compensations applied.

AVCS Intake Activation Post Reset Flag (AVCS In Activate Post Reset Flag) -> Value is 'ON' (or 1) when the post-reflash/reset AVCS intake control learned state is complete and 'OFF' (or 0) when it is not yet complete. After an ECU reflash or reset, the ECU defaults to disabling AVCS control until certain conditions are met at idle. The post-reflash/reset AVCS learned state must be complete before active AVCS control is allowed.

AVCS Intake Control Flag (AVCS In Control Flag) -> Value is 'ON' (or 1) when the AVCS intake control is currently active and 'OFF' (or 0) when it is inactive.

AVCS Intake Left (AVCS In Left) -> Intake Active Valve Control System (AVCS) timing for the left bank based on the corresponding intake camshaft position sensor.

AVCS Intake Right (AVCS In Right) -> Intake Active Valve Control System (AVCS) timing for the right bank based on the corresponding intake camshaft position sensor.

AVCS Intake Target Final LEFT (AVCS In Target Final L) -> Intake Active Valve Control System (AVCS) final target timing for the left bank.

AVCS Intake Target Final RIGHT (AVCS In Target Final R) -> Intake Active Valve Control System (AVCS) final target timing for the right bank.

AVCS Intake Target TABLE (AVCS In Table) -> This is the table value from the AVCS Intake Cam Advance Target table before any compensations are applied.

AVCS Intake Target TABLE FINAL (AVCS In Table Final) -> This is the final AVCS intake table value after TGV blending and compensations are applied.

AVCS Intake Target TABLE TGV CLOSED (AVCS In TGV CL Table) -> This is the table value from the AVCS Intake Cam Advance Target (TGVs Closed) table before any compensations are applied.

AVCS Intake Target TABLE TGV OPEN (AVCS In TGV OP Table) -> This is the table value from the AVCS Intake Cam Advance Target (TGVs Open) table before any compensations are applied.

AVCS Intake Target With Comps TABLE (AVCS In Table) -> This is the table value from the AVCS Intake Cam Advance Target table with some compensations applied.

Barometric Pressure (Baro Pressure) -> Barometric pressure based on the barometric pressure sensor.

Battery Voltage (Battery Volts) -> Battery voltage as determined by the battery voltage input to the ECU.

Boost Limits Base FINAL Rel Sea Level (Limits Boost Base Final Rel SL) -> This is the boost limit after all applicable boost compensations have been applied.

Boost Limits Base TABLE Rel Sea Level (Limits Boost Table Base Rel SL) -> This is the table value from the Boost Limits table.

Boost Limits TABLE Rel Sea Level (Limits Boost Table Rel SL) -> This is the table value from the Boost Limits table.

Boost Target FINAL Abs (Target Boost Final Abs) -> This is the boost target (in absolute pressure) after all boost target compensations have been applied.

Boost Target FINAL Rel (Target Boost Final Rel) -> This is the boost target in relative pressure (absolute boost target - barometric pressure) after all boost target compensations have been applied.

Boost Target FINAL Rel Sea Level (Target Boost Final Rel SL) -> This is the boost target after all boost target compensations have been applied. The underlying value is in absolute pressure with this relative value being calculated based on the assumption of sea level barometric pressure (14.7 psi).

Boost Target TABLE Rel Sea Level (Target Boost Table Rel SL) -> This is the table value from the Boost Targets table before any compensations are applied.

Calculated Load (Calculated Load) -> Engine load, in grams per crankshaft revolution, as calculated by the ECU. This value is determined as follows: (mass airflow * 60) / RPM.

Camshaft Position Switch (Camshaft Sw) -> Camshaft position sensor output. Value is ON (or 1) with camshaft rotation (i.e. when the engine is running).

Catalyst Temperature (Catalyst Temp) -> Estimated catalyst temperature as determined by the ECU.

Closed Loop Delay Count (CL Delay Count) -> This counter increments when conditions are met for a delayed closed to open loop fueling transition (primary OL fuel becomes active after delay is satisified which may or may not result in actual switch to OL). Will be set to its maximum value if delay threshold is zero in tune (or set to zero via conditions).

Closed Loop Fuel Target (CL Fuel Target) -> Target fueling in closed loop after all compensations have been applied. The ECU will attempt to hit this target in closed loop based on feedback from the oxygen sensor(s).

Closed Loop Fuel Target Base Lean Limit and CFF Transfer TABLE (CL Fuel Target Lean Table) -> This is the table value from the Closed Loop Fueling Target Base (Main) Lean Limit tables.

Closed Loop Fuel Target Base TABLE (CL Fuel Target Table) -> This is the table value from the Closed Loop Fueling Target Base (Main) tables.

Closed Loop Fuel Target ECT Comp TABLE (CL Fuel ECT Comp Table) -> This is the table value from the Closed Loop Fueling Target Compensation (Coolant Temp) table.

Closed Open Loop Switch (Closed Loop Sw) -> Closed/open loop fuel system status. Value is 'Closed' (or 1) in closed loop and 'Open' (or 0) in open loop. In closed loop, the ECU uses feedback from the oxygen sensor(s) to attempt to hit the closed loop fueling target. In open loop, this feedback is ignored.

Clutch Switch (Clutch Sw) -> Clutch switch output. Value is ON (or 1) when the clutch pedal is pushed in.

Commanded Fuel Final (Comm Fuel Final) -> This is the final commanded fueling target used in the injector pulse width calculation. This includes all compensations to the fueling target.

Commanded Fuel Primary OL Map (Comm Fuel Map) -> Commanded open loop fueling as determined by the 'Primary Open Loop Fueling' table(s) with all direct compensations applied.

Coolant Temperature (Coolant Temp) -> Coolant temperature based on the engine coolant temperature sensor.

CPC Purge Flow (CPC Purge Flow) -> Estimated current canister purge flow as determined by the ECU.

CPC Purge Fuel Learning (CPC Purge Fuel Learn) -> Canister purge trim learning component as determined by the ECU.

CPC Purge Fuel Trim (CPC Purge Fuel Trim) -> Fuel trim adder based on learning during canister purge control events. This correction is NOT reflected in other fuel trim monitors.

CPC Purge Valve Duty (CPC Purge Valve Duty) -> Duty ratio of the canister purge control solenoid as determined by the ECU.

Cranking Fuel IPW Base Group 1 TABLE (Cranking IPW 1 Table) -> This is the table value from the Cranking Fuel Injector Pulse Width Base (Group 1) tables during cranking before any compensations are applied.

Cranking Fuel IPW Base Group 2 TABLE (Cranking IPW 2 Table) -> This is the table value from the Cranking Fuel Injector Pulse Width Base (Group 2) tables during cranking before any compensations are applied.

Cranking Fuel IPW Base TABLE (Cranking IPW Table) -> This is the table value from the Cranking Fuel Injector Pulse Width Base tables during cranking before any compensations are applied.

Crankshaft Position Switch (Crankshaft Sw) -> Crankshaft position sensor output. Value is ON (or 1) with crankshaft rotation (i.e. when the engine is running).

CVT Lockup Status (CVT Lockup Status) -> Continuously variable transmission (CVT) torque converter lock-up state: 0 = Open, 2 = Partial, 4 = Full.

CVT Temperature (CVT Temp) -> Continuously variable transmission (CVT) fluid temperature as reported by the transmission control module (TCM).

Dyn Adv Adder (Dyn Adv Adder) -> Multiplier applied to the 'Dynamic Advance Adder Max...' map value to determine the portion (if any) of this adder that is applied to dynamic advance. This multiplier is determined by a number of factors which take into account the current knock condition and conditions that can potentially lead to knock.

Dyn Adv Adder A Multiplier (Dyn Adv A Mult) -> Multiplier applied to the 'Dynamic Advance Adder Max. A...' map value to determine the portion (if any) of this adder that is applied to dynamic advance. This multiplier is determined by a number of factors which take into account the current knock condition and conditions that can potentially lead to knock.

Dyn Adv Adder B Multiplier (Dyn Adv B Mult) -> Multiplier applied to the 'Dynamic Advance Adder Max. B...' map value to determine the portion (if any) of this adder that is applied to dynamic advance. This multiplier is determined by a number of factors which take into account the current knock condition and conditions that can potentially lead to knock.

Dyn Adv Primary Map Ratio (Dyn Adv Ratio) -> Map ratio multiplier that determines the map switching (or blending) between the 'high' and 'low' versions of the 'Dynamic Advance Max. Primary' tables. The final primary dynamic advance is determined as follows: (low table * ratio) + (high table * (1.0 - ratio)). This multiplier is determined by a number of factors which take into account the current knock condition and conditions that can potentially lead to knock.

Dynamic Advance Base TABLE (Dynamic Adv Base Table) -> This is the table value from the Dynamic Advance Base tables.

Dynamic Advance Final (Dynamic Adv) -> Dynamic advance map value with the following knock corrections applied: dynamic advance multiplier (DAM), feedback knock correction, and fine knock learning correction. This is the final dynamic advance that makes up a portion of total timing.

Dynamic Advance Learned (Dynamic Adv Lrn) -> Dynamic advance map value with only the following learned knock corrections applied: dynamic advance multiplier (DAM) and fine knock learning correction. This value does not include feedback knock correction.

Dynamic Advance Multiplier (Dyn Adv Mult) -> This is a learned correction applied to dynamic advance. The dynamic advance multiplier (DAM) is one of three knock responses. When conditions dictate that a change to the DAM is to occur, the current knock signal is referenced and the DAM is set to an initial value. If a knock event has occurred, the DAM will decrease. If there's no knock event, the DAM will increase (if no knock over a delay period). The DAM is reset to an initial value after an ECU reset or after a reflash. For the 02-05 WRX, the DAM ranges from 0 to 16 and its application to dynamic advance can be calculated as follows: dynamic advance map value * (DAM/16). For all other ECUs, the DAM ranges from 0 to 1 (decimal value) and is applied as follows: dynamic advance map value * DAM.

EGR Commanded (EGR Commanded) -> Exhaust Gas Recirculation (EGR) valve commanded.

EGR Estimate (EGR Estimate) -> Exhaust Gas Recirculation (EGR) valve actual as estimated by the ECU.

Engine Run Time (Engine Run Time) -> This is the counter that is incremented when the engine is running.

Engine Speed (RPM) -> Engine speed in crankshaft revolutions per minute based on the crankshaft position sensor.

Engine Speed Delta 1 (RPM Delta 1) -> Current RPM delta calculated (generally) as follows: (current RPM - previous RPM) with additional filtering.

Engine Speed Delta 2 (RPM Delta 2) -> Current RPM delta calculated (generally) as follows: (smoothed RPM - current RPM) with additional filtering.

Engine Speed Delta 3 (RPM Delta 3) -> Current RPM delta calculated (generally) as follows: (smoothed RPM - current RPM).

Engine Start MODE (Engine Start Mode) -> Engine start mode used as an input to some post-start enrichment tables.

Engine Torque (Engine Torque) -> Engine torque estimate by the ECU.

Evap Related Fuel Adder (Evap Fuel Adder) -> Evaporative systems related fuel adder (EQ ratio).

Exhaust Gas Temperature (Exh Gas Temp) -> Exhaust gas temperature (EGT) based on the EGT sensor located in the uppipe.

Exhaust Gas Temperature Voltage DIRECT (EGT Volts Direct) -> Exhaust Gas Temperature sensor output voltage direct.

Feedback Knock Correction (Feedback Knock) -> This is a correction applied to dynamic advance based on knock. Feedback knock correction is the default correction of the three knock responses. When conditions dictate that changes to the dynamic advance multiplier or fine knock learning are not called for, feedback knock correction will be active (within specific RPM and load ranges). When a knock event occurs, feedback knock correction will decrease from its initial value of zero. The correction will be held until there's no knock event over a delay period after which the correction value will increase by a specific value (and the process repeats until the value ramps back to zero). If there is a knock event over the delay period, the value will decrease further.

Fine Knock Learning (Fine Knock Learn) -> This is a learned correction applied to dynamic advance. Fine knock learning is one of three knock responses. Its values are stored and applied based on specific load and RPM ranges. When conditions dictate that changes to fine knock learning are to occur, the current knock signal is referenced. If a knock event has occurred, the learned value in the current load/RPM cell will decrease. If no knock event has occurred over a delay period for that cell, the learned value will increase. Limits are placed on positive fine knock learning depending on the current dynamic advance multiplier (DAM).

Fuel Cut (Fuel Cut) -> Number of cylinders involved in fuel cut as dictated by ECU. 0 = no fuel cut present.

Fuel Cut Flag (Fuel Cut Flag) -> Value is 'ON' (or 1) when the ECU is commanding a fuel cut and a value of 'OFF' (or 0) when no fuel cut is commanded.

Fuel Cut Mode (Fuel Cut Mode) -> This is the mode which indicates the fuel cut type that conditions would dictate (even if no fuel cut is currently active). Internal use only.

Fuel Injector Timing CRANKING TABLE (Inj Timing Crank Table) -> This is the table value from the Fuel Injector Start of Injection (Cranking) table.

Fuel Injector Timing Homogeneous TABLE (Inj Timing H Table) -> This is the final table value from the Fuel Injector Start of Injection (Homogeneous) Main table with compensations applied.

Fuel Injector Trim Fuel Pressure MULTIPLIER TABLE (Fuel Inj FP Mult Table) -> This is the table value from the Fuel Injector Trim (Fuel Pressure)(Multiplier) table.

Fuel Injector Trim Fuel Pressure OFFSET TABLE (Fuel Inj FP Offset Table) -> This is the table value from the Fuel Injector Trim (Fuel Pressure)(Offset) table.

Fuel Level (Fuel Level) -> Fuel level sensor output voltage.

Fuel Mode (Fuel Mode) -> The current fuel mode -> 1 = homogeneous mode, 2 = stratified mode.

Fuel Pressure Target Main TABLE (Fuel Press Target Table) -> This is the table value from the Fuel Pressure Target Main table (outside of idle) or the Fuel Pressure Target Main (Idle) table (in idle).

Fuel Pump Duty (Fuel Pump Duty) -> Necessary fuel pump duty ratio as determined by the ECU.

Fuel Rail Pressure (Fuel Pressure) -> Fuel rail pressure as determined by the fuel rail pressure sensor.

Fuel Rail Pressure Target (Fuel Pressure Target) -> Fuel rail pressure target as determined by the ECU.

Fuel Temperature (Fuel Temp) -> Fuel temperature based on the fuel temperature sensor.

Fuel Temperature Voltage DIRECT (Fuel Temp Volts Direct) -> Fuel temperature sensor output voltage direct.

Gear Position ESTIMATED (Gear Position) -> Current estimated gear position as determined by the ECU. This value is estimated based on RPM and vehicle speed.

Gear Position ESTIMATED Req Torque (Gear Position RT) -> Current estimated gear position used to determine requested torque table switching. This value is estimated based on RPM and vehicle speed for 6MT cars.

Hot Restart Enrichment (Hot Restart Enr) -> Post-start hot-restart decay enrichment fuel adder (EQ ratio) as determined by the 'Hot-Restart Enrichment...' tables. This value begins decaying after engine start to provide post-start enrichment during hot-restart conditions. Higher values indicate greater enrichment.

Hot Restart Enrichment Initial TABLE (Hot Restart Table) -> This is the final table value as determined by the "Hot-Restart Enrichment Initial..." tables with the Barometric Multiplier map ratio applied.

Idle Airflow Target (Idle Airflow) -> Mass airflow target in idle mode as determined by the ECU. This is used as a more proactive means to determine an idle throttle opening based on an estimated airflow target. Higher values indicate a potentially greater throttle opening.

Idle Control Duty (Idle SCV Duty) -> Idle speed control valve duty cycle as determined by the ECU. This value is primarily manipulated in order to hit an idle RPM target.

Idle Mode Switch (Idle Mode Sw) -> Idle mode status as determined by the ECU. Value is ON (or 1) when idle mode is active. Idle mode is primarily determined by throttle position for drive-by-cable cars and requested torque for drive-by-wire cars.

Idle Speed Error 1 (Idle Speed Error 1) -> Current idle RPM delta calculated as follows: (smoothed RPM - idle speed target).

Idle Speed Error 2 (Idle Speed Error 2) -> Current idle RPM delta calculated as follows: (idle speed target - current RPM).

Idle Speed Target (Idle Spd Target) -> Idle RPM target as determined by the ECU.

Idle Table Mode (Idle Table Mode) -> Idle mode that determines switching between multiple "Idle Speed Targets" tables.

Ignition Switch (Ignition Sw) -> Ignition switch status. Value is ON (or 1) when the ignition switch is on.

Ignition Timing (Ignition Timing) -> Total ignition timing for cylinder #1. This includes all compensations and corrections.

Ignition Timing Comp Intake Temp (Ign Comp IAT) -> Final intake temperature based ignition timing compensation table with activation compensation applied (any max limit if applicable).

Ignition Timing Comp Intake Temp A FINAL (Ign Comp IAT A) -> Final intake temperature based ignition timing compensation "A" table with activation compensation applied.

Ignition Timing Comp Intake Temp FINAL (Ign Comp IAT) -> Final intake temperature based ignition timing compensation table with activation compensation applied (any max limit if applicable).

Ignition Timing Comp Intake Temp Max (Ign Comp IAT Max) -> Final maximum limit for intake temperature based ignition timing compensation.

Ignition Timing Comp Per Gear (Ign Comp Gear) -> Per gear ignition timing compensation.

Ignition Timing Comp Tip in (Ign Comp Tip in) -> Tip-in ignition timing compensation.

Inj 1 Pulse Width (Inj PW) -> Final calculated injector pulse width for cylinder #1, as determined by the ECU.

Inj 1 Pulse Width NO LATENCY (Inj PW No Lat) -> Final calculated injector pulse width for cylinder #1, as determined by the ECU. This monitor does not include injector latency and also has more resolution than the 'With Latency' monitor.

Inj 1 Pulse Width WITH LATENCY (Inj PW with Lat) -> Final calculated injector pulse width for cylinder #1 (including injector latency), as determined by the ECU.

Inj Duty Cycle (Inj Duty Cycle) -> Percentage of current engine cycle time (based on RPM) that the injectors are commanded to be on (based on the commanded injector pulse width).

Inj Latency (Inj Latency) -> Injector latency (dead-time) as determined by the 'Fuel Injector Latency' table.

Inj Pulse Width Final Base (Inj PW Base) -> Final injector pulse width before individual fuel injector trims are applied.

Intake Temperature Manifold (Intake Temp Manifold) -> Intake temperature based on the intake temperature sensor in intake manifold.

Intake Temperature Pre Turbo (Intake Temp) -> Intake temperature based on the intake air temperature sensor in MAF housing (i.e. Pre-Turbo)

Knock Activity Switch (Knock Active Sw) -> Knock activity status as determined by the ECU with input from the knock sensor. Value is ON (or 1) when knock is detected (as perceived by the ECU). Note: Because this switch is immediately cleared when no knock is occurring (as perceived by the ECU), it can be difficult to catch knock events when monitoring. This is because the time scale of a single knock event is small.

Knock Sensor Bkgd Noise Base (KS Bkgd Base) -> This is a smoothed component of the knock sensor corrected noise level that makes up a portion of the background noise calculation.

Knock Sensor Bkgd Noise Final (KS Bkgd Final) -> This is the final background noise level used as a base upon which the knock threshold adder is added to determine a knock threshold level.

Knock Sensor Corr Noise Level (KS Corr Noise) -> Current knock sensor noise level based on the 'Knock Sensor Calibration' table. This value is corrected to normalize output based on the currently selected filter (each filter represents a different frequency range). This corrected value is used as the basis in various calculations to determine knock events and filter selection.

Knock Sensor Filtered Output (KS Filter Output) -> Filtered knock sensor voltage used as an input to the 'Knock Sensor Calibration' table.

Knock Sensor Level Threshold Cylinder 1 (KS Thresh Cyl 1) -> This is the knock sensor noise level threshold for cylinder #1 as determined by the ECU. When the 'Knock Sensor Noise Level Cylinder 1' value exceeds this value, the ECU will determine that a knock event has occurred (when conditions dictate monitoring). Note: Due to the small time scale involved in potential knock events (relative to the logging rate), these monitors may not reflect every instance when the noise level has exceeded the threshold.

Knock Sensor Level Threshold Cylinder 2 (KS Thresh Cyl 2) -> This is the knock sensor noise level threshold for cylinder #2 as determined by the ECU. When the 'Knock Sensor Noise Level Cylinder 2' value exceeds this value, the ECU will determine that a knock event has occurred (when conditions dictate monitoring). Note: Due to the small time scale involved in potential knock events (relative to the logging rate), these monitors may not reflect every instance when the noise level has exceeded the threshold.

Knock Sensor Level Threshold Cylinder 3 (KS Thresh Cyl 3) -> This is the knock sensor noise level threshold for cylinder #3 as determined by the ECU. When the 'Knock Sensor Noise Level Cylinder 3' value exceeds this value, the ECU will determine that a knock event has occurred (when conditions dictate monitoring). Note: Due to the small time scale involved in potential knock events (relative to the logging rate), these monitors may not reflect every instance when the noise level has exceeded the threshold.

Knock Sensor Level Threshold Cylinder 4 (KS Thresh Cyl 4) -> This is the knock sensor noise level threshold for cylinder #4 as determined by the ECU. When the 'Knock Sensor Noise Level Cylinder 4' value exceeds this value, the ECU will determine that a knock event has occurred (when conditions dictate monitoring). Note: Due to the small time scale involved in potential knock events (relative to the logging rate), these monitors may not reflect every instance when the noise level has exceeded the threshold.

Knock Sensor Noise Level Cylinder 1 (KS Noise Cyl 1) -> This is the current modified knock sensor noise level for cylinder #1 as determined by the ECU. When this value exceeds the 'Knock Sensor Level Threshold Cylinder 1' value, the ECU will determine that a knock event has occurred (when conditions dictate monitoring). Note: Due to the small time scale involved in potential knock events (relative to the logging rate), these monitors may not reflect every instance when the noise level has exceeded the threshold.

Knock Sensor Noise Level Cylinder 2 (KS Noise Cyl 2) -> This is the current modified knock sensor noise level for cylinder #2 as determined by the ECU. When this value exceeds the 'Knock Sensor Level Threshold Cylinder 2' value, the ECU will determine that a knock event has occurred (when conditions dictate monitoring). Note: Due to the small time scale involved in potential knock events (relative to the logging rate), these monitors may not reflect every instance when the noise level has exceeded the threshold.

Knock Sensor Noise Level Cylinder 3 (KS Noise Cyl 3) -> This is the current modified knock sensor noise level for cylinder #3 as determined by the ECU. When this value exceeds the 'Knock Sensor Level Threshold Cylinder 3' value, the ECU will determine that a knock event has occurred (when conditions dictate monitoring). Note: Due to the small time scale involved in potential knock events (relative to the logging rate), these monitors may not reflect every instance when the noise level has exceeded the threshold.

Knock Sensor Noise Level Cylinder 4 (KS Noise Cyl 4) -> This is the current modified knock sensor noise level for cylinder #4 as determined by the ECU. When this value exceeds the 'Knock Sensor Level Threshold Cylinder 4' value, the ECU will determine that a knock event has occurred (when conditions dictate monitoring). Note: Due to the small time scale involved in potential knock events (relative to the logging rate), these monitors may not reflect every instance when the noise level has exceeded the threshold.

Knock Sensor Thresh Adder Final (KS Thresh Adder) -> This value is added to the final background noise level to determine the final knock threshold level. This value is also used in the calculation of the filter reference noise level which determines the selection of the current knock filter.

Knock Sensor Thresh Level Final (KS Thresh Level) -> Final knock threshold noise level which is compared to the current knock sensor corrected noise level to determine if a knock event has occurred.

Knock Sum (Knock Sum) -> Counter which is incremented when a non-consecutive knock event, as perceived by the ECU, occurs. This value may be reset to zero when a certain threshold is reached. Note: On some ECUs, this counter may be incremented even at idle and low load/RPM where false knock detection is a greater probability.

Knock Sum Cyl 1 (Knock Sum Cyl 1) -> Counter which is incremented when a non-consecutive knock event, as perceived by the ECU, occurs in cylinder #1. This value may be reset to zero when a certain threshold is reached. Note: This counter is incremented even at idle and low RPM where false knock is a greater probability.

Knock Sum Cyl 2 (Knock Sum Cyl 2) -> Counter which is incremented when a non-consecutive knock event, as perceived by the ECU, occurs in cylinder #2. This value may be reset to zero when a certain threshold is reached. Note: This counter is incremented even at idle and low RPM where false knock is a greater probability.

Knock Sum Cyl 3 (Knock Sum Cyl 3) -> Counter which is incremented when a non-consecutive knock event, as perceived by the ECU, occurs in cylinder #3. This value may be reset to zero when a certain threshold is reached. Note: This counter is incremented even at idle and low RPM where false knock is a greater probability.

Knock Sum Cyl 4 (Knock Sum Cyl 4) -> Counter which is incremented when a non-consecutive knock event, as perceived by the ECU, occurs in cylinder #4. This value may be reset to zero when a certain threshold is reached. Note: This counter is incremented even at idle and low RPM where false knock is a greater probability.

Manifold Abs Pressure (Man Abs Press) -> Manifold pressure (absolute) based on the manifold absolute pressure sensor.

Manifold Abs Pressure Sensor Voltage (Man Abs Press Volts) -> Manifold absolute pressure sensor voltage.

Manifold Rel Pressure (Boost) -> Manifold pressure (relative) calculated from manifold absolute pressure and barometric pressure as follows: manifold absolute pressure - barometric pressure.

Mass Airflow (MAF) -> Final mass airflow (in grams per second), as determined by the ECU, based on the 'MAF Calibration' table with limits/compensations applied.

Mass Airflow Corrected (MAF Corr) -> Final mass airflow (in grams per second), as determined by the ECU, based on the 'MAF Calibration' table with corrections applied.

Mass Airflow Corrected OEM VE (MAF Corr OEM VE) -> Current volumetric efficiency input to the ideal gas law equation used in determining the final corrected mass airflow.

Mass Airflow Corrected VE (MAF VE) -> Current volumetric efficiency input to the ideal gas law equation used in determining the final corrected mass airflow.

Mass Airflow Frequency (MAF Freq) -> Mass airflow sensor output frequency.

Mass Airflow Voltage (MAF Volts) -> Mass airflow sensor output voltage.

Mass Airflow Voltage DIRECT (MAF Volts Direct) -> Mass airflow sensor output voltage direct (higher precision as compared to non-direct monitor).

Neutral Position Switch (Neutral Pos Sw) -> Transmission neutral status as determined by the neutral position sensor. Value is ON (or 1) when gearshift is in neutral for manual transmissions or neutral or park for automatic transmissions.

OCV Duty Exhaust Left (OCV Duty Exh L) -> Commanded Oil Control Valve duty ratio for exhaust camshaft (left).

OCV Duty Exhaust Right (OCV Duty Exh R) -> Commanded Oil Control Valve duty ratio for exhaust camshaft (right).

OCV Duty Intake Left (OCV Duty Int L) -> Commanded Oil Control Valve duty ratio for intake camshaft (left).

OCV Duty Intake Right (OCV Duty Int R) -> Commanded Oil Control Valve duty ratio for intake camshaft (right).

Oil Temperature (Oil Temp) -> Oil temperature based on the oil temperature sensor.

Post Start AVCS Disabled Map Ratio (PS AVCS Disable Ratio) -> Post-start AVCS disabled map ratio multiplier that determines the switching (and blending) between "...Post-Start AVCS Disabled" tables and the corresponding "Main" tables. The final table value is calculated as follows: (AVCS disabled table * map ratio) + (Main table * (1.0 - map ratio)). Note: For some ECUs, the "AVCS disabled table", when active, is a maximum limit applied to the "Main" table.

Post Start Enrich Homogeneous (Post Start H) -> Post-start fuel adder (EQ ratio) in homogeneous fuel mode. This value begins decaying after engine start to provide post-start enrichment. Higher values indicate greater enrichment.

Post Start Enrich Homogeneous Base FAST TABLE (PS H Fast Table) -> This is the table value from the Post-Start Enrichment (Homogeneous) Base (Fast) tables.

Post Start Enrich Homogeneous Base MODERATE TABLE (PS H Mod Table) -> This is the table value from the Post-Start Enrichment (Homogeneous) Base (Moderate) tables.

Post Start Enrich Homogeneous Base SLOW TABLE (PS H Slow Table) -> This is the table value from the Post-Start Enrichment (Homogeneous) Base (Slow) tables.

Post Start Enrich Stratified (Post Start S) -> Post-start fuel adder (EQ ratio) in stratified fuel mode. This value begins decaying after engine start to provide post-start enrichment. Higher values indicate greater enrichment.

Post Start Enrich Stratified Base FAST TABLE (PS S Fast Table) -> This is the table value from the Post-Start Enrichment (Stratified) Base (Fast) tables.

Post Start Enrich Stratified Base MODERATE TABLE (PS S Mod Table) -> This is the table value from the Post-Start Enrichment (Stratified) Base (Moderate) tables.

Post Start Enrich Stratified Base SLOW TABLE (PS S Slow Table) -> This is the table value from the Post-Start Enrichment (Stratified) Base (Slow) tables.

Post Start High Speed Enrich (Post Start HS) -> Post-start high speed decay fuel adder (EQ ratio) as determined by the 'Post-Start Enrichment High Speed...' tables. This value begins decaying after engine start to provide post-start enrichment. Higher values indicate greater enrichment.

Post Start Low Speed Enrich (Post Start LS) -> Post-start low speed decay fuel adder (EQ ratio) as determined by the 'Post-Start Enrichment Low Speed...' tables. This value begins decaying after engine start to provide post-start enrichment. Higher values indicate greater enrichment.

Primary Ignition (Primary Ign) -> Primary ignition timing advance as determined by the 'Primary Ignition' table(s).

Primary Ignition TABLE (Primary Ign Table) -> This is the table value from the Primary Ignition tables (non-idle) before any compensations are applied.

Primary Open Loop Fueling ECT Comp TABLE (Prim OL ECT Table) -> This is the table value from the Primary Open Loop Fueling Compensation (Coolant Temp) table.

Primary Open Loop Fueling TABLE (Prim OL Fuel Table) -> This is the table value from the Primary Open Loop Fueling table before any compensations are applied.

Radiator Fan Relay 1 Switch (Rad Fan 1 Sw) -> Radiator fan relay #1 status as determined by the ECU. Value is ON (or 1) when the ECU determines that the relay should be on.

Radiator Fan Relay 2 Switch (Rad Fan 2 Sw) -> Radiator fan relay #2 status as determined by the ECU. Value is ON (or 1) when the ECU determines that the relay should be on.

Requested Torque (Req Torque) -> Requested torque as determined by the 'Requested Torque' table(s) and used as an input to the 'Target Throttle Angle...' table(s) to determine the target throttle angle.

Requested Torque BOOST TARGETS (Req Torque Bst Targets) -> Requested torque as determined by the 'Requested Torque' table(s) (and with other compensations) and used as an input to the 'Boost Targets' table to determine the boost target.

Requested Torque BOOST TARGETS Adder AC LOAD (Req Torque Bst Targets AC) -> Adder to the the 'Requested Torque (Boost Targets)' value based on A/C compressor load.

Requested Torque BOOST TARGETS Adder ALTERNATOR LOAD (Req Torque Bst Targets ALT) -> Adder to the the 'Requested Torque (Boost Targets)' value based on alternator load.

Requested Torque Delta (Req Torque Delta) -> This is the requested torque delta (current - previous).

Requested Torque Limit TCM FINAL WITH COMPS (Req Tor TCM Final) -> Final applied requested torque limit as determined by the transmission control module (TCM) during normal operation.

Requested Torque Limit TCM OEM BASE (Req Tor TCM Base) -> Base requested torque limit as determined by the transmission control module (TCM) during normal operation. This value is further manipulated by specific compensations to determine a final limit.

Requested Torque Ratio (Req Torq Ratio) -> Requested Torque Ratio as used as an input to the 'Target Throttle Angle...' tables. This value is calculated as follows: requested torque / requested torque ratio base. The requested torque ratio base is determined by the 'Requested Torque (Ratio Base)' table.

Roughness Cyl 1 (Roughness Cyl 1) -> Misfire count for cylinder #1 as determined by the ECU.

Roughness Cyl 2 (Roughness Cyl 2) -> Misfire count for cylinder #2 as determined by the ECU.

Roughness Cyl 3 (Roughness Cyl 3) -> Misfire count for cylinder #3 as determined by the ECU.

Roughness Cyl 4 (Roughness Cyl 4) -> Misfire count for cylinder #4 as determined by the ECU.

SI Drive Mode (SI Drive Mode) -> This is the final SI-DRIVE mode used to determine requested torque table switching as follows: SPORT ('S' or 1), SPORT# ('S#' or 2), INTELLIGENT ('I' or 3)

Target Throttle Angle (Target Throttle) -> Target throttle plate opening position during non-idle conditions. This value is determined by requested torque and RPM.

TGV Drive Switch (TGV Drive Sw) -> Tumble generator valves (TGV) position as determined by the ECU. Value is ON (or 1) when the TGVs are open.

TGV Map Ratio (TGV Map Ratio) -> TGV-based map ratio multiplier that determines the switching (and blending) between the TGVs closed and TGVs open tables. The final table value is calculated as follows: (TGVs open table * map ratio) + (TGVs closed table * (1.0 - map ratio)).

TGV Output Switch (TGV Output Sw) -> Tumble generator valve output status as determined by the ECU. Value is ON (or 1) when ECU intends to change the position of the TGVs.

TGV Voltage Left (TGV Volts Left) -> Tumble generator valve (TGV) output voltage as determined by the TGV position sensor in the left bank.

TGV Voltage Left DIRECT (TGV Volts Left Direct) -> Tumble generator valve (TGV) output voltage direct (higher precision and unfilitered as compared to non-direct monitor) as determined by the TGV position sensor in the left bank.

TGV Voltage Left DIRECT Smoothed (TGV Volts Left Direct Sm) -> Tumble generator valve (TGV) output voltage direct smoothed (higher precision as compared to non-direct monitor) as determined by the TGV position sensor in the left bank.

TGV Voltage Right (TGV Volts Right) -> Tumble generator valve (TGV) output voltage as determined by the TGV position sensor in the right bank.

TGV Voltage Right DIRECT (TGV Volts Right Direct) -> Tumble generator valve (TGV) output voltage direct (higher precision and unfilitered as compared to non-direct monitor) as determined by the TGV position sensor in the right bank.

TGV Voltage Right DIRECT Smoothed (TGV Volts Right Direct Sm) -> Tumble generator valve (TGV) output voltage direct smoothed (higher precision as compared to non-direct monitor) as determined by the TGV position sensor in the right bank.

Throttle Position (Throttle Pos) -> Throttle plate opening percentage based on the throttle position sensor.

Tip in Enrich LAST APPLIED (Tip in Enrich) -> The last applied injector pulse width for tip-in enrichment after all compensations have been applied. Tip-in enrichment temporarily overrides current fueling based on abrupt changes in throttle in a positive direction. Note: This value is not cleared when tip-in enrichment is inactive.

Tip in Enrich LAST CALC (Tip in Enrich) -> The last calculated injector pulse width for tip-in enrichment after all compensations have been applied. Tip-in enrichment temporarily overrides current fueling based on abrupt changes in throttle in a positive direction. Note: This value is not necessarily applied as it is a calculation before thresholds are checked for activation. This value is also not cleared when tip-in enrichment is inactive.

Tip in Enrich TABLE (Tip in Enrich Table) -> This is the table value from the Tip-in Enrichment table before any compensations are applied.

TPS Delta (TPS Delta) -> Change in throttle position, as determined by the ECU. This value is calculated as follows: current throttle position - previous throttle position. Positive values indicate that the throttle has changed in a positive direction.

TPS Duty (TPS Duty) -> Throttle motor duty as determined by the ECU. This value is manipulated in order to hit a throttle target.

TPS Voltage (TPS Volts) -> Throttle position sensor output voltage.

TPS Voltage MAIN (TPS Volts Main) -> Main throttle position sensor output voltage.

TPS Voltage SUB (TPS Volts Sub) -> Sub throttle position sensor output voltage.

Turbo Dynamics Boost Error (TD Boost Error) -> This is the difference between the current boost target and actual boost calculated as follows: boost target - actual boost.

Turbo Dynamics Burst (TD Burst) -> Current correction (absolute) to wastegate duty based on the 'Turbo Dynamics Burst' table. This correction is generally active when boost error immediately swings from positive to negative (or vice versa).

Turbo Dynamics Continuous (TD Continuous) -> Current correction (absolute) to wastegate duty based on the 'Turbo Dynamics Continuous' table. This correction is generally active when boost error is non-zero.

Turbo Dynamics Integral (TD Integral) -> Current total correction (absolute) to wastegate duty based on the 'Turbo Dynamics Integral...' tables. This value accumulates generally over a short period of time based on minimum RPM and boost target thresholds.

Turbo Dynamics Integral WG POSITION CORRECTION (TD Integ WG Pos Corr) -> Current total correction to wastegate position based on the 'Turbo Dynamics Integral' table. This value accumulates generally over a short period of time based on specific conditions.

Turbo Dynamics Proportional (TD Proportional) -> Current correction (absolute) to wastegate duty based on the 'Turbo Dynamics Proportional' table.

Turbo Dynamics Proportional WG POSITION CORRECTION (TD Prop WG Pos Corr) -> Current correction to wastegate position based on the 'Turbo Dynamics Propotional' table.

VDC Ban of Torque Down Switch (VDC Ban Torq Sw) -> Ban of torque-down as determined by the ECU to be transmitted to the Vehicle Dynamics Control (VDC) module.

VDC Req Torque Down Switch (VDC Req Torq Sw) -> Request for torque-down to the ECU as determined by the Vehicle Dynamics Control (VDC) module.

Vehicle Speed (Vehicle Speed) -> Vehicle speed based on the vehicle speed sensor (VSS).

Wall Wetting 1 (Wall Wetting 1) -> This is the group 1 eq ratio adder for the group 1 manifold wall wetting compensation. The final wall wetting compensation is determined as: (group 1 + group 2) * group 4.

Wall Wetting 1 Base (Wall Wetting 1 Base) -> This is the manifold wall wetting compensation for the group 1 Base eq ratio adder which includes the Base Adder with the Load-Based and RPM-Based corrections applied. The final wall wetting compensation is determined as: ((group 1 Base * group 1 Wall) + (group 2 Base * group 2 Wall)) * group 4.

Wall Wetting 1 Wall Temp Correction (Wall Wetting 1 Wall) -> This is the group 1 Wall Temp correction that is applied to the group 1 Base value for the manifold wall wetting compensation. The final wall wetting compensation is determined as: ((group 1 Base * group 1 Wall) + (group 2 Base * group 2 Wall)) * group 4.

Wall Wetting 1A (Wall Wetting 1A) -> This is the group 1A base eq ratio adder for the group 1 manifold wall wetting compensation. The final wall wetting compensation is determined as: ((1A*1B*1C)+(2A*2B*2C)+(3A*3B*3C))*4.

Wall Wetting 1B (Wall Wetting 1B) -> This is the group 1B multiplier for the group 1 manifold wall wetting compensation. The final wall wetting compensation is determined as: ((1A*1B*1C)+(2A*2B*2C)+(3A*3B*3C))*4.

Wall Wetting 1C (Wall Wetting 1C) -> This is the group 1C multiplier for the group 1 manifold wall wetting compensation. The final wall wetting compensation is determined as: ((1A*1B*1C)+(2A*2B*2C)+(3A*3B*3C))*4.

Wall Wetting 2 (Wall Wetting 2) -> This is the group 2 eq ratio adder for the group 2 manifold wall wetting compensation. The final wall wetting compensation is determined as: (group 1 + group 2) * group 4.

Wall Wetting 2 Base (Wall Wetting 2 Base) -> This is the manifold wall wetting compensation for the group 2 Base eq ratio adder which includes the Base Adder with the RPM-Based corrections applied. The final wall wetting compensation is determined as: ((group 1 Base * group 1 Wall) + (group 2 Base * group 2 Wall)) * group 4.

Wall Wetting 2 Wall Temp Correction (Wall Wetting 2 Wall) -> This is the group 2 Wall Temp correction that is applied to the group 2 Base value for the manifold wall wetting compensation. The final wall wetting compensation is determined as: ((group 1 Base * group 1 Wall) + (group 2 Base * group 2 Wall)) * group 4.

Wall Wetting 2A (Wall Wetting 2A) -> This is the group 2A base eq ratio adder for the group 2 manifold wall wetting compensation. The final wall wetting compensation is determined as: ((1A*1B*1C)+(2A*2B*2C)+(3A*3B*3C))*4.

Wall Wetting 2B (Wall Wetting 2B) -> This is the group 2B multiplier for the group 2 manifold wall wetting compensation. The final wall wetting compensation is determined as: ((1A*1B*1C)+(2A*2B*2C)+(3A*3B*3C))*4.

Wall Wetting 2C (Wall Wetting 2C) -> This is the group 2C multiplier for the group 2 manifold wall wetting compensation. The final wall wetting compensation is determined as: ((1A*1B*1C)+(2A*2B*2C)+(3A*3B*3C))*4.

Wall Wetting 3A (Wall Wetting 3A) -> This is the group 3A base eq ratio adder for the group 3 manifold wall wetting compensation. The final wall wetting compensation is determined as: ((1A*1B*1C)+(2A*2B*2C)+(3A*3B*3C))*4.

Wall Wetting 3B (Wall Wetting 3B) -> This is the group 3B multiplier for the group 3 manifold wall wetting compensation. The final wall wetting compensation is determined as: ((1A*1B*1C)+(2A*2B*2C)+(3A*3B*3C))*4.

Wall Wetting 3C (Wall Wetting 3C) -> This is the group 3C multiplier for the group 3 manifold wall wetting compensation. The final wall wetting compensation is determined as: ((1A*1B*1C)+(2A*2B*2C)+(3A*3B*3C))*4.

Wall Wetting 4 (Wall Wetting 4) -> This is the group 4 multiplier for the manifold wall wetting compensation. The final wall wetting compensation is determined as: ((1A*1B*1C)+(2A*2B*2C)+(3A*3B*3C))*4.

Wall Wetting Final (Wall Wetting Final) -> This is the final applied manifold wall wetting compensation (eq ratio adder) to the Commanded Fuel Final.

Warm Up Enrichment (Warm up Enrich) -> Warm-up enrichment fuel adder (EQ ratio) as determined by the 'Warm-up Enrichment...' table(s). This adder provides warm-up enrichment based on coolant temperature. Higher values indicate greater enrichment.

Warm Up Enrichment Homogeneous (Warm up Enrich H) -> Warm-up enrichment fuel adder (EQ ratio) in homogeneous fuel mode. This adder provides warm-up enrichment based on coolant temperature. Higher values indicate greater enrichment.

Warm Up Enrichment Stratified (Warm up Enrich S) -> Warm-up enrichment fuel adder (EQ ratio) in stratified fuel mode. This adder provides warm-up enrichment based on coolant temperature. Higher values indicate greater enrichment.

Warm up Mode (Warm up Mode) -> Warm-up mode that determines switching between the "Fuel Pressure Target" tables and other functions in the ECU.

Wastegate Duty (Wastegate Duty) -> Final wastegate duty cycle as determined by the ECU's boost control logic. This value is manipulated in order to hit the boost target.

Wastegate Duty Cycles High TABLE (Wastegate High Table) -> This is the table value from the Wastegate Duty Cycles (High) table before any compensations are applied.

Wastegate Duty Cycles Low TABLE (Wastegate Low Table) -> This is the table value from the Wastegate Duty Cycles (Low) table before any compensations are applied.

Wastegate Duty Max (Wastegate Max) -> Maximum wastegate duty limit as determined by the 'Wastegate Duty Cycles (High)' table(s) with all wastegate compensations and limits applied.

Wastegate Initial Position FINAL (Wastegate Init Pos Final) -> This is the final wastegate initial position from the Wastegate Initial Position table with all wastegate compensations and limits applied.

Wastegate Initial Position TABLE (Wastegate Init Pos Table) -> This is the table value from the Wastegate Initial Position table before any compensations are applied.

Wastegate Position Actual (Wastegate Pos Actual) -> This is the actual wastegate position as determined by the wastegate valve.

Wastegate Position Commanded (Wastegate Pos Comm) -> This is the commanded wastegate position BEFORE the learned correction and/or ramping is applied.

Wastegate Position Commanded Final (Wastegate Pos Comm Final) -> This is the final commanded wastegate position with learned correction and/or ramping applied.

Wastegate Position Learned Correction (Wastegate Pos Learn Corr) -> This is a learned correction (based on fully closed wastegate states) that is applied to the commanded wastegate position to determine the final commanded wastegate position.

WWC 1 Load Delta (WWC 1 Load Delta) -> Caclulated load delta determined as: (current load - previous load) as used in wall-wetting compensation group 1 logic.

WWC 1 MAP Delta (WWC 1 MAP Delta) -> Manifold absolute pressure (MAP) delta determined as: (current MAP - previous MAP) as used in wall-wetting compensation group 1 logic.

