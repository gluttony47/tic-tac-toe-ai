# Tahir's tic-tac-toe project

## Architecture

tic-tac-toe
|
|

- presentation_layer(front_end)
  |
  | - command_line_interface
  |
  |
- game_engine(back_end)
  |
  |
  | - game_coordinator
  | - game_state_generator
  | - game_state_analysis
  | - game_move_analysis(XAI)
  | - opponent_interaction
  |
  |
- opponent_intelligence
  |
  |
  | - random
  | - dynamic_programming(minimax)
  | - michie's MENACE
  | - reinforcement learning

## Why tic-tac-toe

- zero sum game
- much simpler and smaller board than chess/go
- finite and bound game states

## plans

- 280223 | implement this: https://realpython.com/tic-tac-toe-ai-python/ for game engine and minimax
