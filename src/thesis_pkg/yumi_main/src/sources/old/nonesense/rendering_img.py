#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the MIT License license.

"""
Finally I got in xyz coordinates according to ROS
"""


import sys
sys.path.insert(0, '/home/sinchiguano/yumi_depends_ws/src/yumi_main/scripts/project')
from thesis_library import *



euler_angles_=[0,0,0]
position_=[0.0,0.0,0.0]

##convert a rot and trans matrix to a 4x4 matrix
def data_to_transform(r_matrix,t_position):
    mat =np.hstack((r_matrix,t_position))
    mat=np.vstack((mat,[0.0,0.0,0.0,1.0]))
    return mat

#convert a 4x4 matrix to a Pose message
def transform_to_pose(mat):
    pose = Pose()
    pose.position.x = mat[0,3]
    pose.position.y = mat[1,3]
    pose.position.z = mat[2,3]
    quat = tf.transformations.quaternion_from_matrix(mat)
    pose.orientation.x = quat[0]
    pose.orientation.y = quat[1]
    pose.orientation.z = quat[2]
    pose.orientation.w = quat[3]
    return pose

def pose_camera_callback(msg):

    global euler_angles_
    global position_

    position_=[msg.position.x,msg.position.y,msg.position.z]
    quaternion_=msg.orientation

    quaternion_tmp=[quaternion_.x,quaternion_.y,quaternion_.z,quaternion_.w]
    roll_, pitch_, yaw_=tf.transformations.euler_from_quaternion(quaternion_tmp)
    euler_angles_=[roll_,pitch_,yaw_]

def publish_transforms(br):

    global euler_angles_
    global position_


    t0 = geometry_msgs.msg.TransformStamped()
    t0.header.stamp = rospy.Time.now()
    t0.header.frame_id = "world"
    t0.child_frame_id = "panda_link0"
    t0.transform.translation.x = 0.0
    t0.transform.translation.y = 0.0
    t0.transform.translation.z = 0.0

    tmp_rot=np.array([[1,0, 0], [0, 1, 0],[0, 0, 1]])
    tmp_trans=np.array([[0.30],[0],[0] ])
    myrot =np.hstack((tmp_rot,tmp_trans))
    myrot=np.vstack((myrot,[0.0,0.0,0.0,1.0]))
    #print('my rotation: \n {}'.format(myrot) )

    q0 = tf.transformations.quaternion_from_matrix(myrot)
    t0.transform.rotation.x = q0[0]
    t0.transform.rotation.y = q0[1]
    t0.transform.rotation.z = q0[2]
    t0.transform.rotation.w = q0[3]
    br.sendTransform(t0)


    # t1 = geometry_msgs.msg.TransformStamped()
    # t1.header.stamp = rospy.Time.now()
    # t1.header.frame_id = "target"
    # t1.child_frame_id = "object"
    # t1.transform.translation.x = 0.12
    # t1.transform.translation.y = 0.12
    # t1.transform.translation.z = 0.0

    # q1 = tf.transformations.quaternion_from_euler(0, 0, 0)
    # t1.transform.rotation.x = q1[0]
    # t1.transform.rotation.y = q1[1]
    # t1.transform.rotation.z = q1[2]
    # t1.transform.rotation.w = q1[3]
    # br.sendTransform(t1)

    t1 = geometry_msgs.msg.TransformStamped()
    t1.header.stamp = rospy.Time.now()
    t1.header.frame_id = "world"
    t1.child_frame_id = "target"
    t1.transform.translation.x = 0.50
    t1.transform.translation.y = 0.0
    t1.transform.translation.z = 0.0

    # tmp_rot=np.array([[0, 1, 0], [1, 0, 0],[0, 0, -1]])
    # tmp_trans=np.array([[0.30],[0],[0] ])
    # myrot =np.hstack((tmp_rot,tmp_trans))
    # myrot=np.vstack((myrot,[0.0,0.0,0.0,1.0]))
    #print('my rotation: \n {}'.format(myrot) )

    #q1 = tf.transformations.quaternion_from_matrix(myrot)
    q1 = tf.transformations.quaternion_from_euler(0, 0, 0)
    t1.transform.rotation.x = q1[0]
    t1.transform.rotation.y = q1[1]
    t1.transform.rotation.z = q1[2]
    t1.transform.rotation.w = q1[3]
    br.sendTransform(t1)

    t2 = geometry_msgs.msg.TransformStamped()
    t2.header.stamp = rospy.Time.now()
    t2.header.frame_id = "target"
    t2.child_frame_id = "camera_link"
    t2.transform.translation.x = 1.0*position_[0]
    t2.transform.translation.y = 1.0*position_[1]
    t2.transform.translation.z = 0.80*position_[2]
    #orientation according to openCV
    q3 = tf.transformations.quaternion_from_euler(euler_angles_[0],euler_angles_[1],euler_angles_[2])
    #orientation of camera link. which is parallel to world frame
    q2 = tf.transformations.quaternion_from_euler(math.pi/2,-math.pi/2,0)
    #correction of camera frame according to openCV orientation
    q4=quaternion_multiply(q3,q2)#rotation,origin
    t2.transform.rotation.x = q4[0]
    t2.transform.rotation.y = q4[1]
    t2.transform.rotation.z = q4[2]
    t2.transform.rotation.w = q4[3]
    br.sendTransform(t2)

def print_information(rotation_vector,translation_vector,rvec_matrix):


    global euler_angles
    print("\n\nThe world coordinate systems origin in-->> camera's coordinate system:")
    print("===rotation_vector:")
    print(rotation_vector)
    print("===rotation_matrix:")
    print(rvec_matrix)
    print("===translation_vector:")
    print(translation_vector)

    matr =np.hstack((rvec_matrix,translation_vector))
    matr=np.vstack((matr,[0.0,0.0,0.0,1.0]))

    quat_tmp = tf.transformations.quaternion_from_matrix(matr)
    roll_, pitch_, yaw_=tf.transformations.euler_from_quaternion(quat_tmp)
    euler_angles_tmp=[roll_,pitch_,yaw_]
    print("euler_angles_tmp: ",euler_angles_tmp)
    import math
    print(roll_* 180 / math.pi,pitch_* 180 / math.pi,yaw_* 180 / math.pi)

    print("\n\nThe camera origin in -->>world coordinate system:")
    print("===camera rvec_matrix:")
    print(rvec_matrix.T)
    print("===camera translation_vector:")
    print(-np.dot(rvec_matrix.T, translation_vector))
    print('euler_angles inv roll_,pitch_,yaw:  \n',euler_angles_)
    print(euler_angles_[0]* 180 / math.pi,euler_angles_[1]* 180 / math.pi,euler_angles_[2]* 180 / math.pi)


    print('\n\n-----------------------------------------------------')

def draw_show_on_image(frame,axi_imgpts,corners,ret,line_width=2):
    # We can now plot limes on the 3D image using the cv2.line function,numpy.ravel-->Return a contiguous flattened array.
    cv2.drawChessboardCorners(frame, (7,9), corners, ret)#column and rows 7x9 after the calibration i do not need anymore
    cv2.line(frame, tuple(axi_imgpts[3].ravel()), tuple(axi_imgpts[1].ravel()), (0,255,0), line_width) #GREEN Y
    cv2.line(frame, tuple(axi_imgpts[3][0]), tuple(axi_imgpts[2].ravel()), (255,0,0), line_width) #BLUE Z
    cv2.line(frame, tuple(axi_imgpts[3,0]), tuple(axi_imgpts[0].ravel()), (0,0,255), line_width) #RED x

    # for idx, corner in enumerate(corners):
    #     idx_as_str = '{}'.format(idx)
    #     text_pos = (corner + np.array([3.5,-7])).astype(int)
    #     cv2.putText(frame, idx_as_str, tuple(text_pos),cv2.FONT_HERSHEY_PLAIN, 1, (0, 0,255))

    # Display the resulting frame
    cv2.imshow('frame',frame)
    #cv2.imwrite('test.jpg', frame)

def locate_target_orientation(frame):
    #2D image points. If you change the image, you need to change vector
    image_points = np.array([
                                (223, 290),     # left down
                                (274, 292),     # right down
                                (228, 280),     # left middle
                                (265, 281),     # right middle
                                (248, 287),     # center
                                (248, 278)      # top
                            ], dtype="double")

    # 3D model points.
    model_points = np.array([
                                (2.0, 0.0, 3.0),
                                (2.0, 8.0, 3.0),
                                (1.0, 0.0, 4.8),
                                (1.0, 5.5, 4.8),
                                (2.0, 4.0, 4.0),
                                (2.0, 4.0, 6.5)

                            ])

    # Camera internals
    #Intrinsic parameters===>>> from the intrinsic calibration!!!!
    list_matrix=[529.3652640113527, 0, 310.3141830332983, 0, 540.6164768242445, 220.3657848482968, 0, 0, 1]
    cameraMatrix_ar=np.asarray(list_matrix).reshape(3,3)
    distCoef=[0.1852661379687586, -0.264551739977949, -0.03684812841833995, 0.0009882520270208214, 0]
    distCoef_ar=np.asarray(distCoef).reshape(len(distCoef),1)


    #Rotation vector (radians)
    (success, rotation_vector, translation_vector) = cv2.solvePnP(model_points, image_points, cameraMatrix_ar, distCoef_ar, flags=cv2.SOLVEPNP_ITERATIVE)


    # World coordinates system
    axis = np.float32([[0.06,0,0],[0,0.06,0],[0,0,0.06],[2.0,4.0,4.0]])
    axis_imgpts, jacobian = cv2.projectPoints(axis, rotation_vector, translation_vector,cameraMatrix_ar, distCoef_ar)
    #print(axis_imgpts)

    line_width=2

    cv2.line(frame, tuple(axis_imgpts[3,0]), tuple(axis_imgpts[1].ravel()), (0,255,0), line_width) #GREEN Y
    cv2.line(frame, tuple(axis_imgpts[3,0]), tuple(axis_imgpts[2].ravel()), (255,0,0), line_width) #BLUE Z
    cv2.line(frame, tuple(axis_imgpts[3,0]), tuple(axis_imgpts[0].ravel()), (0,0,255), line_width) #RED x

    # Display image
    cv2.imshow("Output", frame)


def main():

    counter=0
    tmpNamec='temp2.jpg'

    pub_pose = rospy.Publisher('pose_camera_topic', Pose, queue_size=10)
    sub_pose = rospy.Subscriber('/pose_camera_topic', Pose, pose_camera_callback)
    br = tf2_ros.TransformBroadcaster()

    rate = rospy.Rate(10) # 10hz

    import sys
    print "This is the name of the script: ", sys.argv[0]
    #flag=sys.argv[1]

    while not rospy.is_shutdown():

        counter+=1

        # Capture frame-by-frame
        frame=camObj.get_image()


        #print(type(frame))
        if frame is None:
            print('no image!!!')
            continue

        #cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('orientation_img.jpg', frame)
            break


        rate.sleep()

        locate_target_orientation(frame)
        print('\ncounter:',counter,'\n')



    # When everything done, release the capture
    cv2.destroyAllWindows()


if __name__ == '__main__':
    camObj=camera()
    main()
