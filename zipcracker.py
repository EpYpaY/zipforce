from pathlib import Path
from zipfile import ZipFile
from tqdm import tqdm

# Import the word list and the zip file
word_list = Path(str(input('Word List Path:')))
zip_file_path = Path(str(input('Zip File Path:')))

# Define the function to attack the password
def attack_password():
    zip_file = ZipFile(zip_file_path)
    n_passwords = len(list(open(word_list, 'rb')))
    print('Total passwords to test:', f'{n_passwords:,}')

    # Test the password
    with open(word_list, 'rb') as wordlist:
        for word in tqdm(wordlist, total=n_passwords, unit='password'):
            try:
                zip_file.extractall(pwd=word.strip())
            except:
                continue
            else:
                print('\n[+] Password found:', word.decode().strip())
                exit(0)
    
    print("\n[!] Password not found, try another wordlist.")

# Check if the word list and the zip file exist
if word_list.exists() and zip_file_path.exists():
    attack_password()

else:
    print('The word list or the zip file does not exist.')
    exit(1)