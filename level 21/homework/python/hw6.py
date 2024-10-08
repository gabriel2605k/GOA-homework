# 6) დამატებით თქვენთვითონ მოიფიქრეთ რაიმე
# ამოცანები რაზეც ფიქრობთ რომ for loop გამოგადგებათ და ივარჯიშეთ ამაზე ბევრი
secret_number = 42 
attempts = 0
for attempt in range(5):
    user_guess = int(input("Guess number between 1 and 100: "))
    if user_guess == secret_number:
        print(" Congratulations! You guessed my number in", attempt + 1, "attempts.")
        
    elif user_guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
    attempts += 1
if attempts == 5:
    print(" you didn't guessnumber. It was", secret_number)