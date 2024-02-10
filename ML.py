def reward_function(params):

  track_width = params['track_width']
  distance_from_center = params['distance_from_center']

  market_1 = 0.1 * track_width
  market_2 = 0.5 * track_width

  if distance_from_center <= market_1:
    reward = 2.0 # Close to center line
  elif distance_from_center <= market_2:
    reward = 0.2 # Futher from center line
  else:
    reward = 1e-3 # Off track

  return float(reward)