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
sys.path.insert(0, '/home/casch/yumi_depends_ws/src/thesis_pkg/yumi_main/scripts/project')

from thesis_library import *

from yumipy import YuMiRobot

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
    #t0.child_frame_id = "panda_link0"
    #t0.child_frame_id = "yumi_base_link"
    t0.child_frame_id = "base_link"
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
    t1.transform.translation.x = 0.286213
    t1.transform.translation.y = 0.115956
    t1.transform.translation.z = -0.00933129

    tmp_rot=np.array([[1, 0, 0], [0, 1, 0],[0, 0, 1]])
    tmp_trans=np.array([[0.286213],[0.115956],[-0.00933129]])
    myrot =np.hstack((tmp_rot,tmp_trans))
    myrot=np.vstack((myrot,[0.0,0.0,0.0,1.0]))
    print('my rotation: \n {}'.format(myrot) )

    q1 = tf.transformations.quaternion_from_matrix(myrot)
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
    t2.transform.translation.z = 1.0*position_[2]
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

    r_matrix=rvec_matrix.T
    t_position=-np.dot(rvec_matrix.T, translation_vector)
    print('euler_angles inv roll_,pitch_,yaw:  \n',euler_angles_)
    print(euler_angles_[0]* 180 / math.pi,euler_angles_[1]* 180 / math.pi,euler_angles_[2]* 180 / math.pi)
    mat =np.hstack((r_matrix,t_position))
    mat=np.vstack((mat,[0.0,0.0,0.0,1.0]))
    print('transform world->camera:')
    print(mat)


    print('\n\n-----------------------------------------------------')

def draw_show_on_image(frame,axi_imgpts,corners,ret,line_width=2):
    # We can now plot limes on the 3D image using the cv2.line function,numpy.ravel-->Return a contiguous flattened array.
    #cv2.drawChessboardCorners(frame, (7,9), corners, ret)#column and rows 7x9 after the calibration i do not need anymore
    cv2.line(frame, tuple(axi_imgpts[3].ravel()), tuple(axi_imgpts[1].ravel()), (0,255,0), line_width) #GREEN Y
    cv2.line(frame, tuple(axi_imgpts[3][0]), tuple(axi_imgpts[2].ravel()), (255,0,0), line_width) #BLUE Z
    cv2.line(frame, tuple(axi_imgpts[3,0]), tuple(axi_imgpts[0].ravel()), (0,0,255), line_width) #RED x

    # for idx, corner in enumerate(corners):
    #     idx_as_str = '{}'.format(idx)
    #     text_pos = (corner + np.array([3.5,-7])).astype(int)
    #     cv2.putText(frame, idx_as_str, tuple(text_pos),cv2.FONT_HERSHEY_PLAIN, 1, (0, 0,255))
    #print(axi_imgpts)
    #print()

    text_pos = (axi_imgpts[0].ravel() + np.array([3.5,-7])).astype(int)
    cv2.putText(frame,'X', tuple(text_pos),cv2.FONT_HERSHEY_PLAIN, 1, (0, 0,255))
    text_pos = (axi_imgpts[1].ravel() + np.array([3.5,-7])).astype(int)
    cv2.putText(frame,'Y', tuple(text_pos),cv2.FONT_HERSHEY_PLAIN, 1, (0, 0,255))
    text_pos = (axi_imgpts[2].ravel() + np.array([3.5,-7])).astype(int)
    cv2.putText(frame,'Z', tuple(text_pos),cv2.FONT_HERSHEY_PLAIN, 1, (0, 0,255))

    text_pos = (axi_imgpts[3].ravel() + np.array([0,-100])).astype(int)
    cv2.putText(frame,'1unit=2cm', tuple(text_pos),cv2.FONT_HERSHEY_PLAIN, 1, (0, 0,255))

    # Display the resulting frame
    cv2.imshow('Target locator',frame)
    cv2.imwrite('test.jpg', frame)

def locate_target_orientation(frame,ret, corners):

    # 3D world points.
    x,y=np.meshgrid(range(7),range(9))#col row
    world_points_3d=np.hstack((y.reshape(63,1)*0.020,x.reshape(63,1)*0.020,np.zeros((63,1)))).astype(np.float32)
    # print(world_points_3d)
    # print(corners)
    # exit(0)

    # Camera internals
    #Intrinsic parameters===>>> from the intrinsic calibration!!!!
    list_matrix=[616.5322265625, 0, 323.4304504394531, 0, 616.58984375, 233.87391662597656, 0, 0, 1]
    cameraMatrix_ar=np.asarray(list_matrix).reshape(3,3)
    # print(cameraMatrix_ar.shape)
    # print(cameraMatrix_ar)
    # print(cameraMatrix_ar[1,:])



    #distCoef=[0.0, 0.0, 0.0, 0.0, 0,0]
    distCoef=[0.1852661379687586, -0.264551739977949, -0.03684812841833995, 0.0009882520270208214, 0]
    distCoef_ar=np.asarray(distCoef).reshape(len(distCoef),1)
    # print(distCoef_ar)
    # print(distCoef_ar.shape)

    #Rotation vector (radians)
    (success, rotation_vector, translation_vector) = cv2.solvePnP(world_points_3d, corners, cameraMatrix_ar, distCoef_ar, flags=cv2.SOLVEPNP_ITERATIVE)
    #_, rvecs, tvecs, inliers=cv2.solvePnPRansac(world_points_3d, corners, cameraMatrix_ar, distCoef_ar)


    # World coordinates system
    axis = np.float32([[0.10,0,0],[0,0.10,0],[0,0,0.10],[0,0,0]])
    axis_imgpts, jacobian = cv2.projectPoints(axis, rotation_vector, translation_vector,cameraMatrix_ar, distCoef_ar)
    print('coordinates syste in camera image')
    print('axi_imgpts: ',axis_imgpts)
    print('\n')
    # Rotation_vector into rotation_matrix
    rvec_matrix = cv2.Rodrigues(rotation_vector)[0]


    return axis_imgpts,corners,ret,rvec_matrix,translation_vector,rotation_vector

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

        frame=cv2.imread('temp3.jpg')
        #frame=camObj.get_image()

        #print(type(frame))
        if frame is None:
            print('no image!!!')
            continue

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('temp3.jpg', frame)
            break

        try:
            # 2D image points
            # To handle the corners array more easily, we can reshape it as follows
            ret, corners = cv2.findChessboardCorners(frame, (7,9))#coulmn and rows
            corners=corners.reshape(-1,2)#undefied number of rows
            if not ret:
                print('\nPlease, locate well the calibration target!!!')
                continue
        except Exception as ex:
            print('\nStatus of findChessboardCorners: {}'.format(ret))
            print('Please, locate well the calibration target!!!')
            print(ex)
            print('-------------------------------------------------')
            continue


        # Extrinsic calibration!!!
        axis_imgpts,corners,ret,rvec_matrix,translation_vector,rotation_vector= locate_target_orientation(frame,ret, corners)


        # print information about rotation and translation for the camera and world frame
        print_information(rotation_vector,translation_vector,rvec_matrix)


        #draw and display lines and text on the image
        draw_show_on_image(frame,axis_imgpts,corners,ret)


        # get transform matrix from rotation and translation of the camera frame relative to the world frame
        mat=data_to_transform(rvec_matrix.T,-np.dot(rvec_matrix.T, translation_vector))
        #print(mat)

        # get the pose of the camera frame relative to the world frame
        pose=transform_to_pose(mat)
        #print(pose)

        # publish pose of the camera frame
        pub_pose.publish(pose)

        # we should expect to go through the loop 10 times per second
        rate.sleep()

        # publish transform for the following coordinate frames: target, camera and world
        publish_transforms(br)


        print('\ncounter:',counter,'\n')



    # When everything done, release the capture
    cv2.destroyAllWindows()


if __name__ == '__main__':
    camObj=camera()
    main()