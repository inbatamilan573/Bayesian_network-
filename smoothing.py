import numpy as np

# Transition matrix (Motion Model)
transition_matrix = np.array([[0.7, 0.3], [0.3, 0.7]])

# Observation models for "Umbrella" and "No Umbrella"
observation_models = {
    "U": np.array([[0.9, 0], [0, 0.2]]),
    "N": np.array([[0.1, 0], [0, 0.8]])
}

# Initial prior probability for day 0
prior_day_0 = np.array([[0.5], [0.5]])

# Evidence sequence
evidence_sequence = "UUNN"

# Day to smooth backward from the end
k = 1

# Forward Filtering
filtered_probabilities = {0: prior_day_0}
for i in range(len(evidence_sequence)):
    prior_prob = np.matmul(transition_matrix, filtered_probabilities[i])
    post_prob = np.matmul(observation_models[evidence_sequence[i]], prior_prob)
    norm_prob = post_prob / np.sum(post_prob)
    filtered_probabilities[i + 1] = norm_prob
  

# Backward Smoothing
backward_result = 1
for i in range(k, len(evidence_sequence)):
    transition_matrix_k = np.dot(backward_result, transition_matrix)
    backward_result = np.dot(observation_models[evidence_sequence[i]], transition_matrix_k)
    
    # Smoothing at day k
    smoothed_result = np.dot(backward_result, filtered_probabilities[k])
    smoothed_result = smoothed_result / np.sum(smoothed_result)

# Print the results
print("Before Smoothing:")
print(f"Rain in day {k}: {filtered_probabilities[k]}")

print("\nAfter Smoothing:")
print(f"Rain in day {k}: {smoothed_result}")

# Define a threshold for making a decision
threshold = 0.5

    
# Make a decision based on the final belief state
if smoothed_result[0] > threshold:
    prediction = "Rain"
else:
    prediction = "No Rain"

# Print the final decision

print(f"Final Decision in day {k}:", prediction)


