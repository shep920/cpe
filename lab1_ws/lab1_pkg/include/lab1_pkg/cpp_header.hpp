#ifndef LAB1_PKG_CPP_HEADER_HPP
#define LAB1_PKG_CPP_HEADER_HPP

#include "rclcpp/rclcpp.hpp"

class MyCustomNode : public rclcpp::Node
{
public:
    MyCustomNode() : Node("my_node") {
        RCLCPP_INFO(this->get_logger(), "TEST Cpp node");
    }

private:
};

#endif // LAB1_PKG_CPP_HEADER_HPP
