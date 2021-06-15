FROM mongo

COPY songs.json /songs.json
CMD mongoimport --host mongodb --db dev --collection song --type json --file /songs.json --jsonArray