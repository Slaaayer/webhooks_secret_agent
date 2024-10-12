# Prerequisites

1. If it wasn't done already, install the following prerequisites :
 - [Python](https://www.python.org/) > v3.10
 - [Poetry](https://python-poetry.org/docs/) = v1.4.2
 - [Ngrok](https://ngrok.com/) = v3.16.0 Make sure you create an ngrok account. If you're on Windows and experiencing some issues with the antivirus software, check the following [Confluence](https://dentalm.atlassian.net/wiki/spaces/QAT/pages/3921018892/How+To+run+GW+automated+tests).
2. Install your poetry environment : 

```bash
cd <workspace>/webhooks_secret_agents
```

# Mission setup

## Objective
Participants will work in pairs. You’re secret agents on a mission. One of you will set up a secure server, ready to receive a classified message, while the other sends that message through a hidden tunnel using Ngrok. The goal? Get the secret message to your partner without anyone else knowing. The receiver needs to catch the message and display it on their server—simple, but critical. Think you’ve got what it takes to pull it off? Let’s find out.

# Mission Execution
Alright, agents, here’s the deal: One of you will set up a secret base (the webhook listener) to receive an encrypted message, and the other will send that message through an underground tunnel (Ngrok). You need to get the message across, intercept it, and make sure no one else sniffs it out. If something goes wrong and the message is compromised, consider the mission a failure. Stay sharp.

##  Step 1: Set Up Your Covert Listening Post

As the **receiver**, your job is to get your listening post up and running. This is your secure base where you’ll be intercepting messages. Run the `setup_listener.py` script to get things started. But before you dive in, take a quick look at the script to make sure you understand what it's doing—you don’t want any surprises.

```bash
cd <workspace>/webhooks_secret_agents
poetry run python3 setup_listener.py
```

After that, check if your listener is working by visiting https://localhost:5000/webhook. You shouldn’t see any errors, just a message confirming your base is ready—though no transmissions have come through yet.


## Step 2: Set Up the Secure Tunnel

Now that your base is ready, you need to open a secret tunnel to communicate with your partner. As the receiver, it’s up to you to set up Ngrok. First, grab your authentication token by following these steps from the [Ngrok documentation](https://dashboard.ngrok.com/get-started/your-authtoken).

Once you’ve got your token, open a new terminal and fire up Ngrok with this command:

```bash
ngrok http 5000
```

Ngrok will give you a URL (something like https://xyz.ngrok.io). This is your tunnel. **Only share it with your partner (the sender)**. Nobody else should know about this.

As the **sender**, check that the tunnel works by visiting <ngrok_link>/webhook. You should see the same confirmation message as your partner. If you get a security warning, just hit "Proceed"—don’t worry, the mission’s secure.

## Step 3: Send the Secret Message

Now it’s time to send the secret message. As the **sender**, you’ll run the message_sender.py script. It takes two arguments:

 - `webhook_url`: This is the tunnel URL the receiver shared with you.
 - `secret_message`: The actual message you want to send.

```bash
cd <workspace>/webhooks_secret_agents
poetry run python3 message_sender.py --webhook_url <url> --secret_message <message>
```

Make sure you replace `<url>` with the actual Ngrok link from your partner, and don’t forget to make the message fun or clever—but remember, it’s classified. If someone else gets ahold of it, the whole mission’s blown.

## Step 4: Intercept and Verify

As the **receiver**, your job now is to intercept the message and make sure it’s the one your partner sent—untouched. Visit the Ngrok tunnel URL (`<ngrok_link>/webhook`) and verify that everything checks out.

To make sure no unauthorized eyes have been snooping around, log into your Ngrok account and use the **traffic inspector** to check the logs. You’ll see a record of every transmission that went through the tunnel. If it’s just you and your partner, you’re good. Otherwise, you may have a problem.

## Bonus Mission: Automate It

There’s more intel to share, and the sender’s running out of time. Write a script to automate fetching the secret message from the Ngrok tunnel. Use `pyngrok` to make this easier. Your goal is to create a seamless, automatic process so messages can be intercepted without anyone lifting a finger.

Good luck, agents. Don’t let the mission slip.