observations = {
    1: {
        "time": "8:30",
        "cars": 4,
        "pedestrians": 2,
        "bikes": 1,
        "intersection_type": "4-way stop",
        "infractions": "None",
        "notes": "Light morning traffic"
    },
    2: {
        "time": "8:32",
        "cars": 7,
        "pedestrians": 5,
        "bikes": 0,
        "intersection_type": "Traffic light",
        "infractions": "1 jaywalker",
        "notes": "Students crossing to school"
    },
    3: {
        "time": "8:34",
        "cars": 5,
        "pedestrians": 4,
        "bikes": 2,
        "intersection_type": "4-way stop",
        "infractions": "None",
        "notes": "Delivery truck turning"
    },
    4: {
        "time": "8:36",
        "cars": 6,
        "pedestrians": 3,
        "bikes": 1,
        "intersection_type": "Traffic light",
        "infractions": "1 rolling stop",
        "notes": "Steady flow"
    },
    5: {
        "time": "8:38",
        "cars": 3,
        "pedestrians": 1,
        "bikes": 0,
        "intersection_type": "4-way stop",
        "infractions": "None",
        "notes": "Very quiet"
    },
    6: {
        "time": "8:40",
        "cars": 8,
        "pedestrians": 6,
        "bikes": 1,
        "intersection_type": "Traffic light",
        "infractions": "None",
        "notes": "School rush"
    },
    7: {
        "time": "8:42",
        "cars": 5,
        "pedestrians": 2,
        "bikes": 3,
        "intersection_type": "Traffic light",
        "infractions": "1 car ran red",
        "notes": "Bike group passing"
    },
    8: {
        "time": "8:44",
        "cars": 4,
        "pedestrians": 3,
        "bikes": 0,
        "intersection_type": "4-way stop",
        "infractions": "None",
        "notes": "Bus drop-off nearby"
    },
    9: {
        "time": "8:46",
        "cars": 6,
        "pedestrians": 4,
        "bikes": 2,
        "intersection_type": "Traffic light",
        "infractions": "None",
        "notes": "Busy but smooth"
    },
    10: {
        "time": "8:48",
        "cars": 7,
        "pedestrians": 5,
        "bikes": 1,
        "intersection_type": "4-way stop",
        "infractions": "1 car ran stop",
        "notes": "Rush starting again"
    }
}


# ===============================
#   ACCESSING A SINGLE OBSERVATION
# ===============================

def get_observation(observations, number):
    # Returns the observation dictionary for a specific observation number.
    # For example: get_observation(observations, 1) returns the first observation.
    # Returns: dict (e.g. {'time': '10:05', 'cars': 14, ...})
    return observations[number]


# ===============================
#   ACCESSING INDIVIDUAL DATA POINTS
# ===============================

def get_observation_time(obs):
    # Returns the time string from a single observation.
    # Returns: str
    return obs["time"]

def get_observation_cars(obs):
    # Returns the number of cars counted during one observation.
    # Returns: int
    return obs["cars"]

def get_observation_pedestrians(obs):
    # Returns the number of pedestrians counted during one observation.
    # Returns: int
    return obs["pedestrians"]

def get_observation_bikes(obs):
    # Returns the number of bikes counted during one observation.
    # Returns: int
    return obs["bikes"]

def get_observation_type(obs):
    # Returns the type of intersection (e.g. '4-way stop', 'Traffic light').
    # Returns: str
    return obs["intersection_type"]

def get_observation_notes(obs):
    # Returns the notes recorded for a single observation.
    # Returns: str
    return obs["notes"]


# ===============================
#   AGGREGATION FUNCTIONS (WORK FOR ANY SIZE DICTIONARY)
# ===============================

def get_num_observations(observations):
    # Returns the total number of observations recorded.
    # Returns: int
    return len(observations)

def get_total_cars(observations):
    # Calculates the total number of cars across all observations.
    # Returns: int
    total = 0
    for obs_num in observations:
        obs = get_observation(observations, obs_num)
        total += get_observation_cars(obs)
    return total

def get_total_pedestrians(observations):
    # Calculates the total number of pedestrians across all observations.
    # Returns: int
    total = 0
    for obs_num in observations:
        obs = get_observation(observations, obs_num)
        total += get_observation_pedestrians(obs)
    return total

def get_average_bikes(observations):
    # Calculates the average number of bikes per observation.
    # Returns: float
    total = 0
    for obs_num in observations:
        obs = get_observation(observations, obs_num)
        total += get_observation_bikes(obs)
    return total / get_num_observations(observations)


# ===============================
#   FORMATTING & PRINTING HELPERS
# ===============================

def format_observation_row(obs_num, time, cars, peds, bikes, inter_type, notes):
    # Formats a single row of observation data for display in a table.
    # Returns: str (a nicely formatted line of data)
    print() # replace print with your code

def print_table_header():
    # Prints the header section for the table of observations.
    # Returns: None
    print() # replace print with your code

def print_totals(total_cars, total_peds, avg_bikes):
    # Prints the total cars, total pedestrians, and average bikes
    # after all observations are displayed.
    # Returns: None
    print() # replace print with your code

ob1 = get_observation(observations,3)
print(get_observation_cars(ob1))

print(f"Total pedestrians: {get_total_pedestrians(observations)}")



