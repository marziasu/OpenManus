import asyncio

from app.agent.manus import Manus
from app.logger import logger


async def main():
    agent = Manus()
    try:
        # prompt = input("Enter your prompt: ")
        # prompt = (
        #     "Scrape the titles, intro paragraphs, links and the current scraping time "
        #     "of each news article from https://www.dailynayadiganta.com/latest. "
        #     "Return the result as a JSON list. Each item should include: "
        #     "`title`, `intro`, `link`, and `scraping_time`. "
        #     "Do not return anything else. Just clean JSON output."
        #     "After scraping, save the JSON output to a file named `nayadiganta_latest.json`."
        # )

        prompt = (
            "Go to https://www.dailynayadiganta.com/latest and scrape all visible news article entries. "
            "For each article on the page, extract:\n"
            "- The article `title`\n"
            "- The `intro` (summary or first visible paragraph)\n"
            "- The article `link`\n"
            "- The `published_time` if it exists on the article or page\n"
            "- The `scraping_time` (current timestamp)\n\n"
            "Return the result as a clean JSON list. Each item should include exactly:\n"
            "`title`, `intro`, `link`, `published_time`, and `scraping_time`.\n"
            "Do not return anything else — just clean JSON.\n"
            "After scraping, save the JSON result to a file named `nayadiganta_latest.json`."
        )


        if not prompt.strip():
            logger.warning("Empty prompt provided.")
            return

        logger.warning("Processing your request...")
        await agent.run(prompt)
        logger.info("Request processing completed.")
    except KeyboardInterrupt:
        logger.warning("Operation interrupted.")
    finally:
        # Ensure agent resources are cleaned up before exiting
        await agent.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
