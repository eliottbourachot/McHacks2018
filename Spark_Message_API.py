#need to do: pip install ciscosparkapi first

from __future__ import print_function
from ciscosparkapi import CiscoSparkAPI
import os

DEMO_ROOM_NAME = "You've got a match"
DEMO_PEOPLE = ["eliott.bourachot@gmail.com"]
DEMO_MESSAGE = "We found you a friend"

api = CiscoSparkAPI(access_token='MTQxNjUxMWYtYjA3My00M2UzLTlkMzItN2M2MmE4Y2JlNGMzMWFjNmRmMWQtMjJj')
    # Create a CiscoSparkAPI connection object; uses your SPARK_ACCESS_TOKEN
# Clean up previous demo rooms
print("Searching for existing demo rooms...")
rooms = api.rooms.list()                                                          # Creates a generator container (iterable) that lists the rooms where you are a member
existing_demo_rooms = [room for room in rooms if room.title == DEMO_ROOM_NAME]    # Builds a list of rooms with the name DEMO_ROOM_NAME
if existing_demo_rooms:
    print("Found {} existing room(s); deleting them."
          "".format(len(existing_demo_rooms)))
    for room in existing_demo_rooms:
        api.rooms.delete(room.id)                                                # Delete the room
        print("Room '{}' deleted.".format(room.id))


demo_room = api.rooms.create(DEMO_ROOM_NAME)                          # Create a new demo room
print(demo_room)                                                      # Print the room details (formatted JSON)
for person_email in DEMO_PEOPLE:
    api.memberships.create(demo_room.id, personEmail=person_email)    # Add people to the room
message = api.messages.create(demo_room.id, text=DEMO_MESSAGE)        # Create a message in the new room
print(message)