
# lab1_pkg

This ROS 2 package supports both Python and C++ nodes. The package includes:
- A `talker` node that listens to two ROS parameters (`v` and `d`) and publishes `AckermannDriveStamped` messages.
- A `relay` node that subscribes to the `drive` topic, modifies the values, and publishes them to the `drive_relay` topic.

## Prerequisites

- ROS 2 (Foxy or later)
- `ackermann_msgs` dependency
- Python 3.x
- C++17 or later

## Installation

1. **Clone the Repository**:
   Clone this package into your ROS 2 workspace `src` folder:
   ```bash
   cd ~/lab1_ws/src
   git clone <your-repo-url> lab1_pkg
   ```

2. **Install Dependencies**:
   Use `rosdep` to install all required dependencies:
   ```bash
   cd ~/lab1_ws
   rosdep install --from-paths src --ignore-src -r -y
   ```

3. **Build the Package**:
   Build the workspace with both Python and C++ nodes:
   ```bash
   colcon build
   ```

4. **Source the Workspace**:
   Source your workspace so ROS 2 can find your package:
   ```bash
   source install/setup.bash
   ```

## Running the Nodes

### Running the `talker` Node (Python)

The `talker` node listens for two parameters (`v` and `d`) and publishes an `AckermannDriveStamped` message with the speed and steering angle values to the `drive` topic.

You can run the `talker` node and set parameters via the command line:

```bash
ros2 run lab1_pkg talker --ros-args -p v:=2.0 -p d:=0.5
```

### Running the `relay` Node (Python or C++)

The `relay` node subscribes to the `drive` topic, multiplies the speed and steering angle by 3, and publishes the result to the `drive_relay` topic.

#### Running the Python Relay Node:
```bash
ros2 run lab1_pkg relay_py
```

#### Running the C++ Relay Node:
```bash
ros2 run lab1_pkg relay_cpp
```

## Testing the Communication

1. **List ROS Topics**:
   Check if the topics are active:
   ```bash
   ros2 topic list
   ```

2. **Echo Messages on the `drive` Topic**:
   Verify messages published by the `talker` node:
   ```bash
   ros2 topic echo /drive
   ```

3. **Echo Messages on the `drive_relay` Topic**:
   Verify messages published by the `relay` node:
   ```bash
   ros2 topic echo /drive_relay
   ```

## Folder Structure

```
lab1_pkg/
  ├── CMakeLists.txt
  ├── package.xml
  ├── setup.py
  ├── src/
  │   ├── talker.py  # Python talker node
  │   ├── relay.py   # Python relay node
  │   └── relay.cpp  # C++ relay node
  └── include/
      └── lab1_pkg/  # C++ header files if needed
```

## Acknowledgments

This package was created as part of a ROS 2 lab exercise to demonstrate publisher-subscriber communication using both Python and C++.
