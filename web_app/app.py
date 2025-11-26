from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vand10a_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

# حالة اللعبة
game_state = {
    'players': ['Marcus', 'Fahad', 'Ruffin', 'Kaled', 'Murgar'],
    'current_player': 0,
    'top_card': '7♥',
    'direction': 1,
    'connected_players': []
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html', game=game_state)

@app.route('/api/game-state')
def api_game_state():
    return jsonify(game_state)

# WebSocket events
@socketio.on('connect')
def handle_connect():
    print(f'Client connected: {request.sid}')
    emit('connected', {'message': 'Ansluten till spelet!'})

@socketio.on('join_game')
def handle_join_game(data):
    player_name = data.get('name', 'Anonymous')
    game_state['connected_players'].append(player_name)
    
    emit('player_joined', {
        'player': player_name,
        'all_players': game_state['connected_players']
    }, broadcast=True)
    
    print(f'Player {player_name} joined the game')

@socketio.on('play_card')
def handle_play_card(data):
    player_index = data.get('player_index')
    card_index = data.get('card_index')
    
    if player_index == game_state['current_player']:
        # تغيير اللاعب الحالي
        game_state['current_player'] = (game_state['current_player'] + game_state['direction']) % len(game_state['players'])
        
        # تحديث الكرت العلوي (عشوائي لل演示)
        cards = ['A♥', 'K♠', 'Q♦', 'J♣', '10♥', '9♠', '8♦', '7♣', '6♥', '5♠']
        game_state['top_card'] = random.choice(cards)
        
        # إرسال التحديث للجميع
        emit('game_update', {
            'game_state': game_state,
            'message': f'{game_state["players"][player_index]} spelade ett kort!'
        }, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    print(f'Client disconnected: {request.sid}')

if __name__ == '__main__':
    print("🎴 Vänd 10a Web Server startar...")
    print("🌐 Gå till: http://localhost:5000")
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
