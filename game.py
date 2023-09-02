import random

# Initialize the game variables
track_length = 20  # Length of the racetrack
player_position = track_length // 2  # Initial position of the player's car
enemy_position = random.randint(0, track_length - 1)  # Initial position of the enemy car

# Main game loop
while True:
    # Display the racetrack
    track = [" "] * track_length
    track[player_position] = "P"
    track[enemy_position] = "E"
    
    print("".join(track))
    
    # Get user input
    move = input("Press 'L' to move left, 'R' to move right, or 'Q' to quit: ").upper()
    
    # Quit the game
    if move == "Q":
        print("Game over!")
        break
    
    # Move the player's car
    if move == "L":
        player_position -= 1
    elif move == "R":
        player_position += 1
    
    # Move the enemy car
    enemy_position += random.randint(-1, 1)
    
    # Check for collisions
    if player_position == enemy_position:
        print("You crashed! Game over!")
        break
    
    # Check if the player has won
    if player_position >= track_length:
        print("You won! Congratulations!")
        break
