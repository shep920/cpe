#include "lab1_pkg/cpp_header.hpp"

class MyCustomNode : public rclcpp::Node
{
public:
    MyCustomNode() : Node("my_node") {
        RCLCPP_INFO(this->get_logger(), "TEST Cpp node");
    }

private:
};
