import requests, argparse

parser=argparse.ArgumentParser(description="Webhook Parameters")
parser.add_argument("--webhook_url", type=str)
parser.add_argument("--secret_message", type=str)
args=parser.parse_args()

# Ngrok URL provided by the receiver
ngrok_url = args.webhook_url
message = args.secret_message
# The secret funny message
secret_message = {"message": message}

# Send the POST request
response = requests.post(ngrok_url, json=secret_message)

