import joblib

# Load the trained model and vectorizer
model = joblib.load('./models/trained_model.pkl')
vectorizer = joblib.load('./models/vectorizer.pkl')

def evaluate_password(password):
    password_vec = vectorizer.transform([password]).toarray()
    strength = model.predict(password_vec)
    return strength[0]

if __name__ == "__main__":
    password = input("Enter a password to evaluate: ")
    strength = evaluate_password(password)
    print(f"The password '{password}' is {strength}.")