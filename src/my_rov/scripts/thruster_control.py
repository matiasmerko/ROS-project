#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Wrench
from geometry_msgs.msg import Vector3
from my_rov.srv import ForceTorqueToThrust, ForceTorqueToThrustRequest, ForceTorqueToThrustResponse


def main():
    
    wrench=Wrench()

    rospy.init_node("wrench_control_node")
    pub = rospy.Publisher("/rexrov/thruster_manager/input", Wrench, queue_size=10)
    def callback(req):
        res=ForceTorqueToThrustResponse()
        wrench.force=req.force
        wrench.torque=req.torque
        res.result=True
        return res
    service = rospy.Service("force_torque_to_thrust", ForceTorqueToThrust, callback)
    rospy.loginfo("service started")

    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(wrench)

        rate.sleep()
        

if __name__=='__main__':
    main()