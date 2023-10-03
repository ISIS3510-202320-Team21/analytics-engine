import schedule, time, prediction

MEASURE_INTERVAL = 1

# Define a job function to be executed
def most_played_sport_by_user():
    print("Prediction of most played sport by user started")
    prediction.most_played_sport_by_user()

# Define a job function to be executed
def most_played_sport():
    print("Prediction of most played sport started")
    prediction.most_played_sport()

def start():
    # Create a job and schedule it to run every minute
    schedule.every(MEASURE_INTERVAL).days.do(most_played_sport_by_user)
    schedule.every(MEASURE_INTERVAL).days.do(most_played_sport)

    # Run the scheduled job
    while True:
        schedule.run_pending()
        time.sleep(1)

start()