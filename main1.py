#PROMPT CHAINING, ek ka output doosre ka input, ek ka output doosre ka input, aesy chalta rahega

from crewai.flow.flow import Flow, start, listen  # type: ignore
from litellm import completion 

API_KEY = "AIzaSyA_L-7e3fUB9Y8gBnOhdoVpE-IB6FORIts"

class CityFunFact(Flow):
    @start()
    def generate_random_city(self):
        result = completion(
            model="gemini/gemini-1.5-pro",
            api_key=API_KEY,   # type:ignore
            messages=[{"content": "Generate a random city from Pakistan", "role": "user"}]
        )
        city = result['choices'][0]['message']['content']  # Correctly assign the city name
        print(f"Generated City: {city}")
        return city  # Return city so it can be used in the next step

    @listen("generate_random_city")
    def generate_fun_fact(self, city_name):
        result = completion(
            model="gemini/gemini-1.5-flash",
            api_key=API_KEY,   # type:ignore
            messages=[{"content": f"Write some fun fact about {city_name} city", "role": "user"}]
        )
        fun_fact = result['choices'][0]['message']['content']
        print(f"Fun Fact for {city_name}: {fun_fact}")

        self.state['fun_fact'] = fun_fact  # Save it in state
        return fun_fact  # Return for the next step

    @listen("generate_fun_fact")
    def save_fun_fact(self):
        with open('fun_fact.md', "w") as file:  # Fix syntax error
            file.write(self.state['fun_fact'])  # Write the fun fact correctly
        print("Fun fact saved to fun_fact.md")
        return self.state['fun_fact']

def kickoff():
    obj = CityFunFact()
    result = obj.kickoff()
    print(result)
