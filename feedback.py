import uuid


class Feedback:
    def __init__(self, item_id, user_email, rating, comment):
        self.feedback_id = str(uuid.uuid4())
        self.item_id = item_id
        self.user_email = user_email
        self.rating = rating
        self.comment = comment


class FeedbackSystem:
    def __init__(self):
        self.feedbacks = []

    def leave_feedback(self, item_id, user_email):
        while True:
            try:
                rating = int(input("Enter a rating between 1 and 10: "))
                if rating < 1 or rating > 10:
                    raise ValueError("Rating must be between 1 and 10.")
                break
            except ValueError as e:
                print(e)

        comment = input("Enter your comment: ")

        feedback = Feedback(item_id, user_email, rating, comment)
        self.feedbacks.append(feedback)
        print("Feedback submitted successfully!\n")

    def view_feedback_for_item(self, item_id):
        item_feedbacks = [fb for fb in self.feedbacks if fb.item_id == item_id]
        if not item_feedbacks:
            print("No feedback for this item.")
        for fb in item_feedbacks:
            print(f"User: {fb.user_email}, Rating: {fb.rating}, Comment: {fb.comment}")

    def view_feedback_by_user(self, user_email):
        user_feedbacks = [fb for fb in self.feedbacks if fb.user_email == user_email]
        if not user_feedbacks:
            print("No feedback from this user.")
        for fb in user_feedbacks:
            print(f"Item ID: {fb.item_id}, Rating: {fb.rating}, Comment: {fb.comment}")
