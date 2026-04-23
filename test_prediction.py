import requests
import json

url = 'http://localhost:8000/api/v1/jobs/analyze'
data = {
  "title": "Data Analyst",
  "company": "Unknown",
  "description": "We are offering a simple copy-paste typing job. You can earn ₹5,000 per day without any experience. Work from mobile or laptop. Hurry up and apply fast. Payment guaranteed.",
  "requirements": "Bachelor’s degree in IT, Computer Science or related field\nKnowledge of HTML, CSS, JavaScript\nBasic knowledge of React or Angular\nUnderstanding of responsive design\nProblem-solving ability\nGood teamwork skills"
}

try:
    response = requests.post(url, json=data)
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print(f"Error: {e}")
