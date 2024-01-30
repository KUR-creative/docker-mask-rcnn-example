참고 튜토리얼 - [출처](https://pytorch.org/tutorials/intermediate/torchvision_tutorial.html)

다음 소스 코드 다운로드
- 튜토리얼 코드 - [출처](https://github.com/pytorch/tutorials/blob/main/intermediate_source/torchvision_tutorial.py)
  - `wget https://raw.githubusercontent.com/pytorch/tutorials/main/intermediate_source/torchvision_tutorial.py`
- 그 외 코드(추가 설치) - [출처](https://github.com/pytorch/vision/tree/main/references/detection)
  - `wget https://raw.githubusercontent.com/pytorch/vision/main/references/detection/engine.py`
  - `wget https://raw.githubusercontent.com/pytorch/vision/main/references/detection/utils.py`
  - `wget https://raw.githubusercontent.com/pytorch/vision/main/references/detection/coco_utils.py`
  - `wget https://raw.githubusercontent.com/pytorch/vision/main/references/detection/coco_eval.py`
  - `wget https://raw.githubusercontent.com/pytorch/vision/main/references/detection/transforms.py`

추가적인 [디펜던시](https://github.com/pytorch/vision/blob/main/references/detection/README.md) 설치
- matplotlib, pycocotools

그리고.. notebook이 아니므로 제대로 출력하도록 살짝 수정.
