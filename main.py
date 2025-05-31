from datetime import datetime
from gym_planner.crew import GymPlanner
from langchain_google_genai import ChatGoogleGenerativeAI
import browser_use
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("AIzaSyACfT5FMsWLhsgyEIrVoDdhzIYiyKWgHrg")


def run():
    try:
        goal = input("Enter your fitness goal (e.g., bulking, fat loss, lean bulking): ")
        current_weight = input("Enter your current weight (kg): ")
        activity_level = input("How many days a week do you train? ")
        diet_preference = input("Any diet preferences? (e.g., vegetarian, vegan, none): ")
        budget = input("Enter your supplement/diet budget (e.g., $200): ")
        gender = input("Your gender (optional): ")
        age = input("Your age (optional): ")

        inputs = {
            "goal": goal,
            "current_weight": current_weight,
            "activity_level": activity_level,
            "diet_preference": diet_preference,
            "budget": budget,
            "gender": gender,
            "age": age,
            "date": f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day}",
        }

        GymPlanner().crew().kickoff(inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while running the gym planner crew: {e}")


def get_browser_agent(tasks):
    async def main(tasks):
        agent = browser_use.Agent(
            task=tasks,
            llm=ChatGoogleGenerativeAI(
                model="gemini-2.0-flash",
                api_key="AIzaSyACfT5FMsWLhsgyEIrVoDdhzIYiyKWgHrg",
            ),
        )
        result = await agent.run()

        with open("output/output.txt", "w") as f:
            f.write(str(result))

    asyncio.run(main(tasks))


if __name__ == "__main__":
    run()

    # If you have a browser-based task like supplement shopping or workout video scraping
    with open("output/supplements.txt", "r", encoding="utf-8") as file:
        task = file.read()
    get_browser_agent(task)
