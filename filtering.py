import numpy as np

# Transition matrix (Motion Model)
motion_model = np.array([[0.7, 0.3], [0.3, 0.7]])

# Observation models for "Umbrella" and "No Umbrella"
observation_model = {
    "U": np.array([[0.9, 0.2], [0.1, 0.8]]),
    "N": np.array([[0.2, 0.1], [0.8, 0.9]])
}

# Initial prior probability
prior = np.array([0.8, 0.2])

# Evidence sequence (umbrella observations)
evidence_sequence = ["U", "N", "N", "U"]

# Filtering and Prediction
for i in range(len(evidence_sequence)):
    print(f"Day {i + 1}")
    # Filtering Step
    prior = np.matmul(motion_model, prior) #updating the belif state for next day without considering evidence
    post = np.matmul(observation_model[evidence_sequence[i]], prior)
    norm = post / np.sum(post)
    # Prediction Step
    prior = np.matmul(motion_model, norm)
    print("--------------------------------------------")
    print(f"Filtering: \n {norm}")
    print(f"Prediction: \n{prior}")
    print("--------------------------------------------")

# Define a threshold for making a decision
threshold = 0.5

# Make a decision based on the final belief state
if prior[0] > threshold:
    today = "Rain"
else:
    today = "No Rain"
    
# Make a decision based on the final belief state
if norm[0] > threshold:
    prediction = "Rain"
else:
    prediction = "No Rain"

# Print the final decision
#print("Final Decision Today:", today)
print("Final Decision Tommorrow:", prediction)
