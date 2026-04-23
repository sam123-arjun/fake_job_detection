from app.services.ml_service import predict_job_post

title = "Data Analyst"
description = "We are offering a simple copy-paste typing job. You can earn ₹5,000 per day without any experience. Work from mobile or laptop. Hurry up and apply fast. Payment guaranteed."
requirements = """Bachelor’s degree in IT, Computer Science or related field
Knowledge of HTML, CSS, JavaScript
Basic knowledge of React or Angular
Understanding of responsive design
Problem-solving ability
Good teamwork skills"""

try:
    result, confidence, conf_level, explanation = predict_job_post(
        description=description,
        title=title,
        requirements=requirements
    )
    print(f"Result: {result}")
    print(f"Confidence: {confidence}")
    print(f"Confidence Level: {conf_level}")
    print(f"Explanation:")
    for r in explanation:
        print(f" - {r}")
except Exception as e:
    print(f"Error occurred: {e}")
