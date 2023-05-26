
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/adirpedroso/ROS_stage_controller/blob/main/LICENSE)
# ROS_stage_controller
Navegação de robô diferencial no ambiente de simulação Stage- Distância entre 2 pontos

# Sobre o projeto:

# Como executar o pacote:

Clone o repositório para dentro da pasta catkin
```bash
git clone https://github.com/adirpedroso/ROS_stage_controller.git
```
e
Para iniciar a simulação é necessario 2 passos:

1º: rodar o comando no terminal: roslaunch dois_stage_controller launcher.launch
	esse cimando ira abrir o ambiente de simulação (não é executado tudo junto para facilitar a 	    visualização da simulação)
		
2º:Agora, após o ambiente aberto, rodamos o código de nabegação: rosrun dois_stage_controller sh_stage_controller.py 

*Para testar novos pontos de chegada, basta abrir abrir o código, para isso execute esse comando: gedit catkin_ws/src/dois_stage_controller/scripts/sh_stage_controller.py 

 a agora na linha 24 e 25, altere os valores de targer_x e target_y
