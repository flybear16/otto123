# OTTO 机器人扩展方案调研报告

> 调研时间：2026-04-12
> 涵盖范围：3D 打印配件、舵机升级、屏幕扩展、摄像头模块

***

## 一、3D 打印扩展

### 1.1 官方核心部件

OTTO 机器人 3D 打印部件主要来自 **Open-Hardware-Leaders/OttoDIY** GitHub 仓库：

| 部件 | 文件名                    | 许可证           |
| -- | ---------------------- | ------------- |
| 头部 | OttoDIY+\_head\_V9.stl | CERN OHL v2.0 |
| 身体 | OttoDIY+\_body\_V9.stl | CERN OHL v2.0 |
| 腿部 | OttoDIY+\_Leg\_V9.stl  | CERN OHL v2.0 |
| 脚部 | OttoDIY+\_foot\_V9.stl | CERN OHL v2.0 |

* **GitHub**: <https://github.com/Open-Hardware-Leaders/OttoDIY>
* **许可证**: 软件 GNU GPL v3.0 / 硬件 CERN OHL v2.0 / 文档 CC-BY-SA 4.0

### 1.2 功能性扩展配件

| 配件                       | 来源                   | 用途     |
| ------------------------ | -------------------- | ------ |
| Otto Gripper (夹爪)        | Printables HP Robots | 抓取小物体  |
| Otto Pen Adapter (画笔适配器) | Printables           | 绘画/写字  |
| OTTO Ninja 衍生款           | oshwhub / TuyaOpen   | 忍者主题外观 |

* **Otto Gripper**: <https://www.printables.com/model/1603958-hp-robots-otto-gripper>
* **Otto Pen Adapter**: <https://www.printables.com/model/1642077-ottos-pen-adapter>
* **OTTO Ninja**: <https://oshwhub.com/robben.wang/ottorobot_ninja>

### 1.3 外观/Cosplay 配件

| 配件              | 来源                   |
| --------------- | -------------------- |
| OTTO 头部 LEGO 风格 | Cults3D              |
| 头盔/帽子类配件        | Thingiverse 社区 remix |
| 装饰性外壳           | 各社区衍生设计              |

* **Thingiverse OTTO DIY**: <https://www.thingiverse.com/thing:1568652>
* **Cults3D OTTO Head LEGO**: <https://cults3d.com/en/3d-model/art/otto-head-lego/similar-designs>

***

## 二、舵机升级方案

### 2.1 标准配置 vs 升级选项

OTTO 标准使用 **SG90 9g 微型舵机**，社区常见升级方案：

| 型号             | 力矩 (4.8V)                 | 重量     | 电压       | 价格参考   | 兼容性        |
| -------------- | ------------------------- | ------ | -------- | ------ | ---------- |
| **SG90** (标准)  | 1.8 kg-cm                 | 9g     | 4.8-6V   | ¥5-10  | 原装兼容       |
| **MG90S** (推荐) | 1.8 kg-cm / 2.2 kg-cm @6V | 13-18g | 4.8-6.6V | ¥15-25 | 尺寸相近，直接替换  |
| **MG996R**     | 9.4 kg-cm / 11 kg-cm @6V  | 55g    | 4.8-7.2V | ¥20-35 | 更大更重，需强化安装 |

### 2.2 升级建议

**推荐方案 A: SG90 → MG90S**

* 金属齿轮更耐用
* 尺寸与 SG90 相近，无需大幅改动
* OTTO+ 套件已采用 MG90S

**推荐方案 B: SG90 → MG996R**

* 仅在需要大力矩时使用 (如负重、复杂地形)
* 重量增加 55g，需确认结构强度
* 需独立供电，避免舵机电流影响主控

### 2.3 接线与控制

* **控制接口**: 标准 RC PWM (50Hz, 0.5-2.5ms 脉宽)
* **OTTO 库**: OttoDIYLib (GitHub)
* **Arduino 接口**: `#include <Servo.h>` + 4 个舵机引脚 (LeftLeg, RightLeg, LeftFoot, RightFoot)
* **扩展线缆**: 常见 200mm 舵机延长线
* **供电建议**: 4x AA 电池盒或独立 5-6V 供电

### 2.4 关键参考

* OTTO 标准配置：<https://projecthub.arduino.cc/sriharshamallavarapu/otto-robot-7656af>
* OTTO 库 (4 舵机布局): <https://github.com/OttoDIY/OttoDIYLib>
* MG90S 规格：<https://www.hobbyking.com/en_us/turnigytm-mg90s-ds-mg-servo-1-8kg-0-10sec-18g.html>
* MG996R 规格：<https://www.handsontec.com/dataspecs/motor_fan/MG996R.pdf>

***

## 三、屏幕扩展

### 3.1 推荐屏幕型号

| 型号                       | 分辨率     | 接口  | I2C 地址 | 库支持                      |
| ------------------------ | ------- | --- | ------ | ------------------------ |
| **0.96" OLED (SSD1306)** | 128x64  | I2C | 0x3C   | U8g2 / Adafruit\_SSD1306 |
| **1.3" OLED (SH1106)**   | 128x64  | I2C | 0x3C   | U8g2 / Adafruit\_SH1106  |
| **1.44" TFT**            | 128x128 | SPI | -      | TFT\_eSPI                |

### 3.2 ESP32 I2C 引脚

* 默认 SDA = GPIO21, SCL = GPIO22
* 实际可配置任意 GPIO
* 文档：<https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/peripherals/i2c.html>

### 3.3 库推荐

| 库                     | 用途                       |
| --------------------- | ------------------------ |
| **U8g2**              | OLED (SSD1306/SH1106) 通用 |
| **Adafruit\_SSD1306** | SSD1306 I2C 专用           |
| **TFT\_eSPI**         | TFT 彩色屏幕                 |

* U8g2 示例 (OTTO Ninja): <https://github.com/OttoDIY/OttoNinja>

### 3.4 3D 打印安装方案

OTTO 头部有标准 STL 文件可作为屏幕安装基础：

* <https://github.com/Open-Hardware-Leaders/OttoDIY> (3Dprint 文件夹)

### 3.5 面部表情实现

OTTO 通过 `putMouth()` API 显示表情图案，图案定义在 `Otto_mouths.h`:

* <https://github.com/stembotvn/OttoDIY_Vbot/blob/master/Otto_mouths.h>

***

## 四、摄像头模块

### 4.1 推荐摄像头

| 模块                         | 传感器    | 分辨率   | 接口      | 功耗        | 参考价    |
| -------------------------- | ------ | ----- | ------- | --------- | ------ |
| **ESP32-CAM (AI-Thinker)** | OV2640 | 2MP   | ESP32 内置 | 160-310mA | ¥25-40 |
| OV5640                     | 5MP    | ESP32 | 可选      | 更高        | -      |

* **ESP32-CAM 官方仓库**: <https://github.com/espressif/esp32-camera>

### 4.2 应用场景

| 场景   | 库/框架                                                  |
| ---- | ----------------------------------------------------- |
| 人脸识别 | ESP-WHO (<https://github.com/espressif/esp-who>)      |
| 视频流  | CameraWebServer / MJPEG streaming                     |
| 物体检测 | ESP-DL (<https://github.com/espressif/esp-detection>) |
| 巡线   | OpenMV / TensorFlow Lite                              |

### 4.3 功耗注意

* 工作电流：160-310mA (取决于配置)
* 深度睡眠：\~6mA
* 建议：移动 OTTO 使用低分辨率 (QVGA) 节省电力
* 供电：需独立 5V 供电，避免 USB 供电不足

### 4.4 OTTO 集成参考

* OTTO DIY ESP32: <https://github.com/rhansenne/OttoDIY_ESP32>
* OTTO micro-ROS (ROS2 可视化): <https://github.com/FyrbyAdditive/Otto-microROS>
* OTTO Xiaozhi AI 版本：<https://ottodiy.tech/en/docs/downloads/>

***

## 五、扩展接口与供电

### 5.1 I2C 扩展

OTTO 预留 I2C 接口，可连接：

* OLED 屏幕
* 超声波传感器 (HC-SR04)
* I2C 光传感器
* I2C 陀螺仪 (MPU6050)

### 5.2 供电方案

| 方案         | 适用场景    | 容量      |
| ---------- | ------- | ------- |
| 4x AA 电池盒  | 基础 OTTO | 4.8-6V  |
| 18650 锂电池盒 | 增强续航    | 3.7V x2 |
| USB 5V 供电  | 有线调试    | 5V/1A+  |

### 5.3 通信扩展

| 模块               | 用途        |
| ---------------- | --------- |
| ESP32 内置 WiFi/BT | 无线控制、OTA  |
| HC-05/06 蓝牙模块    | 经典蓝牙串口    |
| NRF24L01         | 2.4G 无线通信 |

***

## 六、采购参考

### 核心配件 BOM

| 配件                 | 数量 | 参考价      | 链接         |
| ------------------ | -- | -------- | ---------- |
| ESP32-CAM (OV2640) | 1  | ¥25-40   | 各电商平台      |
| 0.96" OLED I2C     | 1  | ¥8-15    | 各电商平台      |
| MG90S 金属齿轮舵机       | 4  | ¥15-20/个 | 各电商平台      |
| 200mm 舵机延长线        | 4  | ¥2-5/条   | 各电商平台      |
| 5V/2A 电源模块         | 1  | ¥10-15   | 各电商平台      |
| OTTO 3D 打印件        | 1 套 | 自打印或采购   | GitHub STL |

***

## 七、扩展方向建议

### 优先级排序

1. **MG90S 舵机升级** (高优先级)
   * 金属齿轮更耐用，提升行走稳定性
   * 替换简单，性价比高

2. **0.96" OLED 表情屏幕** (高优先级)
   * 扩展 OTTO 表达能力
   * 接线和库支持成熟

3. **ESP32-CAM 视觉模块** (中优先级)
   * 人脸识别/视频流功能
   * 需注意功耗和供电

4. **3D 打印功能配件** (低优先级)
   * 夹爪、传感器支架等
   * 根据具体需求添加

***

## 八、参考链接汇总

### GitHub 仓库

* OTTO 官方：<https://github.com/Open-Hardware-Leaders/OttoDIY>
* OTTO 库：<https://github.com/OttoDIY/OttoDIYLib>
* OTTO ESP32: <https://github.com/rhansenne/OttoDIY_ESP32>
* OTTO Ninja: <https://github.com/OttoDIY/OttoNinja>

### 硬件规格

* SG90 规格：<https://handsontec.com/dataspecs/motor_fan/SG90-Servo.pdf>
* MG90S 规格：<https://www.hobbyking.com/en_us/turnigytm-mg90s-ds-mg-servo-1-8kg-0-10sec-18g.html>
* MG996R 规格：<https://www.handsontec.com/dataspecs/motor_fan/MG996R.pdf>
* ESP32-CAM: <https://github.com/espressif/esp32-camera>

### 社区资源

* ESP-WHO (人脸识别): <https://github.com/espressif/esp-who>
* ESP-DL (物体检测): <https://github.com/espressif/esp-detection>
* U8g2 库：<https://github.com/olikraus/u8g2>
* TFT\_eSPI 库：<https://github.com/Bodmer/TFT_eSPI>
