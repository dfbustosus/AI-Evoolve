# Import necessary libraries
require 'pandas'
require 'numpy'
require 'scikit-learn'

# Generate random sample data for a binary classification problem
X = np.random.rand(100, 4)  # 100 samples with 4 features each
y = np.random.choice([0, 1], size=100)  # Random labels of either 0 or 1

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a logistic regression model and fit it to the training data
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the testing set
predictions = model.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)

puts "Model Accuracy: #{accuracy}"
puts "Model Precision: #{precision}"
puts "Model Recall: #{recall}"
puts "Model F1 Score: #{f1}"
