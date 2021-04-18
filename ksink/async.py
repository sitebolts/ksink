#https://stackoverflow.com/a/61478547/1741346
async def gather_with_concurrency(num_threads, *tasks):
    semaphore = asyncio.Semaphore(num_threads)

    async def sem_task(task):
        async with semaphore:
            return await task
    return await asyncio.gather(*(sem_task(task) for task in tasks))
