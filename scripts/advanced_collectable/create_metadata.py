from black import re
from metadata.sample_metadata import metadata_template
from scripts.helpful_scripts import get_breed
from brownie import AdvancedCollectable, network
from pathlib import Path
import requests


def main():
    advanced_collectable = AdvancedCollectable[-1]
    number_of_advanced_collectable = advanced_collectable.tokenCounter()
    print(f"You have created {number_of_advanced_collectable} collectables!")
    for token_id in range(number_of_advanced_collectable):
        breed = get_breed(advanced_collectable.tokenIdToBreed(token_id))
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        )
        collectable_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists! Delete it to overwrite")
        else:
            print(f"Creating Metadata file: {metadata_file_name}")
            collectable_metadata["name"] = breed
            collectable_metadata["description"] = f"A cute {breed} pup!"
            image_path = "./img/" + breed.lower().replace("_", "-") + ".png"
            image_uri = upload_to_ipfs(image_path)
            # collectable_metadata["image"] = image_uri


def upload_to_ipfs(filepath):
    # Opening the file in binary
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        # "./img/0-PUG.png" -> "0-PUG.png"
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
