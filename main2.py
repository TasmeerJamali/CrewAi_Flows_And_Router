from crewai.flow.flow import Flow,listen , start, router  # type: ignore 
import random
class RouteFlow(Flow):
    @start()
    def greeting(self):
        print("Hello from RouteFlow")
        
    @listen("greeting")
    def select_city(self):
        cities=["Karachi","Lahore","Islamabad"]
        select_city=random.choice(cities)
        print(select_city)

@listen("karachi")
def karachi(self,city):
    print("write some fun facts about {city} ")

@listen("lahore")
def lahore(self,city):
    print("write some fun facts about {city} ")

@listen('islamabad')
def islamabad(self,city):
    print("write some fun facts about {city} ")

def kickoff():
    obj = RouteFlow()
    obj.kickoff()
    
def plot():
    obj=RouteFlow()
    obj.plot()


