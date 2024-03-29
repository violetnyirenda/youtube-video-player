from flask import Flask, request, jsonify
import random


app = Flask(__name__)

animals = ["monkey", "lion", "zebra", "dog", "tiger"]
chosen_animal = random.choice(animals).lower()
guessed_letters = set()
attempts = 6

@app.route('/genius', methods=['POST'])
def animals():
    global attempts, guessed_letters

    data = request.get_json()

    if 'guess' not in data:
        return jsonify({'error': 'Missing guess parameter'}), 400

    guess = data['guess'].lower()

    if guess in guessed_letters:
        return jsonify({'message': 'You already guessed that letter. Try again.'}), 200

    guessed_letters.add(guess)

    if guess not in chosen_animal:
        attempts -= 1

    game_state = ''.join(letter if letter in guessed_letters else '_' for letter in chosen_animal)

    response = {
        'attempts_left': attempts,
        'game_state': game_state,
    }

    if '_' not in game_state:
        response['message'] = 'Congratulations! You guessed the animal.'
    elif attempts == 0:
        response['message'] = f'Sorry, you ran out of attempts. The animal was: {chosen_animal}'

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)





