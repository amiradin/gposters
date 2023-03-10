import os


def create_folder():
    if not "posters" in os.listdir():
        os.mkdir("posters")


def write_file(bin_data, filename):
    with open(f"posters/{filename}", "wb") as file:
        file.write(bin_data)


async def fetch_content(url, session):
    async with session.get(url) as response:
        filename = response.url.path.split("/")[-1]
        bin_file = await response.read()
        write_file(bin_data=bin_file, filename=filename)
