YAGSL Configuration Files
=========================

Now that you have the initial sample code, we need to configure the YAGSL library to work with your robot. The configuration files are located in the `src/main/deploy` directory of your project.

Let's copy last years configs and verify the map to our robot. The configs are located in the `src/main/deploy` directory of your project. You can copy the configs from last years project and paste them into your current project.

To create hand-written JSON configuration files matching the **2026 YAGSL schema standards**, your students will need to populate a total of **7 JSON files** manually:

```text
src/main/deploy/swerve/base/
├── swervedrive.json
└── modules/
    ├── physicalproperties.json
    ├── pidfproperties.json
    ├── frontleft.json
    ├── frontright.json
    ├── backleft.json
    └── backright.json

```

Below is the structured data worksheet for students to fill out by hand, followed by the complete 2026 template structure for each JSON file.

---

# 📝 Hand-Configuration Student Data Sheet (2026 Standard)

### 1. General Robot & Gyro Information

* **CAN Bus Notation (2026 Standard):** Use `""` for main bus (`can_s0`), `"1"` for `can_s1`, or exact CANivore name for CTRE.

| Setting | Value / Selection |
| --- | --- |
| **Gyro Type** | `pigeon2`, `navx_can`, `canandgyro_can`, `imu` *(built-in SystemCore)* |
| **Gyro CAN ID** | ________ |
| **Gyro CAN Bus** | `""` *(default `can_s0`)* |

---

### 2. Module Physical Constants (`physicalproperties.json`)

| Parameter | Measured / Hardware Spec Value |
| --- | --- |
| **Drive Gear Ratio** | ____ : 1 *(e.g., L2 MK4i = 6.75)* |
| **Angle Gear Ratio** | ____ : 1 *(e.g., L2 MK4i = 21.42857)* |
| **Wheel Diameter (inches)** | ____ in *(e.g., 4.0)* |
| **Current Limits (Amps)** | Stator Drive: `40`A | Stator Angle: `20`A |

---

### 3. Module Physical Coordinates (`swervedrive.json`)

*Measure in inches from the **exact physical center of the robot** to the center of each swerve wheel.*

* **+X** = Front, **-X** = Back
* **+Y** = Left, **-Y** = Right

| Module | X Position (Front / Back) | Y Position (Left / Right) |
| --- | --- | --- |
| **Front Left (FL)** | `+` __________ in | `+` __________ in |
| **Front Right (FR)** | `+` __________ in | `-` __________ in |
| **Back Left (BL)** | `-` __________ in | `+` __________ in |
| **Back Right (BR)** | `-` __________ in | `-` __________ in |

---

### 4. Device CAN ID Mapping Table

| Module | Device | Type String (2026 Standard) | CAN ID / Channel | CAN Bus |
| --- | --- | --- | --- | --- |
| **FL** | Drive Motor | e.g. `sparkmax_neo`, `talonfx_kraken` |  |  |
|  | Angle Motor | e.g. `sparkmax_neo`, `talonfx_kraken` |  |  |
|  | Encoder | e.g. `cancoder_can`, `dutycycle_dio` |  |  |
| **FR** | Drive Motor |  |  |  |
|  | Angle Motor |  |  |  |
|  | Encoder |  |  |  |
| **BL** | Drive Motor |  |  |  |
|  | Angle Motor |  |  |  |
|  | Encoder |  |  |  |
| **BR** | Drive Motor |  |  |  |
|  | Angle Motor |  |  |  |
|  | Encoder |  |  |  |

---

# 📄 2026 Standard JSON Configuration Templates

Have your students write or edit these exact 2026 schema layouts in `src/main/deploy/swerve/base/`:

### 1. `swervedrive.json`

*(Located at: `src/main/deploy/swerve/base/swervedrive.json`)*

```json
{
  "gyro": {
    "type": "pigeon2",
    "id": 13,
    "canbus": ""
  },
  "gyroInvert": false,
  "gyroAxis": "yaw",
  "modules": [
    "frontleft.json",
    "frontright.json",
    "backleft.json",
    "backright.json"
  ]
}

```

---

### 2. `modules/physicalproperties.json`

*(Located at: `src/main/deploy/swerve/base/modules/physicalproperties.json`)*

```json
{
  "gearing": {
    "drive": {
      "gearRatio": 6.75,
      "diameter": 4.0
    },
    "angle": {
      "gearRatio": 21.42857
    }
  },
  "statorCurrentLimit": {
    "drive": 40,
    "angle": 20
  }
}

```

---

### 3. `modules/pidfproperties.json`

*(Located at: `src/main/deploy/swerve/base/modules/pidfproperties.json`)*

```json
{
  "drive": {
    "p": 0.01,
    "i": 0.0,
    "d": 0.0,
    "f": 0.0,
    "s": 0.0,
    "v": 0.0,
    "a": 0.0
  },
  "angle": {
    "p": 0.005,
    "i": 0.0,
    "d": 0.0,
    "f": 0.0,
    "s": 0.0,
    "v": 0.0,
    "a": 0.0
  }
}

```

---

### 4. Individual Module File Template (e.g. `modules/frontleft.json`)

*(Create 4 files: `frontleft.json`, `frontright.json`, `backleft.json`, `backright.json`)*

```json
{
  "location": {
    "x": 12.5,
    "y": 12.5
  },
  "drive": {
    "type": "sparkmax_neo",
    "id": 1,
    "canbus": ""
  },
  "angle": {
    "type": "sparkmax_neo",
    "id": 2,
    "canbus": ""
  },
  "absoluteEncoder": {
    "type": "cancoder_can",
    "id": 3,
    "canbus": ""
  },
  "inverted": {
    "drive": false,
    "angle": false
  },
  "absoluteEncoderInverted": false,
  "absoluteEncoderOffset": 0.0
}

```

---

## ⚠️ Key 2026 Schema Hand-Writing Rules for Students

---

## 🛠️ Student Workflow Instructions

1. **Step 1: Inspect Physical Hardware:** Complete the printed/physical data collection sheet.
Have students measure the module X/Y distances from the center of the frame and record all CAN IDs using vendor client utilities (REV Hardware Client / CTRE Phoenix Tuner).


2. **Step 2: Write JSON Configurations by Hand:** Write files in src/main/deploy/swerve/base/.
Students create the directory structure in VS Code and populate the 7 files using the template structures provided above.


3. **Step 3: Measure Encoder Offsets:** Align bevel gears facing LEFT.
Manually align all swerve wheels straight forward with bevel gears facing to the left. Read the raw angle values off AdvantageScope or SmartDashboard/Elastic and write the offset value into absoluteEncoderOffset for each module.


---
