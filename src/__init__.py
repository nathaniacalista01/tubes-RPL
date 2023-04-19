"""Utilities"""
import os.path


def load_profile():
    profile = {}
    path = os.path.join(os.path.dirname(__file__), "profile.config")
    with open(path, "r") as file:
        for line in file.readlines():
            key, *value = line.split(":")
            value = "".join(value)
            profile[key.strip()] = value.strip()
    return profile


def save_profile(profile: dict[str, str]):
    path = os.path.join(os.path.dirname(__file__), "profile.config")
    with open(path, "w") as file:
        for k, v in profile.items():
            file.write(f"{k}: {v}\n")
