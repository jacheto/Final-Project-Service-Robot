# Service Robot

## About the project
This is my final project at University. It is a 1.5 m (or 5 feet) service robot that can map the environment and walk in a room, avoiding walls, obstacules and humans. I did it with 3 other people, my part was basically doing all the software / coding / intelligence of the robot. We used ROS Kinetic running in Ubuntu for the robot brain.

Here is a tutorial to remind myself if I ever need to run the software again (it is in portuguese):

### Como configurar o projeto

#### 1.Requisitos:
##### 1.1 Ubuntu 16.04 instalado
Separe pelo menos 20gb para o sistema se for dual boot

##### 1.2 ROS versão Kinetic instalado
Abra o terminal do linux (Ctrl+Alt+T) e digite os comandos:

Configure a lista de sources:

    sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

Configure as chaves:

    sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

Atualize o apt-get:

    sudo apt-get update
    
Baixe o pacote full do ROS Kinect: (pode demorar)
    
    sudo apt-get install ros-kinetic-desktop-full

Inicie o rosdep:

    sudo rosdep init
    rosdep update

Adicione o ROS no bashrc:

    echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
    source ~/.bashrc
    
Teste se foi instalado corretamente iniciando o sistema do ROS: (depois aperte Ctrl+C para parar o sistema)

    roscore
    
Adicione esses pacotes para a criação de workspaces:
    
    sudo apt install python-rosinstall python-rosinstall-generator python-wstool build-essential

##### 1.3 Workspace do Roboserv

Agora vamos ver como baixar e configurar o projeto.
Vá até o diretorio principal:
    
    cd ~
    
Crie uma nova pasta, que será o workspace do robô, e entre nela:

    mkdir roboserv_ws
    cd roboserv_ws

Clone o repositório dentro desta pasta: (deverá aparecer uma pasta chamada workspace_ws

    git clone "https://github.com/jacheto/Roboserv.git"

Já temos o projeto, agora vamos resolver as dependencias para o robo conseguir rodar:
Compile o workspace:
    
    cd ~/roboserv_ws
    catkin_make

Instale o turtlebot, robô que pegamos emprestados algumas features:

    sudo apt-get install ros-kinetic-turtlebot*

Instale o pointcloud_to_laserscan, um pacote para gerar um laser scan a partir de uma nuvem de pontos:

    sudo apt-get install ros-kinetic-pointcloud-to-laserscan
    
Adicione o workspace na lista de pastas onde o ROS procura os pacotes:
    
    echo "export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$HOME/roboserv_ws/src" >> ~/.bashrc
    source ~/.bashrc
    
Verifique se o ROS achou os pacotes do robô: (digite isto e aperte tab, se autocompletar então deu sucesso)

    roscd robose
    
Pronto! Agora é só iniciar o projeto:

    roslaunch roboserv_simulation roboserv_simulation.launch
    
### Divirta-se!
