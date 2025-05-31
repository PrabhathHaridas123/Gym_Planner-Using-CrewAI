 🏋️‍♂️ GymPlanner AI Crew

this is an AI-powered personal fitness assistant built using the [CrewAI](https://docs.crewai.com) framework. It brings together a crew of expert agents to help users define fitness goals, calculate macros, plan diets, schedule workouts, recommend supplements, and optimize lifestyle habits.
------------------------------------------------------------------------------------------------------------------------------------------
Each agent has a specific role in the fitness journey:

Goal Setting Agent – Helps define your fitness goals (bulking, fat loss, etc.)

Macro Calculator Agent – Calculates TDEE and macro requirements

Diet Planner Agent – Creates a personalized meal plan

Workout Schedule Agent – Designs your weekly workout split

Training Plan Agent – Integrates training strategies and progression

Supplement Agent – Suggests evidence-based supplements

Progress Tracking Agent – Builds a system to track progress

Lifestyle Optimizer Agent – Recommends recovery, sleep, hydration, and stress tips

Browser Agent – Fetches real-time fitness information via Serper search

✅ Tasks Defined (config/tasks.yaml)
Each task is handled by a dedicated agent:

Task	Description	Agent
Goal Setting	Understand user goals	goal_setting_agent
Macro Calculator	Compute TDEE and macros	macro_calculator_agent
Diet Planning	Generate meal plans	diet_planner_agent
Workout Schedule	Build a weekly workout routine	workout_schedule_agent
Training Plan	Long-term training strategy	training_plan_agent
Supplement Recommendations	Suggest fitness supplements	supplement_recommendation_agent
Progress Tracking	System for measuring and adjusting progress	progress_tracking_agent
Lifestyle Optimization	Provide wellness and recovery tips	lifestyle_optimizer_agent
Web Search	Real-time data from the internet	browser_agent




📦 Output
Each agent writes results to the /output/ folder:



macro_calculator_task.md

diet_planner_task.md
and more...
