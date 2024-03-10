# Create a set of letters to find letters index and encrypt or decrypt them using shift number.
# We'll use set of alphabet twice to shift letters like v,w,x,y,z.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Create a function for encryption of message
# Create a function called 'encrypt' that takes the 'plain_msg' and 'shift' as inputs.
def caeser(start_text, shift_count, direction):
  end_text = ""
  if direction == 2:
      shift_count *= -1
  # If his message contain more than a-z letters means some special character or space or numbers
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_count
      end_text += alphabet[new_position]
    else:
      end_text +=char
  print(f"\nYour Result Message is: {end_text}\n")

# Import program logo from cipher logo file
from Caeser_Cipher_logo import logo
print(logo)

# Create a system where user can code decode message unlimited times.
project_status = False
while not project_status:
  #Ask user, what he want to do.
  direction = int(input("\n\nType '1' to encrypt the message, or type '2' to decrypt the message or type '3' for exit:\n"))
  if direction not in [1,2,3]:
      print("Please select valid options")
      break
  # If user want to exit at first place
  if direction == 3:
    project_status = True
    print("Good Bye")
    break
  # Else, Ask for his message
  text = input("Type your message:\n").lower()
  # Ask for his shift number
  shift = int(input("Type the shift number:\n"))
  # If he entered shift number more than 26 letters
  if shift > 26:
    shift = shift % 26
  caeser(start_text = text, shift_count = shift, direction = direction)
