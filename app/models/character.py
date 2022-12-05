import datetime

class Character():
    def __init__(self, _id, name, alive, species, typo, gender, origin, location_name, episode, image_url, created, episode_n):
        self._id = _id
        self.name = name
        self.alive = alive
        self.species = species
        self.typo = typo
        self.gender = gender
        self.origin = origin
        self.location_name = location_name
        self.episode = episode
        self.image_url = image_url
        self.created = created
        self.episode_n = episode_n

    def to_json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "alive": self.alive,
            "species": self.species,
            "typo": self.typo,
            "gender": self.gender,
            "origin": self.origin,
            "location_name": self.location_name,
            "episode": self.episode,
            "image_url": self.image_url,
            "created": self.created,
            "episode_n": self.episode_n
        }