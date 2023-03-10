import asyncio
import aiohttp
import utils


async def main(count_of_posters):
    URL = "https://api.lorem.space/image/movie?w=150&h=220"
    tasks = []

    async with aiohttp.ClientSession() as session:
        for _ in range(count_of_posters):
            task = asyncio.create_task(utils.fetch_content(url=URL, session=session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == "__main__":
    utils.create_folder()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    count_of_posters = int(input("Enter count of posters: "))
    asyncio.run(main(count_of_posters))
