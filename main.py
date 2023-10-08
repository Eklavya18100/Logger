import asyncio
from async_logger.log_component import LogComponent


async def main():
    asyncio.create_task(log_component._process_queue())
<<<<<<< HEAD
    # await log_component.queue.join()
=======
    await log_component.queue.join()
>>>>>>> 540f7ee6e928d57cadad95a247bba428bea12605


if __name__ == "__main__":

    log_component = LogComponent()
    # Start processing the log messages
    log_component.write("Log message 1")
    log_component.write("Log message 2")

    asyncio.run(main())
<<<<<<< HEAD
    # log_component.stop(immediate=False)
    # log_component.wait_for_completion()
    # loop.run_until_complete(log_component.stop(immediate=True))  # Stop processing the queue immediately
    # loop.close()
=======
   
>>>>>>> 540f7ee6e928d57cadad95a247bba428bea12605
