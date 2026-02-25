# role_predictor.py
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Example dataset (skills -> role)
data = [
    ("Python Machine Learning SQL", "Data Scientist"),
    ("JavaScript HTML CSS", "Frontend Developer"),
    ("Python Django SQL", "Backend Developer"),
    ("C++ Java", "Software Engineer"),
]

# Split skills and labels
X = [x[0] for x in data]
y = [x[1] for x in data]

# Vectorize skills
vectorizer = CountVectorizer()
X_vect = vectorizer.fit_transform(X)

# Train a classifier
model = MultinomialNB()
model.fit(X_vect, y)

# Save model and vectorizer
with open("role_model.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)

# Function to predict role
def predict_role(skills_list):
    with open("role_model.pkl", "rb") as f:
        model, vectorizer = pickle.load(f)
    skills_str = " ".join(skills_list)
    vect = vectorizer.transform([skills_str])
    return model.predict(vect)[0]

# Example usage
if __name__ == "__main__":
    print(predict_role(["Python", "SQL", "Machine Learning"]))  # Output: Data Scientist