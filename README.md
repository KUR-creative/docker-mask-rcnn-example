## Docker
[install and config](script/install/)
- [install Docker on Ubuntu22](script/install/docker.ubuntu22.sh) - [출처](https://github.com/KUR-creative/inits/blob/master/install-scripts/docker.ubuntu22.sh)
- [post-install process](script/install/docker-postinstall.ubuntu22.sh) - [출처](https://github.com/KUR-creative/inits/blob/master/install-scripts/docker-postinstall.ubuntu22.sh)
- [Use gpu in Docker container](script/install/docker.nvidia-container-toolkit.sh) - [출처](https://github.com/KUR-creative/inits/blob/master/install-scripts/docker.nvidia-container-toolkit.sh)

Docker container as dev env in vscode
- vscode에서 [dev container extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 설치
- vscode에서 명령 실행: `Dev Containers: Open Folder in Container...` 이후 vscode 터미널 창에서 python 실행 가능
- `Dockerfile`이나 `.devcontainer/devcontainer.json`이 변경될 경우 명령 실행: `Dev Containers: Rebuild Container and Rebuild Container Without Cache`

## 출처
참고 튜토리얼 - [출처](https://pytorch.org/tutorials/intermediate/torchvision_tutorial.html)

다음 소스 코드 다운로드
- 튜토리얼 코드 - [출처](https://github.com/pytorch/tutorials/blob/main/intermediate_source/torchvision_tutorial.py)
  - https://raw.githubusercontent.com/pytorch/tutorials/main/intermediate_source/torchvision_tutorial.py
- 그 외 코드(추가 설치) - [출처](https://github.com/pytorch/vision/tree/main/references/detection)
  - https://raw.githubusercontent.com/pytorch/vision/main/references/detection/engine.py
  - https://raw.githubusercontent.com/pytorch/vision/main/references/detection/utils.py
  - https://raw.githubusercontent.com/pytorch/vision/main/references/detection/coco_utils.py
  - https://raw.githubusercontent.com/pytorch/vision/main/references/detection/coco_eval.py
  - https://raw.githubusercontent.com/pytorch/vision/main/references/detection/transforms.py

추가적인 [디펜던시](https://github.com/pytorch/vision/blob/main/references/detection/README.md) 설치
- matplotlib, pycocotools

그리고.. notebook이 아니므로 제대로 출력하도록 살짝 수정.
