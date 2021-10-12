from tkinter import messagebox, simpledialog, Tk

# boolean function that returns if the length is even or not
def is_even(number):
    return number % 2 == 0

# returns the list of characters at even index positions
def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

# returns the list of characters at odd index positions
def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

# prepare message
def swap_letters(message):
    # initialize empty list
    letter_list = []
    # append 'x' to the message if the length message is odd
    if not is_even(len(message)):
        message = message + 'x'

    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)

    # iterate over both the lists and append odd letter and even letter at the specific 'counter' value
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])

    # make list to string
    new_message = ''.join(letter_list)
    return new_message

# gets the task to perform: encrypt or decrypt
def get_task():
    task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')
    return task

# gets the message to encrypt or decrypt
def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message: ')
    return message

root = Tk()
while True:
    task = get_task()
    if task == 'encrypt':
        message = get_message()
        encrypted = swap_letters(message)
        messagebox.showinfo('Ciphertext of the secret message is:', encrypted)
        
    elif task == 'decrypt':
        message = get_message()
        decrypted = swap_letters(message)
        messagebox.showinfo('Plaintext of the secret message is:', decrypted)
    else:
        break
    
root.mainloop()