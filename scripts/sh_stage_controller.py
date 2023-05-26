#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import *
from sensor_msgs.msg import *
from nav_msgs.msg import *
import random
import math

scan_data = LaserScan()  # Variável para armazenar dados do laser
odom_data = Odometry()  # Variável para armazenar dados da odometria

def callback_odometry(data):
    global odom_data
    odom_data = data

def callback_laser(data):
    global scan_data
    scan_data = data

if __name__ == "__main__":
    rospy.init_node("controller_node", anonymous=False)
    rospy.Subscriber("/base_scan", LaserScan, callback_laser)  # Assina o tópico do laser
    rospy.Subscriber("/base_pose_ground_truth", Odometry, callback_odometry)  # Assina o tópico da odometria

    target_x = 1.0  # Coordenada X do destino
    target_y = 3.0  # Coordenada Y do destino
    min_distance = 0.4  # Distância mínima para parar o robô

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)  # Publica comandos de velocidade
    rate = rospy.Rate(5)  # Frequência de atualização (10 Hz)
    velocity = Twist()  # Objeto Twist para enviar comandos de velocidade

    while not rospy.is_shutdown():
        x = odom_data.pose.pose.position.x  # Posição atual em X
        y = odom_data.pose.pose.position.y  # Posição atual em Y

        # Verifica se chegou ao destino, se a distância for menor que a distância mínima, para o robô
        distance = math.sqrt((x - target_x) ** 2 + (y - target_y) ** 2)
        if distance <= min_distance:
            rospy.loginfo("Opa, Cheguei no destino.")
            velocity.linear.x = 0.0  # Para o movimento linear
            velocity.angular.z = 0.0  # Para o movimento angular
            pub.publish(velocity)
            break

        rospy.loginfo("Estou em X: %s, e em Y: %s", x, y)

        # Verifica se o tamanho da lista de leituras do laser é maior que 0 e se a menor distância é maior que 0.5
        if len(scan_data.ranges) > 0 and min(scan_data.ranges) > 0.5:
            velocity.linear.x = random.uniform(0.0, 0.5)  # Define uma velocidade linear aleatória
            velocity.angular.z = random.uniform(-1.0, 1.0) * random.uniform(0.0, 0.5)  # Define uma velocidade angular aleatória
            rospy.loginfo("Estou procurando, quase lá...")

        # Caso contrário, gira (encontrou uma parede)
        else:
            velocity.linear.x = 0.0  # Para o movimento linear
            velocity.angular.z = 0.50  # Define uma velocidade angular fixa
            rospy.loginfo("Girando")

        pub.publish(velocity)  # Publica os comandos de velocidade
        rate.sleep()  # Aguarda a próxima iteração no loop com a frequência definida
