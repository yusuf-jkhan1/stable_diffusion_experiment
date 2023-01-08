!wget -q https://raw.githubusercontent.com/buildspace/diffusers/main/examples/dreambooth/train_dreambooth.py
!wget -q https://github.com/ShivamShrirao/diffusers/raw/main/scripts/convert_diffusers_to_original_stable_diffusion.py
%pip install -qq git+https://github.com/ShivamShrirao/diffusers
%pip install -q -U --pre triton
%pip install -q accelerate==0.15.0 transformers ftfy bitsandbytes==0.35.0 gradio natsort