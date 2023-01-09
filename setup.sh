echo 'Begining Primary Installs'
pip install -r requirements.txt

echo 'Setup is expecting a .env file with a huggingface read token(hf_read_token)'
echo 'Setting up huggingface token'
mkdir -p ~/.huggingface
if [ -f .env ]
then
    export $(cat .env | xargs)
    echo -n $hf_read_token > ~/.huggingface/token
fi

