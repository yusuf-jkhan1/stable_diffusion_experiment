echo '=== Beginning Setup ==='
pip install -qq git+https://github.com/ShivamShrirao/diffusers
pip install -q -U --pre triton
pip install -q accelerate==0.15.0 transformers==4.25.1 ftfy bitsandbytes==0.35.0 gradio natsort ninja
pip install -v -U git+https://github.com/facebookresearch/xformers.git@47ab8b812fbc0518eb6b630440548c1ff7915500#egg=xformers


mkdir -p ~/.huggingface
if [ -f .env ]
then
    echo 'Setting up huggingface token'
    export $(cat .env | xargs)
    echo -n $hf_read_token > ~/.huggingface/token
else
    echo 'Setup is expecting a .env file with a huggingface read token(hf_read_token)'
    echo 'No .env file found'
fi

sudo apt-get update
sudo apt-get -y install git-lfs

echo '=== Completed Setup ==='