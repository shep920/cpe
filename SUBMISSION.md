
# Lab 1: Intro to ROS 2 - Written Questions

### Q1: During this assignment, you've probably ran these two following commands at some point: source /opt/ros/foxy/setup.bash and source install/local_setup.bash. Functionally what is the difference between the two?

**Answer:**  
`/opt/ros/foxy/setup.bash` sets up the ROS 2 environment globally, while `install/local_setup.bash` sets it up for your local workspace.

---

### Q2: What does the queue_size argument control when creating a subscriber or a publisher? How does different queue_size affect how messages are handled?

**Answer:**  
`queue_size` controls how many messages can be buffered. A smaller size may drop messages if not processed fast enough, while a larger size allows more buffering but uses more memory.

---

### Q3: Do you have to call colcon build again after you've changed a launch file in your package?

**Answer:**  
**Yes**, you need to call `colcon build` after changing the `launch.py` file for the changes to take effect.
