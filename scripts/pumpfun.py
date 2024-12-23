from solana.account import Account
from solana.rpc.api import Client
from solana.system_program import TransferParams, transfer
from solana.transaction import Transaction
import base58

# Connect to Solana network (Devnet for testing)
client = Client("https://api.devnet.solana.com")

# Your Solana private key
private_key = [your_private_key_bytes_here]
account = Account(private_key)

# Program ID (from deployment step)
program_id = "Your_Solana_Program_ID"

# Define the Twitter account and website
twitter_account = "x.com/klyote"
website = "https://github.com/Tianyu-Zhao-Sakana/klyote"

# Example function to update the market cap and store info on Solana
def send_transaction(twitter_account, website, market_cap):
    transaction = Transaction()
    
    # Create an instruction to update the contract with new info
    instruction_data = (
        twitter_account.encode('utf-8') + 
        website.encode('utf-8') + 
        market_cap.to_bytes(8, 'big')
    )

    # Create the transaction instruction for your Solana program
    instruction = {
        'program_id': program_id,
        'accounts': [
            {'pubkey': account.public_key(), 'is_signer': True, 'is_writable': False},
        ],
        'data': base58.b58encode(instruction_data).decode('utf-8'),
    }

    transaction.add(instruction)

    # Send transaction
    response = client.send_transaction(transaction, account)
    print("Transaction response:", response)

# Call the function to update the contract
send_transaction("your_twitter_handle", "https://yourwebsite.com", 100000000)
