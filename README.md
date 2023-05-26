
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/adirpedroso/ROS_stage_controller/blob/main/LICENSE)
# ROS_stage_controller

Navegação de robô diferencial no ambiente de simulação Stage- Distância entre 2 pontos

# Sobre o projeto:
## Pré-requisitos
- Python 3
- ROS 1
# Como executar o pacote:

O seguinte comando dará clone no repositório [stage_controller](https://github.com/adirpedroso/ROS_stage_controller/tree/main) para dentro da sua pasta catkin do ROS
```bash
cd catkin_ws/src/ && git clone https://github.com/adirpedroso/ROS_stage_controller.git
```
Após isso, execute os seguintes comandos:
```bash
cd .. 
catkin_make
```
Em seguida:
```bash
source devel/setup.bash
cd src/ROS_stage_controller/scripts/
chmod +x sh_stage_controller.py 
```
Se tudo estiver certo, basta executar os passos para iniciar o ambiente Stage:
```bash
roslaunch ROS_stage_controller launcher.launch 
```
Após o simulador aberto, execute o script em python:
```bash
roslaunch ROS_stage_controller launcher.launch 
```
