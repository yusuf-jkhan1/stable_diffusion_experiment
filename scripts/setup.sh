echo 'Begining Primary Installs'
wget -q https://raw.githubusercontent.com/buildspace/diffusers/main/examples/dreambooth/train_dreambooth.py
wget -q https://github.com/ShivamShrirao/diffusers/raw/main/scripts/convert_diffusers_to_original_stable_diffusion.py
cd ..
pip install -r requirements.txt
echo 'Begining xformers install (this may take some time)'
pip install git+https://github.com/facebookresearch/xformers@4c06c79#egg=xformers