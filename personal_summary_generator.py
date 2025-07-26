
import random
import os
from datetime import datetime

class PersonalSummaryGenerator:
    def __init__(self):
        self.question_pools = {
            'name': ["What's your name?", "What should I call you?", "What's your full name?"],
            'age': ["How old are you?", "What's your age?", "How many years have you been on this planet?"],
            'color': ["What's your favorite color?", "Which color makes you happy?", "What color do you love most?"],
            'food': ["What's your favorite food?", "What's your go-to meal?", "What food could you eat every day?"],
            'city': ["Which city do you live in?", "What's your hometown?", "Where do you call home?"],
            'school': ["Which SHS did you attend?", "What's the name of your senior high school?", "Where did you go for SHS?"],
            'team': ["What's your favorite soccer team?", "Which football club do you support?", "Who's your favorite soccer team?"],
            'hobby': ["What's your favorite hobby?", "What do you like to do in your free time?", "What's your passion?"],
            'music': ["What's your favorite music genre?", "What type of music do you love?", "What music gets you pumped up?"],
            'movie': ["What's your favorite movie?", "Which movie could you watch over and over?", "What's the best movie you've seen?"],
            'season': ["What's your favorite season?", "Which time of year do you love most?", "Summer, winter, spring, or autumn?"],
            'animal': ["What's your favorite animal?", "Which animal do you find most amazing?", "If you could be any animal, what would it be?"]
        }

        self.fun_responses = [
            "Wow, that's awesome!",
            "Great choice!",
            "Interesting!",
            "Cool!",
            "Nice one!",
            "That's fantastic!",
            "Excellent taste!",
            "I love that too!"
        ]

        self.ratings = []

    def get_random_questions(self, num_questions=7):
        available_keys = list(self.question_pools.keys())
        required = ['name', 'age', 'city']
        optional = [key for key in available_keys if key not in required]
        selected = required + random.sample(optional, min(num_questions - len(required), len(optional)))
        return selected[:num_questions]

    def ask_question(self, question_type):
        question = random.choice(self.question_pools[question_type])
        response = input(f"\n{question} ")
        if question_type != 'name':
            print(f"  → {random.choice(self.fun_responses)}")
        return response

    def generate_summary(self, user_data):
        name = user_data.get('name', 'Friend')
        age = user_data.get('age', 'unknown age')
        city = user_data.get('city', 'somewhere amazing')
        summary = f"\n{'='*50}\n"
        summary += f"✨ PERSONAL SUMMARY FOR {name.upper()} ✨\n"
        summary += f"{'='*50}\n\n"
        summary += f"Hello, {name}! 👋\n\n"
        summary += f"You are {age} years old and life must be awesome in {city}!\n\n"

        details = []
        if 'color' in user_data:
            details.append(f"love the color {user_data['color']}")
        if 'food' in user_data:
            details.append(f"enjoy eating {user_data['food']}")
        if 'team' in user_data:
            details.append(f"support {user_data['team']} in soccer")
        if 'school' in user_data:
            details.append(f"went to {user_data['school']} for SHS")
        if 'hobby' in user_data:
            details.append(f"love spending time on {user_data['hobby']}")
        if 'music' in user_data:
            details.append(f"jam to {user_data['music']} music")
        if 'movie' in user_data:
            details.append(f"could watch {user_data['movie']} on repeat")
        if 'season' in user_data:
            details.append(f"feel most alive during {user_data['season']}")
        if 'animal' in user_data:
            details.append(f"find {user_data['animal']}s absolutely amazing")

        if details:
            if len(details) == 1:
                summary += f"You {details[0]}.\n"
            elif len(details) == 2:
                summary += f"You {details[0]} and {details[1]}.\n"
            else:
                summary += f"You {', '.join(details[:-1])}, and {details[-1]}.\n"

        summary += f"\nWhat an interesting person you are, {name}! 🌟\n"
        summary += f"{'='*50}\n"
        return summary

    def save_to_file(self, name, summary, rating):
        filename = f"{name.replace(' ', '_')}.txt"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Personal Summary - Generated on {timestamp}\n")
                f.write(summary)
                f.write(f"\nAssistant Rating: {rating}/5 stars ⭐\n")
            print(f"\n✅ Summary saved successfully as '{filename}'!")
            return True
        except Exception as e:
            print(f"\n❌ Error saving file: {e}")
            return False

    def get_rating(self):
        while True:
            try:
                print("\n" + "="*30)
                rating = input("How would you rate this assistant? (1-5 stars): ")
                rating_num = int(rating)
                if 1 <= rating_num <= 5:
                    stars = "⭐" * rating_num
                    print(f"Thanks for the {rating_num}/5 rating! {stars}")
                    self.ratings.append(rating_num)
                    return rating_num
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Please enter a valid number between 1 and 5.")

    def run(self):
        print("🎉 Welcome to the Personal Summary Generator! 🎉")
        print("I'll ask you some fun questions and create a personalized summary!")
        while True:
            print("\n🚀 Starting new session...")
            question_types = self.get_random_questions()
            user_data = {}
            for q_type in question_types:
                user_data[q_type] = self.ask_question(q_type)
            summary = self.generate_summary(user_data)
            print(summary)
            rating = self.get_rating()
            while True:
                save_choice = input("\nWould you like to save this summary to a file? (y/n): ").lower().strip()
                if save_choice in ['y', 'yes']:
                    self.save_to_file(user_data['name'], summary, rating)
                    break
                elif save_choice in ['n', 'no']:
                    print("No problem! Summary not saved.")
                    break
                else:
                    print("Please enter 'y' for yes or 'n' for no.")
            while True:
                restart = input("\nWould you like to create another summary? (y/n): ").lower().strip()
                if restart in ['y', 'yes']:
                    break
                elif restart in ['n', 'no']:
                    if self.ratings:
                        avg_rating = sum(self.ratings) / len(self.ratings)
                        print("\n📊 Final Stats:")
                        print(f"   • Sessions completed: {len(self.ratings)}")
                        print(f"   • Average rating: {avg_rating:.1f}/5.0 stars")
                    print("\n👋 Thanks for using Personal Summary Generator!")
                    print("Have a wonderful day! 🌟")
                    return
                else:
                    print("Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    generator = PersonalSummaryGenerator()
    generator.run()
