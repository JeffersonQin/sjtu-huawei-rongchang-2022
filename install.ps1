python -m venv venv
venv\Scripts\Activate.ps1
pip install torch==1.8.2 torchvision==0.9.2 torchaudio===0.8.2 --extra-index-url https://download.pytorch.org/whl/lts/1.8/cu111
pip install -U openmim
mim install mmcv-full
cd .\wrc\mmdetection ; python setup.py install
