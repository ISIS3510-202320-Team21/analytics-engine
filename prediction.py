import crud
from collections import defaultdict

# get most played sport by user
def most_played_sport_by_user():
    users = crud.get_all_users()
    sports = crud.get_all_sports()
    for user in users:
        matches = crud.get_matches_of_user(user.id)
        if not matches:
            continue
        user_sports = defaultdict(int)
        for match in matches:
            user_sports[match.sport_id] += 1
        most_played_sport = max(user_sports, key=user_sports.get)
        sport_name = sports[most_played_sport-1].name.lower()
        create_notification_for_user(f"Wanna play a match of {sport_name}?", "createMatch", f"/sport/{most_played_sport}", user.id)

# get most played sport by all users
def most_played_sport():
    users = crud.get_all_users()
    sports = crud.get_all_sports()
    all_sports = defaultdict(int)
    for user in users:
        matches = crud.get_matches_of_user(user.id)
        if not matches:
            continue
        for match in matches:
            all_sports[match.sport_id] += 1
    most_played_sport = max(all_sports, key=all_sports.get)
    sport_name = sports[most_played_sport-1].name
    for user in users:
        create_notification_for_user(f"{sport_name} is very popular! Match with someone!", "createMatch", f"/sport/{most_played_sport}", user.id)

# create notification for user
def create_notification_for_user(name: str, type: str, redirectTo: str, user_id: int):
    return crud.create_user_notification(name, type, redirectTo, user_id)